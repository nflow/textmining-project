import gensim
import pyLDAvis
import time
from pyLDAvis import gensim as gensimvis

#
# This script can be used to generate a html file of pyLDAvis to explore topics of an LDA model.
#

folder = 'lda/manifesto/'
# this has been added in previous steps (basically the number of topics)
postfix = '_100'
manifestos = ['cdu_2002.csv', 'cdu_2005.csv', 'cdu_2009.csv', 'cdu_2013.csv', 'fdp_2002.csv',
              'fdp_2005.csv', 'fdp_2009.csv', 'fdp_2013.csv', 'gruene_2002.csv', 'gruene_2005.csv', 'gruene_2009.csv', 'gruene_2013.csv',
              'linke_2005.csv', 'linke_2009.csv', 'linke_2013.csv', 'pds_2002.csv', 'piraten_2013.csv', 'spd_2002.csv', 'spd_2005.csv',
              'spd_2009.csv', 'spd_2013.csv']

start = time.time()

for file in manifestos:
    checkpoint = time.time()
    print('starting analysis for file ' + file)
    model = gensim.models.ldamodel.LdaModel.load(folder + file + postfix + '.model')
    corpus = gensim.corpora.mmcorpus.MmCorpus(folder + file + postfix + '.corpus')
    dictionary = gensim.corpora.dictionary.Dictionary.load(folder + file + postfix + '.dictionary', )

    visdata = gensimvis.prepare(model, corpus, dictionary, R=15)
    pyLDAvis.save_html(visdata, folder + file + postfix + '.html')
    print('generated html for ' + file + ' in ' + str(time.time() - checkpoint) + 's')

print('generating html for all files took ' + str(time.time() - start) + 's')
