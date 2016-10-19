from sys import stderr
from nltk.metrics.distance import jaccard_distance
import os
import multiprocessing
import json
import ijson
import data_io
from create_bow import create_clean_bow
import sys
import getopt

VERBOSE = True
OUTPUT_JSON = True
SKIP_BOW_CREATION = True

#used for printing output on the command line.
def printv(*args, **kwargs):
        if VERBOSE:
            print(*args, file=stderr, **kwargs)

# Calculate jaccard distance
def calc_jaccard(bow_set_a, bow_set_b):
    n = len(bow_set_a.intersection(bow_set_b))
    return n / float(len(bow_set_a) + len(bow_set_b) - n)
'''
Calculate jaccard similarity for newspaper articles and party manifestos.
'''
def jaccard_m2s_from_json(file_manifesto_json, file_spiegel_json, file_output=None):
    result = dict()
    manifesto_dataset = dict()
    result = dict()
    with open(file_manifesto_json) as fh_manifesto:
        manifesto_dataset = json.load(fh_manifesto)
    with open(file_spiegel_json) as fh_spiegel:
        stream_spiegel = ijson.items(fh_spiegel, 'item')
        for spiegel_part in stream_spiegel:
            for manifesto_id, manifesto_data in manifesto_dataset.items():
                spiegel_part_len = len(spiegel_part)
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
                        result[manifesto_id][article_date][article_category][article_id] = calc_jaccard(
                            set(manifesto_data), set(article_data[data_io.DATA_FIELD]))
    if file_output is None:
        print(json.dumps(result, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(result, outfile)

'''
Use this function to read XML and CSVs directly. It supports multithreading
to calculate the BOW faster. Can consume a lot of RAM. *DEPRECATED*
'''
result = dict()
def jaccard_m2s_direct(path_to_manifesto, path_to_spiegel, file_output=None):
    manifesto_bow_list = dict()
    result.clear()
    headers = ["article_date"]

    for filename_manifesto in os.listdir(path_to_manifesto):
        printv('Loading manifesto data and create clean BOW from ' + filename_manifesto)
        headers.append(filename_manifesto)
        manifesto_data = data_io.read_manifesto_data(path_to_manifesto + filename_manifesto)
        if SKIP_BOW_CREATION:
            manifesto_bow_list[filename_manifesto] = manifesto_data
        else:
            manifesto_bow_list[filename_manifesto] = create_clean_bow(manifesto_data)

    for filename_spiegel in os.listdir(path_to_spiegel):
        printv('Loading spiegel data from ' + filename_spiegel)
        spiegel_dict = data_io.read_spiegel_data(path_to_spiegel + filename_spiegel)
        p = multiprocessing.Pool(multiprocessing.cpu_count())
        for m_filename, m_bow in manifesto_bow_list.items():
            printv('Start to calculate distance to ...')
            for article in spiegel_dict.items():
                p.apply_async(calcualte, args=(article, m_bow), callback=calc_callback)
        p.close()
        p.join()


    printv('Print results ...')
    if file_output is None:
        print(json.dumps(result, indent=4))
    else:
        with open(file_output, 'w') as outfile:
            json.dump(result, outfile)

# deprecated
def calc_callback(process_result):
    if process_result is not None:
        id, distance = process_result
        if id not in result:
            result[id] = list()
        result[id].append(distance)
#deprecated
def calcualte(dict, manifesto_bow):
    article_id, article_dict = dict
    if data_io.DATA_FIELD in article_dict and len(article_dict[data_io.DATA_FIELD]) > 0:
        printv('\tProcessing ' + str(article_id) + ' with ' + str(len(article_dict[data_io.DATA_FIELD])) + ' words.')
        if SKIP_BOW_CREATION:
            distance = jaccard_distance(set(manifesto_bow), set(article_dict[data_io.DATA_FIELD]))
        else:
            article_bow = create_clean_bow(article_dict[data_io.DATA_FIELD])
            distance = jaccard_distance(set(manifesto_bow), set(article_bow))
        return (article_dict[data_io.DATE_FIELD] + '-' + article_id, distance)

def usage():
        print('This tool calculates Jaccard similarity between Manifestos and Spiegel articles.')
        print('Usage for %s.' % sys.argv[0])
        print('%s [-h|--help] -m|--manifesto <path to manifesto bow> -s|--spiegel <path to spiegel bow> -o|--output-file <path to output file>' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-s | --spiegel: Path to Spiegel BOW in JSON format, created by create_bow.py.')
        print('\t-m | --manifesto: Path to Manifesto BOW in JSON format, created by create_bow.py.')
        print('\t-o | --output-file: Path to the output JSON file. If no output file is defined the result is printed to STDOUT.')

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'o:s:m:h', ['manifesto=', 'spiegel=', 'help','output-file=', 'direct'])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    spiegel = None
    manifesto = None
    is_direct = False
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
        elif option in ('--direct'):
            is_direct = True
        else:
            usage()
            sys.exit()

    if spiegel is not None and manifesto is not None and not is_direct:
        jaccard_m2s_from_json(manifesto, spiegel, output_file)
    elif spiegel is not None and manifesto is not None and is_direct:
        jaccard_m2s_direct(manifesto, spiegel, output_file)
    else:
        usage()