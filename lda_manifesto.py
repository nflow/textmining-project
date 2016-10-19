import gensim
import nltk
import pyLDAvis
import time
from pyLDAvis import gensim as gensimvis
from create_bow import create_clean_bow
from data_io import read_manifesto_data

#
# This script can be used to prepare and process manifestos (located in 'folder' variable) to generate LDA .corpus, .model
# and .dictionary files. Additionally A html file is generated that can be used to explore the topics of the manifesto.
# All generated files are stored in a folder that can be specified in 'output_folder'.
#

# configuration
num_topics = 10
progress = True
generate_html = True
folder = 'data/manifestos/'
output_folder = 'lda/manifesto/'
LANG = 'german'
manifestos = ['afd_2013.csv', 'cdu_2002.csv', 'cdu_2005.csv', 'cdu_2009.csv', 'cdu_2013.csv', 'fdp_2002.csv',
              'fdp_2005.csv', 'fdp_2009.csv', 'fdp_2013.csv', 'gruene_2002.csv', 'gruene_2005.csv', 'gruene_2009.csv', 'gruene_2013.csv',
              'linke_2005.csv', 'linke_2009.csv', 'linke_2013.csv', 'pds_2002.csv', 'piraten_2013.csv', 'spd_2002.csv', 'spd_2005.csv',
              'spd_2009.csv', 'spd_2013.csv']

for manifesto in manifestos:
    checkpoint = time.time()
    if progress:
        print('starting analysis for manifesto ' + manifesto)
    manifesto_content = read_manifesto_data(folder + manifesto, as_word_list=False)

    all_sentences = []

    # additional stop words
    stop_words = ['mus', 'das', 'un', 'braucht', 'mehr', 'dafur', 'ab', 'soll', 'be']

    for sentence in manifesto_content:
        sentence_tokens = nltk.tokenize.word_tokenize(sentence, language=LANG)
        sentence_bow = create_clean_bow(sentence_tokens)
        sentence_bow = [x for x in sentence_bow if x not in stop_words]
        all_sentences.append(sentence_bow)

    dictionary = gensim.corpora.Dictionary(all_sentences)
    corpus = [dictionary.doc2bow(text) for text in all_sentences]
    model = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=20)
    # uncomment for multithreaded
    #model = gensim.models.ldamulticore.LdaMulticore(corpus, num_topics=num_topics, id2word=dictionary, passes=20, workers=3)

    model.save(output_folder + manifesto + '_' + str(num_topics) + '.model')
    gensim.corpora.MmCorpus.serialize(output_folder + manifesto + '_' + str(num_topics) + '.corpus', corpus)
    dictionary.save(output_folder + manifesto + '_' + str(num_topics) + '.dictionary')

    if generate_html:
        visdata = gensimvis.prepare(model, corpus, dictionary, R=15)
        pyLDAvis.save_html(visdata, output_folder + manifesto + '_' + str(num_topics) + '.html')

    if progress:
        print('generated html for ' + manifesto + ' in ' + str(time.time() - checkpoint) + 's')
