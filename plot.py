import matplotlib.pyplot as plt
import json

from collections import OrderedDict


import numpy as np
import scipy as sp
import scipy.stats
import cosine_sim as cosine
'''
Deprecated!
This file is an older version used for plotting the data based on matplot.
Plotting is done, manuall, via Microsoft Excel based on Values extracted from the Word similarity algorithms.
'''
color_dict = {
	'afd_2013.csv': 'cyan',
	'cdu_2002.csv': 'black',
	'cdu_2005.csv': 'black',
	'cdu_2009.csv': 'black',
	'cdu_2013.csv': 'black',
	'fdp_2002.csv': 'yellow',
	'fdp_2005.csv': 'yellow',
	'fdp_2009.csv': 'yellow',
	'fdp_2013.csv': 'yellow',
	'gruene_2002.csv': 'green',
	'gruene_2005.csv': 'green',
	'gruene_2009.csv': 'green',
	'gruene_2013.csv': 'green',
	'linke_2005.csv': 'pink',
	'linke_2009.csv': 'pink',
	'linke_2013.csv': 'pink',
	'pds_2002.csv': 'magenta',
	'piraten_2013.csv': 'orange',
	'spd_2002.csv': 'red',
	'spd_2005.csv': 'red',
	'spd_2009.csv': 'red',
	'spd_2013.csv': 'red'
}

color_dict_short = {
	'afd': 'cyan',
	'cdu': 'black',
	'fdp': 'yellow',
	'gru': 'green',
	'lin': 'pink',
	'pds': 'magenta',
	'pir': 'orange',
	'spd': 'red',
}

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h

def hot_categories():
    read_file(file_name)
    global date, category, manifesto_id, data
    final_dict = dict()
    for date, category, manifesto_id, data in sorted(data_list, key=lambda x: x[0]):
        if manifesto_id not in final_dict:
            final_dict[manifesto_id] = dict()
        if category not in final_dict[manifesto_id]:
            final_dict[manifesto_id][category] = list()
        final_dict[manifesto_id][category].append(data)
    data_list.clear()
    for id, data in final_dict.items():
        l = list()
        for k in sorted(data.keys()):
           # print((k, sum(final_dict[id][k]) / len(final_dict[id][k])))
            l.append((k, sum(final_dict[id][k]) / len(final_dict[id][k])))
        print(id)
        result = sorted(l, key=lambda x: x[1], reverse=True)[:3]
        print('\n'.join([str(elem) for elem in result]))


def hot_articles():
    read_file_arcticle(file_name)
    final_dict = dict()
    article_dict = dict()

    for date, category, manifesto_id, data, article_id in sorted(data_list,key=lambda x: x[0]):
        if manifesto_id not in final_dict:
            final_dict[manifesto_id] = list()

        final_dict[manifesto_id].append((data, article_id, category, date))

    for id, data in final_dict.items():
        sorted_final = sorted(final_dict[id], key=lambda x: x[0], reverse=True)[:2]
        result = list()
        for item in sorted_final:
            l = list(item)
            l[1] = get_spiegel_headline(l[1])
            l[0] = round(l[0], 4)
            result.append(l)
        #print(id[:-4] + " " + str(result))
        print(id[:-4])
        print('\n'.join([str(elem) for elem in result]))
       # print(id + " " + str(sorted(final_dict[id], key=lambda x: x[0], reverse=True)[:2]))

def hot_arcticles_over_years():
    read_file_hot_topics_over_years(file_name)
    final_dict = dict()
    for date, category, manifesto_id, data in sorted(data_list,key=lambda x: x[0]):
            if manifesto_id not in final_dict:
                final_dict[manifesto_id] = dict()
            if date not in final_dict[manifesto_id]:
                final_dict[manifesto_id][date] = list()
            final_dict[manifesto_id][date].append(data)

    plt.figure(figsize=(20, 10))
    x = np.array([2000,2001,2002,2003,2004,2005,2008,2009,2010,2011,2012, 2014])
    for k, v in final_dict.items():

        v2 = OrderedDict(sorted(v.items(), key=lambda x: x[0]))
        l = list()
        for blubb in v2.keys():
            res = sorted(final_dict[k][blubb], reverse=True)[:100]
            #print(res)
            l.append(sum(res) / len(res))
        plt.plot(x, np.array(l), label=k, c=color_dict_short[k])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('Similarity over years based on hot topics')
    plt.ylabel('manifesto to newspaper similarity')
    final_dict.clear()
    plt.savefig('data/results/hot_articles.png', bbox_inches = 'tight')

