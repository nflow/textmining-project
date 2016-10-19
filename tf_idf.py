from sys import stderr
import json
import math
import ijson
from collections import Counter
import data_io
import sys
import getopt

VERBOSE = True
ALL_KEY = 'sum_of_token'
DOC_NUM_KEY = 'document_count'

def printv(*args, **kwargs):
    if VERBOSE:
        print(*args, file=stderr, **kwargs)


def idf(bow_list):
    idf = dict()
    combined_bow = set([term for bow in bow_list for term in bow])
    for term in combined_bow:
        contained = map(lambda bow: term in bow, bow_list)
        idf[term] = 1 + math.log(len(bow_list)/(sum(contained)))
    return idf

def tf(term, bow):
    return 1 + math.log(bow.count(term))

def tf_length_normalized(term, bow, weight = 0.4):
    c = Counter(bow)
    return weight + (1.0-weight) * c[term] / c.most_common(1)[0][1]

def tfidf(term, tf, idf):
    if term in idf:
        return tf * idf[term]
    else:
        printv('No IDF for ' + term)
        return 0.0


'''
Use this function to extract the mapping from a token to a file out of a prepared JSON.
'''
def all_token_contained(file_manifesto_json, file_spiegel_json, file_output=None):
    number_of_documents = 0
    result = dict()
    with open(file_spiegel_json) as fh_spiegel:
        stream_spiegel = ijson.items(fh_spiegel, 'item')
        for spiegel_part in stream_spiegel:
            for article_id, article_data in spiegel_part.items():
                if len(article_data[data_io.DATA_FIELD]) > 0:
                    number_of_documents += 1
                    for token in set(article_data[data_io.DATA_FIELD]):
                        if token not in result:
                            result[token] = 1
                        else:
                            result[token] += 1

    with open(file_manifesto_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
        for manifesto_id, manifesto_data in manifesto_dataset.items():
            number_of_documents += 1
            for token in set(manifesto_data):
                if token not in result:
                    result[token] = 1
                else:
                    result[token] += 1

    if file_output is None:
        print(json.dumps([number_of_documents, result], indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump([number_of_documents, result], outfile)

def manifesto_token_contained(file_manifesto_json, file_output=None):
    number_of_documents = 0
    result = dict()
    with open(file_manifesto_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
        for manifesto_id, manifesto_data in manifesto_dataset.items():
            number_of_documents += 1
            for token in set(manifesto_data):
                if token not in result:
                    result[token] = 1
                else:
                    result[token] += 1

    if file_output is None:
        print(json.dumps([number_of_documents, result], indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump([number_of_documents, result], outfile)


'''
Calculates the TF for a given dataset. The output can get pretty big.
'''
def tf_spiegel_from_json(file_spiegel_json, file_output=None):
    result = list()
    with open(file_spiegel_json) as fh_spiegel:
        stream_spiegel = ijson.items(fh_spiegel, 'item')
        for spiegel_part in stream_spiegel:
            for article_id, article_data in spiegel_part.items():
                document = (article_id, dict(), dict())
                if data_io.DATE_FIELD in article_data:
                    document[1][data_io.DATE_FIELD] = article_data[data_io.DATE_FIELD]
                if data_io.HEADLINE_FIELD in article_data:
                    document[1][data_io.HEADLINE_FIELD] = article_data[data_io.HEADLINE_FIELD]
                if data_io.CATEGORY_FIELD in article_data:
                    document[1][data_io.CATEGORY_FIELD] = article_data[data_io.CATEGORY_FIELD]
                if data_io.TITLE_FIELD in article_data:
                    document[1][data_io.TITLE_FIELD] = article_data[data_io.TITLE_FIELD]
                if len(article_data[data_io.DATA_FIELD]) > 0:
                    for token in article_data[data_io.DATA_FIELD]:
                        if token not in document[2]:
                            document[2][token] = 1
                        else:
                            document[2][token] += 1
                result.append(document)
    if file_output is None:
        print(json.dumps(result, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(result, outfile)

def tf_manifesto_from_json(file_manifesto_json, file_output=None):
    result = list()
    with open(file_manifesto_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
        for manifesto_id, manifesto_data in manifesto_dataset.items():
            document = (manifesto_id, dict())
            for token in manifesto_data:
                if token not in document[1]:
                    document[1][token] = 1
                else:
                    document[1][token] += 1
            result.append(document)
    if file_output is None:
        print(json.dumps(result, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(result, outfile)

'''
Use the following function to calculate the IDF from a precalculated JSON dataset.
'''
def idf_from_json(file_token_mapping_json, file_output=None):
    result = dict()
    with open(file_token_mapping_json) as file_handel:
        mapping_dataset = json.load(file_handel)

        document_amount, all_token_dict = mapping_dataset

        for token, amount in all_token_dict.items():
            result[token] = 1 + math.log(document_amount/amount)

        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'w') as outfile:
                json.dump(result, outfile)

'''

'''
def tfidf_manifesto_from_json(file_idf_json, file_tf_json, file_output=None):
    result = []
    with open(file_idf_json) as idf_file_handel:
        idf = json.load(idf_file_handel)
        with open(file_tf_json) as tf_file_handel:
            tf = ijson.items(tf_file_handel, 'item')
            for id, tokens in tf:
                result_tmp = dict()
                for token, token_count in tokens.items():
                    tf = 1 + math.log(token_count)
                    result_tmp[token] = tf * idf[token]
                result.append([id,result_tmp])

        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'w') as outfile:
                json.dump(result, outfile)

def tfidf_spiegel_from_json(file_idf_json, file_tf_json, file_output=None):
    result = []
    first_comma = True
    if file_output is not None:
        with open(file_output, 'w') as outfile:
            outfile.write('[')
    with open(file_idf_json) as idf_file_handel:
        idf = json.load(idf_file_handel)
        with open(file_tf_json) as tf_file_handel:
            tf = ijson.items(tf_file_handel, 'item')
            for id, meta, tokens in tf:
                result_tmp = dict()
                for token, token_count in tokens.items():
                    tf = 1 + math.log(token_count)
                    result_tmp[token] = tf * idf[token]
                if file_output is None:
                    result.append([id, meta, result_tmp])
                else:
                    with open(file_output, 'a') as outfile:
                        if not first_comma:
                            outfile.write(',')
                        first_comma = False
                        json.dump([id, meta, result_tmp], outfile)


        if file_output is None:
            print(json.dumps(result, indent=4))
        else:
            with open(file_output, 'a') as outfile:
                outfile.write(']')

def usage(id=0):
    if id==0:
        print('This tool creates all necessary parts used to calculate the tf-idf weight.')
        print('Usage for %s.' % sys.argv[0])
        print('\t%s tf: Compute the term frequency used in tfidf.' % sys.argv[0])
        print('\t%s token-mapping: Compute the token mapping used for the inverse document frequency.' % sys.argv[0])
        print('\t%s idf: Compute the inverse term frequency.' % sys.argv[0])
        print('\t%s tfidf: Compute tf-idf weights.' % sys.argv[0])
    elif id==1:
        print('Usage for %s tf.' % sys.argv[0])
        print('%s tf [-h|--help] -m|--manifesto <path to manifesto bow> -s|--spiegel <path to spiegel bow> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-s | --spiegel: Path to Spiegel BOW in JSON format, created by create_bow.py.')
        print('\t-m | --manifesto: Path to Manifesto BOW in JSON format, created by create_bow.py.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')
    elif id==2:
        print('Usage for %s token-mapping.' % sys.argv[0])
        print('%s token-mapping [-h|--help] -m|--manifesto <path to manifesto bow> -s|--spiegel <path to spiegel bow> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-s | --spiegel: Path to Spiegel BOW in JSON format, created by create_bow.py. Do not use manifesto if -s is set.')
        print('\t-m | --manifesto: Path to Manifesto BOW in JSON format, created by create_bow.py. Do not use manifesto if -m is set.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')
    elif id==3:
        print('Usage for %s idf.' % sys.argv[0])
        print('%s idf [-h|--help] -i|--token-mapping <path to token mapping file> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-i | --token-mapping: Path to token mapping file created by tfidf.py token-mapping.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')
    elif id==4:
        print('Usage for %s tfidf.' % sys.argv[0])
        print('%s tfidf [-h|--help] --tf-manifesto=<path to tf file for manifestos> --tf-manifesto=<path to tf file for spiegel articles> --idf=<path to idf file> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t--tf-manifesto: Path to file containing the term frequency for Manifestos created by tf_idf.py tf.')
        print('\t--tf-spiegel: Path to file containing the term frequency for Spiegel articles created by tf_idf.py tf.')
        print('\t--idf: Path to file containing the inverse term frequency over all Spiegel articles and Manifestos created by tf_idf idf.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if (sys.argv[1] == 'idf'):
            try:
                opts, args = getopt.getopt(sys.argv[2:], 'o:i::h', ['token-mapping=', 'help','output-file='])
            except getopt.GetoptError as err:
                print(str(err))
                usage(3)
                sys.exit(2)

            input = None
            output_file = None
            for option, argument in opts:
                if option in ('-h', '--help'):
                    usage(3)
                    sys.exit()
                elif option in ('-i', '--token-mapping'):
                    input = argument
                elif option in ('-o', '--output-file'):
                    output_file = argument
                else:
                    usage(3)
                    sys.exit()
            if input is not None:
                idf_from_json(input, output_file)
            else:
                usage(3)
        elif (sys.argv[1] == 'tf'):
            try:
                opts, args = getopt.getopt(sys.argv[2:], 'o:s:m:h', ['spiegel=', 'manifesto=', 'help','output-file='])
            except getopt.GetoptError as err:
                print(str(err))
                usage(0)
                sys.exit(2)

            spiegel = None
            manifesto = None
            output_file = None
            for option, argument in opts:
                if option in ('-h', '--help'):
                    usage(1)
                    sys.exit()
                elif option in ('-s', '--spiegel'):
                    spiegel = argument
                elif option in ('-m', '--manifesto'):
                    manifesto = argument
                elif option in ('-o', '--output-file'):
                    output_file = argument
                else:
                    usage(1)
                    sys.exit()
            if spiegel is not None:
                tf_spiegel_from_json(spiegel, output_file)
            elif manifesto is not None:
                tf_manifesto_from_json(manifesto, output_file)
            else:
                usage(1)
        elif (sys.argv[1] == 'token-mapping'):
            try:
                opts, args = getopt.getopt(sys.argv[2:], 'o:s:m:h', ['spiegel=', 'manifesto=', 'help','output-file='])
            except getopt.GetoptError as err:
                print(str(err))
                usage()
                sys.exit(2)

            spiegel = None
            manifesto = None
            output_file = None
            for option, argument in opts:
                if option in ('-h', '--help'):
                    usage(2)
                    sys.exit()
                elif option in ('-s', '--spiegel'):
                    spiegel = argument
                elif option in ('-m', '--manifesto'):
                    manifesto = argument
                elif option in ('-o', '--output-file'):
                    output_file = argument
                else:
                    usage(2)
                    sys.exit()
            if spiegel is not None and manifesto is not None:
                all_token_contained(manifesto, spiegel, output_file)
            elif manifesto is not None:
                manifesto_token_contained(manifesto, output_file)
            else:
                usage(2)
        elif (sys.argv[1] == 'tfidf'):
            try:
                opts, args = getopt.getopt(sys.argv[2:], 's:m:o:h', ['tf-manifesto=', 'tf-spiegel=', 'idf=', 'help','output-file='])
            except getopt.GetoptError as err:
                print(str(err))
                usage()
                sys.exit(2)

            tf_manifesto = None
            tf_spiegel = None
            idf = None
            output_file = None
            for option, argument in opts:
                if option in ('-h', '--help'):
                    usage(4)
                    sys.exit()
                elif option in ('--tf-manifesto='):
                    tf_manifesto = argument
                elif option in ('--tf-spiegel='):
                    tf_spiegel = argument
                elif option in ('--idf'):
                    idf = argument
                elif option in ('-o', '--output-file'):
                    output_file = argument
                else:
                    usage(4)
                    sys.exit()
            if tf_spiegel is not None and idf is not None:
                tfidf_spiegel_from_json(idf, tf_spiegel, output_file)
            elif tf_manifesto is not None and idf is not None:
                tfidf_manifesto_from_json(idf, tf_manifesto, output_file)
            else:
                usage(4)
        else:
            usage()
            sys.exit(3)
    else:
        usage()