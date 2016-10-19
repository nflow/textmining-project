import json
import sys
import getopt
from sys import stderr
import nltk
from collections import Counter
from collections import OrderedDict
import data_io
import create_bow
import os
import tf_idf
import ijson

ID_M_SENTS = 'sents'
ID_M_WORDS = 'words'
ID_M_BOW = 'bow'

ID_M_FACTS = 'facts'
ID_M_HOT_WORDS = 'hot_words'
ID_M_HOT_WORDS_NORMALIZED = 'hot_words_normalized'
ID_M_HOT_WORDS_TFIDF = 'hot_words_tfidf'
ID_M_FACTS = 'facts'

ID_S_ARTICLE_COUNT = 'article_count'
ID_S_AVG_SENTS = 'article_avg_sents'
ID_S_AVG_WORDS = 'article_avg_words'
ID_S_CATEGORIES = 'categories'

FACT_UNIQUE_WORDS = 'uniqu_word_count'
FACT_WORD_COUNT = 'word_count'
FACT_WORD_BOW_RATIO = 'word_bow_ratio'
FACT_BOW_COUNT = 'bow_count'
FACT_LEXICAL_DIVERSITY = 'lexical_diversity'
FACT_SENT_COUNT = 'sent_count'
FACT_SENT_DUPLICATE_COUNT = 'sent_duplicate_count'

ROUND_DIGITS = 4

RESULT_LENGTH =  10

VERBOSE = True

def printv(*args, **kwargs):
    if VERBOSE:
        print(*args, file=stderr, **kwargs)


def m_general_facts(sents, words, bow):
    result = OrderedDict()
    result[FACT_WORD_COUNT] = len(words)
    result[FACT_BOW_COUNT] = len(bow)
    result[FACT_WORD_BOW_RATIO] = round(result[FACT_BOW_COUNT]  / result[FACT_WORD_COUNT],ROUND_DIGITS)
    result[FACT_UNIQUE_WORDS] = len(set(words))
    result[FACT_LEXICAL_DIVERSITY] = round(result[FACT_UNIQUE_WORDS] / result[FACT_WORD_COUNT],ROUND_DIGITS)
    result[FACT_SENT_COUNT] = len(sents)
    result[FACT_SENT_DUPLICATE_COUNT] = [s for s in Counter(sents).items() if s[1] > 2]
    return result


def m_hot_words(bow):
    bow = Counter(bow)
    result = dict()
    for word, count in bow.most_common(RESULT_LENGTH):
        result[word] = count
    return result

def m_hot_words_normalized(bow):
    bow = Counter(bow)
    result = dict()
    for word, count in list(map(lambda e: (e[0],round(e[1]/len(bow),ROUND_DIGITS)),bow.most_common(RESULT_LENGTH))):
        result[word] = count
    return result

def m_hot_words_tfidf(data):
    printv('Calculateing idf score.')
    idf = tf_idf.idf([v[ID_M_BOW] for v in data.values()])
    all_result = dict()
    for id, bow in data.items():
        printv('Calculateing tf-idf score for ' + id)
        result = list()
        for term in set(bow[ID_M_BOW]):
            tf = tf_idf.tf(term, bow[ID_M_BOW])
            result.append((term, round(tf_idf.tfidf(term, tf, idf), ROUND_DIGITS)))
        all_result[id] = dict()
        for word, score in sorted(result, key=lambda x: x[1], reverse=True)[:RESULT_LENGTH]:
            all_result[id][word] = score
    return all_result


