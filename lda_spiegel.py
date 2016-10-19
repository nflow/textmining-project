from gensim import corpora
import gensim
import time
import pyLDAvis
from pyLDAvis import gensim as gensimvis
from create_bow import create_clean_bow
from data_io import read_spiegel_data
import data_io

# configuration
num_topics = 250
progress = True
generate_html = True
years = [2000, 2001, 2002, 2003, 2004, 2005, 2008, 2009, 2010, 2011, 2012, 2014]
input_folder = 'data/spiegel/'
output_folder = 'lda/spiegel/'
LANG = 'german'

start = time.time()

for year in years:

    if progress:
        print('starting analysis for year ' + str(year))
    start_year = time.time()

    articles = read_spiegel_data(input_folder + 'SPOX-' + str(year) + '.xml', True)

    all_articles = []

    for key, article in articles.items():
        all_articles.append(create_clean_bow(article[data_io.DATA_FIELD]))

    dictionary = corpora.Dictionary(all_articles)

    # filtering
    no_below = 5
    no_above = 0.5
    dictionary.filter_extremes(no_below=no_below, no_above=no_above, keep_n=None)

    corpus = [dictionary.doc2bow(text) for text in all_articles]

    model = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=20)
    #model = gensim.models.ldamulticore.LdaMulticore(corpus, num_topics=100, workers=3, id2word=dictionary, passes=20)

    model.save(output_folder + str(year) + '_' + str(num_topics) + '.model')
    gensim.corpora.MmCorpus.serialize(output_folder + str(year) + '_' + str(num_topics) + '.corpus', corpus)
    dictionary.save(output_folder + str(year) + '_' + str(num_topics) + '.dictionary')

    if generate_html:
        visdata = gensimvis.prepare(model, corpus, dictionary, R=15)
        pyLDAvis.save_html(visdata, output_folder + str(year) + '_' + str(num_topics) + '.html')

    if progress:
        print('finished analysis for year ' + str(year) + ' in ' + str(time.time() - start_year) + 's')

print('analysis finished in ' + str(time.time() - start) + 's')
