import gensim
import matplotlib.pyplot as plt


# compare this manifesto to all others
manifesto_base = 'cdu_2002.csv'
folder = 'lda/manifesto/'

manifestos = ['afd_2013.csv', 'cdu_2002.csv', 'cdu_2005.csv', 'cdu_2009.csv', 'cdu_2013.csv', 'fdp_2002.csv',
              'fdp_2005.csv', 'fdp_2009.csv', 'fdp_2013.csv', 'gruene_2002.csv', 'gruene_2005.csv', 'gruene_2009.csv',
              'gruene_2013.csv',
              'linke_2005.csv', 'linke_2009.csv', 'linke_2013.csv', 'pds_2002.csv', 'piraten_2013.csv', 'spd_2002.csv',
              'spd_2005.csv',
              'spd_2009.csv', 'spd_2013.csv']
color_dict = {'afd_2013.csv': 'cyan', 'cdu_2002.csv': 'black', 'cdu_2005.csv': 'black', 'cdu_2009.csv': 'black',
              'cdu_2013.csv': 'black', 'fdp_2002.csv': 'yellow', 'fdp_2005.csv': 'yellow', 'fdp_2009.csv': 'yellow',
              'fdp_2013.csv': 'yellow', 'gruene_2002.csv': 'green', 'gruene_2005.csv': 'green',
              'gruene_2009.csv': 'green', 'gruene_2013.csv': 'green', 'linke_2005.csv': 'pink',
              'linke_2009.csv': 'pink', 'linke_2013.csv': 'pink', 'pds_2002.csv': 'magenta',
              'piraten_2013.csv': 'orange', 'spd_2002.csv': 'red', 'spd_2005.csv': 'red', 'spd_2009.csv': 'red',
              'spd_2013.csv': 'red'}
color_dict_short = {'afd': 'cyan', 'cdu': 'black', 'fdp': 'yellow', 'gruene': 'green', 'linke': 'pink',
                    'pds': 'magenta', 'piraten': 'orange', 'spd': 'red', }

plot_data = {}

corpus_base = gensim.corpora.mmcorpus.MmCorpus(folder + manifesto_base + '.corpus')
vector_base = next(iter(corpus_base))
ctr = 0
xticks = []
manifesto_keys = []

for manifesto in manifestos:

    if manifesto == manifesto_base:
        continue

    if manifesto not in plot_data:
        plot_data[manifesto] = {'manifestos': [], 'sims': []}

    corpus_manifesto = gensim.corpora.mmcorpus.MmCorpus(folder + manifesto + '.corpus')
    vector_manifesto = next(iter(corpus_manifesto))
    sim = gensim.matutils.cossim(vector_base, vector_manifesto)

    plot_data[manifesto]['manifestos'].append(ctr)
    plot_data[manifesto]['sims'].append(sim)

    # print(manifesto_base + ' -> ' + manifesto + ': ' + str(sim))
    manifesto_keys.append(ctr)
    xticks.append(manifesto)
    ctr += 1

for manifesto_id, manifesto in plot_data.items():
    line = plt.bar(manifesto['manifestos'], manifesto['sims'], label=manifesto_id, color=color_dict[manifesto_id])

plt.margins(0.03)
plt.title(manifesto_base[:-4] + ' similarity with all other manifestos (LDA)')
plt.xticks(manifesto_keys, xticks, rotation='vertical')
figure = plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()
