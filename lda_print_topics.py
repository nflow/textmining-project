from gensim import models

folder = 'lda/spiegel/'
model_file = '2000'
num_topics = 3
num_words = 4
model = models.ldamodel.LdaModel.load(folder + model_file + '.model', mmap='r')

print(model.print_topics(num_topics=num_topics, num_words=num_words))