def similarity_over_years():
    read_file(file_name)
    global date, category, manifesto_id, data
    final_dict = dict()
    for date, category, manifesto_id, data in sorted(data_list, key=lambda x: x[0]):
        if manifesto_id not in final_dict:
            final_dict[manifesto_id] = dict()
        if date not in final_dict[manifesto_id]:
            final_dict[manifesto_id][date] = list()
        final_dict[manifesto_id][date].append(data)
    data_list.clear()

    plt.figure(figsize=(20, 10))
    x = np.array([2000,2001,2002,2003,2004,2005,2008,2009,2010,2011,2012, 2014])
    for k, v in final_dict.items():
        if k == "cdu":

            v2 = OrderedDict(sorted(v.items(), key=lambda x: x[0]))
            l = list()
            for blubb in v2.keys():
                l.append(sum(final_dict[k][blubb]) / len(final_dict[k][blubb]))
            plt.bar(x,np.array(l), label=k, color = color_dict_short[k])

    for k, v in final_dict.items():
        if k == "spd":

            v2 = OrderedDict(sorted(v.items(), key=lambda x: x[0]))
            l = list()
            for blubb in v2.keys():
                l.append(sum(final_dict[k][blubb]) / len(final_dict[k][blubb]))
            plt.bar(x, np.array(l), label=k, color=color_dict_short[k])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('Similarity over years')
    plt.ylabel('manifesto to newspaper similarity')
    final_dict.clear()
    plt.show()
   # plt.savefig('data/results/similarity_over_years.png', bbox_inches='tight')


def read_file(file_name):
    global data_list, data, manifesto_id, date, category
    data_list = list()
    with open(file_name) as data_file:
        data = json.load(data_file)
        for manifesto_id, manifesto_data in data.items():
            for date, categories in manifesto_data.items():
                for category, article in categories.items():
                    for article_id, article_data in article.items():
                        data_list.append((date, category, manifesto_id[:3], article_data))

def read_file_hot_topics_over_years(file_name):
    global data_list, data, manifesto_id, date, category
    data_list = list()
    with open(file_name) as data_file:
        data = json.load(data_file)
        for manifesto_id, manifesto_data in data.items():
            for date, categories in manifesto_data.items():
                for category, article in categories.items():
                    for article_id, article_data in article.items():
                        data_list.append((date, category, manifesto_id[:3], article_data))


def read_file_arcticle(file_name):
    global data_list, data, manifesto_id, date, category
    data_list = list()
    with open(file_name) as data_file:
        data = json.load(data_file)
        for manifesto_id, manifesto_data in data.items():
            for date, categories in manifesto_data.items():
                for category, article in categories.items():
                    for article_id, article_data in article.items():
                        data_list.append((date, category, manifesto_id, article_data, article_id))


file_name = 'data/results/result_cosine_all.json'
file_with_articles = 'data/all_spiegel_meta.json'

def get_spiegel_headline(article):
    #article = "PMGSPON-xPMG-SPOX-642457"
    headline = ""
    titel = ""
    with open(file_with_articles) as data_file:
        data = json.load(data_file)
        for manifesto_id, manifesto_data in data.items():
            headline = " "
            titel = " "
            if manifesto_id  == article:
                dic = OrderedDict()
                dic = manifesto_data.items()

                for items, key  in dic:
                   if(items == 'headline' ):
                       headline = key
                   if(items == 'titel'):
                        titel = key
                break
    return headline + ": " + titel

def manifesto_Similarity():
    final_dict = cosine.calc_manifesto_similarity()
    final_dict = OrderedDict(sorted(final_dict.items(), key=lambda x: x[0]))
    manifesto_base = 'cdu_2002.csv'
    plot_data = {}
    ctr = 0
    xticks = []
    manifesto_keys = []

    for k,v in sorted(final_dict[manifesto_base].items(), key=lambda x:x[0]):
        print(k)
        print(v)

        if k not in plot_data:
            plot_data[k] = {'manifestos': [], 'sims': []}


        plot_data[k]['manifestos'].append(ctr)
        plot_data[k]['sims'].append(v[0])

        print(manifesto_base + ' -> ' + k + ': ' + str(v[0]))
        manifesto_keys.append(ctr)
        xticks.append(k)
        ctr += 1
    plt.figure(figsize=(1,1))
    for manifesto_id, manifesto in plot_data.items():
        line = plt.bar(manifesto['manifestos'], manifesto['sims'], label=manifesto_id, color=color_dict[manifesto_id])

    plt.margins(0.03)
    plt.xticks(manifesto_keys, xticks, rotation='vertical')
    figure = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()



#hot_arcticles_over_years()
#hot_categories_over_years()
#hot_categories()
#hot_articles()
#hot_arcticles_over_years()
#similarity_over_years()
manifesto_Similarity()

