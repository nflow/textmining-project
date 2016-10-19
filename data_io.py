import sys
import os
import getopt
import csv
import re
from nltk import tokenize
from lxml import etree
import json
import ijson
import html

DELIMITER = ','
LANG = 'german'
CSV_DATA_COL = 0
XML_DATA_ELEMENT = './artikel/inhalt'

DATA_FIELD = 'data'
DATE_FIELD = 'date'
AUTHOR_FIELD = 'author'
TITLE_FIELD = 'titel'
CATEGORY_FIELD = 'category'
HEADLINE_FIELD = 'headline'

manifesto_data_fields = {DATE_FIELD: './metadaten/quelle/datum',
                         AUTHOR_FIELD: './autor/autor-name',
                         TITLE_FIELD: './inhalt/titel-liste/titel',
                         CATEGORY_FIELD: './inhalt/titel-liste/rubrik',
                         HEADLINE_FIELD: './inhalt/titel-liste/dachzeile'}

# I/O stuff.
def read_manifesto_data(file_name, as_word_list=True):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        compact_string = str()
        with open(file_name, 'rt', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=DELIMITER)
            for row in reader:
                compact_string = compact_string + ' ' + row[CSV_DATA_COL]

        if as_word_list:
            return tokenize.word_tokenize(compact_string, language=LANG)
        else:
            return tokenize.sent_tokenize(compact_string, language=LANG)
    else:
        print(file_name + ' file not found.')

def read_spiegel_data(file_name, as_word_list=True):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        re_newline = re.compile('\\n')
        re_multispace = re.compile('[ ]+')
        output = dict()
        p = etree.XMLParser(load_dtd= True, remove_blank_text=True, resolve_entities=False, recover=True)
        root = etree.parse(file_name, p).getroot()
        for article in root:
            article_id = article.find('./metadaten/artikel-id')
            output[article_id.text] = dict()

            # Extract useful meta data and other informations
            for k, v in manifesto_data_fields.items():
                element = article.find(v)
                if element is not None:
                    output[article_id.text][k] = element.text

            content_element = article.find('inhalt')
            if content_element is not None:
                output_text = str()
                for content in  content_element.find('text'):
                    for text in content.itertext():
                        # Double unescape due to following parts in the text.
                        # Original: 'Der Lyriker <b>Michael Lentz</b> (&amp;quot;Aller Ding&amp;quot;)'
                        # #1 Unesc: 'Der Lyriker <b>Michael Lentz</b> (&quot;Aller Ding&quot;)'
                        # #2 Unesc: 'Der Lyriker <b>Michael Lentz</b> ("Aller Ding")'
                        output_text += html.unescape(html.unescape(text))
                if as_word_list:
                    output[article_id.text][DATA_FIELD] = tokenize.word_tokenize(output_text, language=LANG)
                else:
                    clean_sent_list = list()
                    for sent in tokenize.sent_tokenize(output_text, language=LANG):
                        clean_sent_list.append(re_multispace.sub(' ', re_newline.sub('', sent)).strip())
                    output[article_id.text][DATA_FIELD] = clean_sent_list
        return output
    else:
        print(file_name + ' file not found.')

def extract_spiegel_meta_from_json(json_file, file_output=None):
	result = dict()
	with open(json_file, 'rb') as file:
		data = ijson.items(file,'item')
		for corpa in data:
			for article_id, article_data in corpa.items():
				if article_id in result:
					print("WTF! Id not unique! " + article_id)
				result[article_id] = dict()
				if DATE_FIELD in article_data:
					result[article_id][DATE_FIELD] = article_data[DATE_FIELD]
				if AUTHOR_FIELD in article_data:
					result[article_id][AUTHOR_FIELD] = article_data[AUTHOR_FIELD]
				if TITLE_FIELD in article_data:
					result[article_id][TITLE_FIELD] = article_data[TITLE_FIELD]
				if CATEGORY_FIELD in article_data:
					result[article_id][CATEGORY_FIELD] = article_data[CATEGORY_FIELD]
				if HEADLINE_FIELD in article_data:
					result[article_id][HEADLINE_FIELD] = article_data[HEADLINE_FIELD]
	if file_output is None:
		print(json.dumps(result, indent=4))
	else:
		with open(file_output, 'w') as outfile:
			json.dump(result, outfile)
# Console stuff.

'''
    Prints how to use this application.
'''
def usage():
        print('This tool converts raw Manifestos and Spiegel articles into a, easier to compute, JSON format.')
        print('Usage for %s.' % sys.argv[0])
        print('%s [-h|--help] -m|--manifesto <path to manifesto (csv)> -s|--spiegel <path to corpus(xml)>'
              ' [--as-word-list]' % sys.argv[0])
        print('Options:')
        print('\t-h | --help: Prints the help.')
        print('\t-m | --manifesto: Path where the manifesto is located. The file format has to be CSV.'
              ' Option can be used multiple times.')
        print('\t-s | --spiegel: Path where the spiegel corpa is located. The file format has to be XML. '
              'Option can be used multiple times.')
        print('\t--as-word-list: Returns words instead of sentences.')

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:m:h', ['manifesto=', 'spiegel=', 'help',
                                                           'as-word-list', 'output-file-spiegel=', 'output-file-manifesto='])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    spiegel_list = list()
    manifesto_list = list()
    as_word_list = False
    output_file_spiegel = None
    output_file_manifesto = None
    for option, argument in opts:
        if option in ('-h', '--help'):
            usage()
            sys.exit()
        elif option in ('-s', '--spiegel'):
            spiegel_list.append(argument)
        elif option in ('-m', '--manifesto'):
            manifesto_list.append(argument)
        elif option in ('--as-word-list'):
            as_word_list =  True
        elif option in ('--output-file-spiegel'):
            output_file_spiegel = argument
        elif option in ('--output-file-manifesto'):
            output_file_manifesto = argument
        else:
            usage()
            sys.exit()

    result = list()
    for s in spiegel_list:
        print("Processing " + s)
        res = read_spiegel_data(s, as_word_list)
        if res is not None:
            result.append(res)
    if len(spiegel_list) > 0:
        if output_file_spiegel is None:
            print(json.dumps(result, indent=4))
        else:
            with open(output_file_spiegel, 'w') as outfile:
                json.dump(result, outfile, indent=4)

    result.clear()
    for m in manifesto_list:
        print("Processing " + m)
        res = read_manifesto_data(m, as_word_list)
        if res is not None:
            result.append(res)
    if len(manifesto_list) > 0:
        if output_file_manifesto is None:
            print(json.dumps(result, indent=4))
        else:
            with open(output_file_manifesto, 'w') as outfile:
                json.dump(result, outfile, indent=4)