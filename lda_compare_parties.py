import gensim
import matplotlib.pyplot as plt


manifestos = ['afd', 'cdu', 'fdp', 'gruene', 'linke', 'pds', 'piraten', 'spd']
color_dict_short = { 'afd': 'cyan', 'cdu': 'black', 'fdp': 'yellow', 'gruene': 'green', 'linke': 'pink', 'pds': 'magenta', 'piraten': 'orange', 'spd': 'red',}

folder = 'lda/manifesto/'

# compare this manifesto to all others
manifesto_base = 'spd'
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

    #print(manifesto_base + ' -> ' + manifesto + ': ' + str(sim))
    manifesto_keys.append(ctr)
    xticks.append(manifesto)
    ctr += 1


for manifesto_id, manifesto in plot_data.items():
    line = plt.bar(manifesto['manifestos'], manifesto['sims'], label=manifesto_id, color=color_dict_short[manifesto_id])

plt.margins(0.03)
plt.title('SPD similarity to other parties (all manifestos aggregated)')
plt.xticks(manifesto_keys, xticks, rotation='vertical')
figure = plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
plt.show()