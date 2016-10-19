from sys import stderr
import ijson
import json
import data_io
import re, math
from collections import Counter
import sys
import getopt

VERBOSE = True
OUTPUT_JSON = True
SKIP_BOW_CREATION = True
WORD = re.compile(r'\w+')

#used for printing output on the command line.
def printv(*args, **kwargs):
        if VERBOSE:
            print(*args, file=stderr, **kwargs)

# Calculate cosine similarity
def get_cosine(vec1, vec2):
     intersec = set(vec1.keys()) & set(vec2.keys())
     num = sum([vec1[x] * vec2[x] for x in intersec])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denom = math.sqrt(sum1) * math.sqrt(sum2)

     if not denom:
        return 0.0
     else:
        return float(num) / denom

# Create for a given text a Vector that is based on the term frequency
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

'''
Calculate similarity between manifestos and spiegel articles taken as input. For cosine the term frequency is used
for vector representation
'''
def cosine_m2s_from_json(file_manifesto_json, file_spiegel_json, file_output=None):
    result = dict()
    with open(file_manifesto_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
    with open(file_spiegel_json) as fh_spiegel:
        stream_spiegel = ijson.items(fh_spiegel, 'item')
        for spiegel_part in stream_spiegel:
            for manifesto_id, manifesto_data in manifesto_dataset.items():
                spiegel_part_len = len(spiegel_part)
                manifesto_counter = Counter(manifesto_data)
                i = 0
                for article_id, article_data in spiegel_part.items():
                    i += 1
                    printv("Working on manifesto " + str(manifesto_id) + ". Article progress: " + str(i) + "/" + str(
                        spiegel_part_len))
                    if len(article_data[data_io.DATA_FIELD]) > 0:
                        article_date = article_data[data_io.DATE_FIELD]
                        article_category = article_data[data_io.CATEGORY_FIELD]
                        if manifesto_id not in result:
                            result[manifesto_id] = dict()
                        if article_date not in result[manifesto_id]:
                            result[manifesto_id][article_date] = dict()
                        if article_category not in result[manifesto_id][article_date]:
                            result[manifesto_id][article_date][article_category] = dict()
                        result[manifesto_id][article_date][article_category][article_id] = get_cosine(manifesto_counter, Counter(article_data[data_io.DATA_FIELD]))
    if file_output is None:
        print(json.dumps(result, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(result, outfile)

'''
Calculate the similarity between manifestos and all other manifestos. The given file
containts all partys and their manifestos.
'''
def cosine_m2m_from_json(file_json, file_output=None):
    result = list()
    with open(file_json) as file_handel:
        dataset = list(json.load(file_handel).items())
        while dataset:
            doc_id_1, doc_data_1 = dataset.pop()
            for doc_id_2, doc_data_2 in dataset:
                result.append((doc_id_1, doc_id_2, get_cosine(Counter(doc_data_1), Counter(doc_data_2))))

        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'w') as outfile:
                json.dump(result, outfile)

def cosine_d2d_tfidf_from_json(file_json, file_output=None):
    result = list()
    with open(file_json) as file_handel:
        dataset = json.load(file_handel)
        while dataset:
            doc_id_1, doc_data_1 = dataset.pop()
            for doc_id_2, doc_data_2 in dataset:
                result.append((doc_id_1, doc_id_2, get_cosine(doc_data_1, doc_data_2)))

        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'w') as outfile:
                json.dump(result, outfile)

'''
Calculate similarity between manifestos and spiegel articles taken as input. For cosine the tf-idf is used
for vector representation.
'''
def cosine_m2s_tfidf_from_json(file_m_json, file_s_json, file_output=None, full_date=False):
    result = dict()
    with open(file_m_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
        with open(file_s_json) as fh_spiegel:
            stream_spiegel = json.load(fh_spiegel)
            for manifesto_id, manifesto_data in manifesto_dataset:
                for article_id, article_meta, article_data in stream_spiegel:
                    if full_date:
                        article_date = article_meta[data_io.DATE_FIELD]
                    else:
                        article_date = article_meta[data_io.DATE_FIELD][-4:]
                    article_category = article_meta[data_io.CATEGORY_FIELD]
                    if manifesto_id not in result:
                        result[manifesto_id] = dict()
                    if article_date not in result[manifesto_id]:
                        result[manifesto_id][article_date] = dict()
                    if article_category not in result[manifesto_id][article_date]:
                        result[manifesto_id][article_date][article_category] = dict()
                    result[manifesto_id][article_date][article_category][article_id] = get_cosine(manifesto_data, article_data)

        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'w') as outfile:
                json.dump(result, outfile)

def usage():
        print('This tool calculates Cosine similarity between Manifestos and Spiegel articles, Spiegel to Spiegel articles and Manifestos to Manifestos. It also has the capability to use tf-idf weights.')
        print('Usage for %s.' % sys.argv[0])
        print('%s [-h|--help] -m|--manifesto <path to manifesto bow> -s|--spiegel <path to spiegel bow> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-s | --spiegel: Path to Spiegel BOW in JSON format, created by create_bow.py.')
        print('\t-m | --manifesto: Path to Manifesto BOW in JSON format, created by create_bow.py.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')
        print('\t--tfidf: Determine whether the files defined with option -s and -m are tf-idf weighted files.')


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'o:s:m:h', ['manifesto=', 'spiegel=', 'help','output-file=', 'tfidf'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    spiegel = None
    manifesto = None
    is_tfidf = False
    output_file = None
    for option, argument in opts:
        if option in ('-h', '--help'):
            usage()
            sys.exit()
        elif option in ('-s', '--spiegel'):
            spiegel = argument
        elif option in ('-m', '--manifesto'):
            manifesto = argument
        elif option in ('-o', '--output-file'):
            output_file = argument
        elif option in ('--tfidf'):
            is_tfidf = True
        else:
            usage()
            sys.exit()

    if spiegel is None and manifesto is not None and not is_tfidf:
        cosine_m2m_from_json(manifesto, output_file)
    elif spiegel is None and manifesto is not None and is_tfidf:
        cosine_d2d_tfidf_from_json(manifesto, output_file)
    elif spiegel is not None and manifesto is not None and not is_tfidf:
        cosine_m2s_from_json(manifesto, spiegel, output_file)
    elif spiegel is not None and manifesto is not None and is_tfidf:
        cosine_m2s_tfidf_from_json(manifesto, spiegel, output_file)
    else:
        usage()