def m_create_statistics(manifesto_list, file_output=None):
    all_data = dict()
    all_results = OrderedDict()
    for file in manifesto_list:
        basename = os.path.basename(file)
        all_data[basename] = dict()
        all_results[basename] = dict()
        printv('Loading file ' + basename + ' ...')
        all_data[basename][ID_M_SENTS] = data_io.read_manifesto_data(file, as_word_list=False)
        all_data[basename][ID_M_WORDS] = data_io.read_manifesto_data(file, as_word_list=True)
        all_data[basename][ID_M_BOW] = create_bow.create_clean_bow(all_data[basename][ID_M_WORDS])

    for name, data in all_data.items():
        facts = m_general_facts(data[ID_M_SENTS], data[ID_M_WORDS], data[ID_M_BOW])
        all_results[name][ID_M_FACTS] = facts

    for name, data in all_data.items():
        all_results[name][ID_M_HOT_WORDS] = m_hot_words(data[ID_M_BOW])

    for name, data in all_data.items():
        all_results[name][ID_M_HOT_WORDS_NORMALIZED] = m_hot_words_normalized(data[ID_M_BOW])

    all_tfidf = m_hot_words_tfidf(all_data)
    for name, tfidf in all_tfidf.items():
        all_results[name][ID_M_HOT_WORDS_TFIDF] = tfidf

    if file_output is None:
        print(json.dumps(all_results, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(all_results, outfile)

def s_create_statistics(spiegel_sents_json, file_output=None):
    statistics = dict()
    with open(spiegel_sents_json, 'rb') as file:
        data = ijson.items(file, 'item')
        for y_data in data:
            for a_id, a_data in y_data.items():
                if a_data['data'] is not None:
                    year = a_data['date'][4:]
                    if year not in statistics:
                        statistics[year] = dict()
                        statistics[year][ID_S_ARTICLE_COUNT] = 0
                        statistics[year][ID_S_AVG_SENTS] = 0
                        statistics[year][ID_S_AVG_WORDS] = 0
                        statistics[year][ID_S_CATEGORIES] = list()
                    statistics[year][ID_S_ARTICLE_COUNT] += 1
                    statistics[year][ID_S_AVG_SENTS] += len(a_data[data_io.DATA_FIELD])
                    statistics[year][ID_S_AVG_WORDS] += len(' '.join(a_data[data_io.DATA_FIELD]).split(' '))
                    statistics[year][ID_S_CATEGORIES].append(a_data[data_io.CATEGORY_FIELD])
            statistics[year][ID_S_AVG_SENTS] = round(statistics[year][ID_S_AVG_SENTS] / statistics[year][ID_S_ARTICLE_COUNT])
            statistics[year][ID_S_AVG_WORDS] = round(statistics[year][ID_S_AVG_WORDS] / statistics[year][ID_S_ARTICLE_COUNT])
            statistics[year][ID_S_CATEGORIES] = Counter(statistics[year][ID_S_CATEGORIES])

    if file_output is None:
        print(json.dumps(statistics, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(statistics, outfile)

def usage():
    print('This tool resturns facts about a Manifesto or a Spiegel corpus.')
    print('Usage for %s.' % sys.argv[0])
    print('%s [-h|--help] -m|--manifesto <path to manifesto sentence list> -s|--spiegel <path to spiegel sentence list> -o|--output-file <path to output file>' % sys.argv[0])
    print('Options:')
    print('\t-h | --help: Prints the help.')
    print('\t-s | --spiegel: Path to Spiegel sentence list in JSON format, created by data_io.py.')
    print('\t-m | --manifesto: Path to Manifesto sentence list in JSON format, created by data_io.py.')
    print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:m:o:h', ['spiegel=', 'manifesto=', 'output-file=', 'help'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    manifesto_list = list()
    spiegel_json = None
    output_file = None
    for option, argument in opts:
        if option in ('-h', '--help'):
            usage()
            sys.exit()
        elif option in ('-s', '--spiegel'):
            spiegel_json = argument
        elif option in ('-o', '--output-file'):
            output_file = argument
        elif option in ('-m', '--manifesto'):
            manifesto_list.append(argument)
        else:
            usage()
            sys.exit()
    if len(manifesto_list) > 0:
        m_create_statistics(manifesto_list, output_file)
    if spiegel_json is not None:
        s_create_statistics(spiegel_json, output_file)
