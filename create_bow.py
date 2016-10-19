import re
import sys
import getopt
import json
import data_io
import multiprocessing
from os.path import basename
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import Counter

DELIMITER = ','
LANG = 'german'
CSV_DATA_COL = 0
XML_DATA_ELEMENT = 'data'
WORD_LEN_THRESHOLD = 0

# Create bag of words.
def create_clean_bow(word_list, as_list=True):
    stemmer = SnowballStemmer(language=LANG)
    lemmatizer = WordNetLemmatizer()
    out_list = list()
    reg_nonaplha = re.compile("\W")
    for word in word_list:
        out_word = reg_nonaplha.sub('',word)
        if out_word.lower() not in stopwords.words(LANG):
            out_word = stemmer.stem(out_word)
            out_word = lemmatizer.lemmatize(out_word)
            if out_word != '':
                # Skip tokens that have a size below the defined threshold.
                if len(out_word) >= WORD_LEN_THRESHOLD:
                    out_list.append(out_word)
    if as_list:
        return out_list
    else:
        return Counter(out_list)

'''
    Prints how to use this application.
'''
def usage():
        print('This tool creates a BOW from raw Manifestos and Spiegel articles.')
        print('Usage for %s.' % sys.argv[0])
        print('%s [-h|--help] -m|--manifesto <path to manifesto (csv)> -s|--spiegel <path to corpus(xml)>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-m | --manifesto: Path where the manifesto is located. The file format has to be CSV.'
              ' Option can be used multiple times.')
        print('\t-s | --spiegel: Path where the spiegel corpa is located. The file format has to be XML. '
              'Option can be used multiple times.')

article_list = dict()
def callback_spiegel(article):
    for article_id, article_data in article:
        article_list[article_id][data_io.DATA_FIELD] = article_data

def apply_spiegel(article):
    article_id, article_data = article
    result = create_clean_bow(article_data[data_io.DATA_FIELD])
    return (article_id, result)

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'm:s:h', ['manifesto=', 'spiegel=', 'help'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    spiegel_list = list()
    manifesto_list = list()
    for option, argument in opts:
        if option in ('-h', '--help'):
            usage()
            sys.exit()
        elif option in ('-s', '--spiegel'):
            spiegel_list.append(argument)
        elif option in ('-m', '--manifesto'):
            manifesto_list.append(argument)
        else:
            usage()
            sys.exit()

    if len(spiegel_list) > 0:
        print('[', end='')
        first = True
        for s in spiegel_list:
            article_list.clear()
            article_list = data_io.read_spiegel_data(s)
            p = multiprocessing.Pool(multiprocessing.cpu_count())
            p.map_async(apply_spiegel, article_list.items(), callback=callback_spiegel)
            p.close()
            p.join()
            if not first:
                print(', ')
            first = False
            print(json.dumps(article_list, ensure_ascii=False, sort_keys=True), end='')
        print(']')

    if len(manifesto_list) > 0:
        print('{', end='')
        first = True
        for s in manifesto_list:
            if not first:
                print(', ')
            first = False
            print('"' + basename(s) + '":' + json.dumps(create_clean_bow(data_io.read_manifesto_data(s)), ensure_ascii=False, sort_keys=True), end='')
        print('}')