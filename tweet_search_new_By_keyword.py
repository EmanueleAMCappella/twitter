#struttra: ID / LANG / USER / TEXT / DATE
# -*- coding: utf-8 -*-
import oauth2
import twitter
import csv
from operator import itemgetter
import time

def search_tweets(tag, language_list, keyword_list):
    tweet_list = [[], [], [], [], [], [], []]
    try:
        tweet_list_f = open(percorso + tag + '_tweets.csv', "rb")
        tweet_list_r = csv.reader(tweet_list_f, delimiter = '\t')
        for tweet in tweet_list_r:
            tweet_list[0].append(tweet[0])
            tweet_list[1].append(tweet[1])
            tweet_list[2].append(tweet[2])
            tweet_list[3].append(tweet[3])
            tweet_list[4].append(tweet[4])
            tweet_list[5].append(tweet[5])
            tweet_list[6].append(tweet[6])
        tweet_list_f.close
    except: pass
    
    tweet_list_f = open(percorso + tag + '_tweets.csv', "wb")
    tweet_list_w = csv.writer(tweet_list_f, delimiter = '\t')
    i= 0
    n_query = 0
    for keyword in keyword_list:
        for language in language_list:
            search = api.GetSearch(term = keyword, lang = language, count = 100, result_type = 'recent')
            n_query = n_query + 1
            for result in search:
                try:
                    if (str(result.id) not in tweet_list[0]):
                        for char in result.text:
                            if (char == '\t'):
                                char = ' '
                        tweet_list[0].append(result.id)
                        tweet_list[1].append(result.user.lang)
                        tweet_list[2].append(result.user.screen_name.encode('ascii','replace'))
                        tweet_list[3].append(result.text.encode('ascii','replace'))
                        tweet_list[4].append(result.created_at)
                        tweet_list[5].append(result.user.followers_count)
                        tweet_list[6].append(keyword)
                        i= i+1
                        print str(result.id)+'  '+keyword.encode('ascii','replace')+'    '+ str(i)+'   '+result.created_at
                except: print 'ERROR ON RESULT #'+str(i)
            try:
                last_id = result.id
            except:
                print 'ERROR ON KEYWORD '+keyword+' WITH LANGUAGE '+language
                break
            time.sleep(5)
            for page in range(1,(n_results/100)/(len(keyword_list)*len(language_list))-len(keyword_list)*len(language_list)+1):
                print n_query
                search = api.GetSearch(term = keyword, lang = language, count = 100, result_type = 'recent', max_id = last_id-1)
                n_query = n_query + 1
                for result in search:
                    try:
                        if (str(result.id) not in tweet_list[0]):
                            for char in result.text:
                                if (char == '\t'):
                                    char = ' '    
                            tweet_list[0].append(result.id)
                            tweet_list[1].append(result.user.lang)
                            tweet_list[2].append(result.user.screen_name.encode('ascii','replace'))
                            tweet_list[3].append(result.text.encode('ascii','replace'))
                            tweet_list[4].append(result.created_at)
                            tweet_list[5].append(result.user.followers_count)
                            tweet_list[6].append(keyword)
                            i = i+1
                            print str(result.id)+'  '+keyword.encode('ascii','replace')+'    '+ str(i)+'   '+result.created_at
                            last_id = result.id
                    except: print 'ERROR ON RESULT #'+str(i)
                time.sleep(5)
                               
    for i in range(0, len(tweet_list[0])):
        tweet_list_w.writerow([tweet_list[0][i]] + [tweet_list[1][i]] + [tweet_list[2][i]]+[tweet_list[3][i]] + [tweet_list[4][i]] + [tweet_list[5][i]] + [tweet_list[6][i]])               
    tweet_list_f.close




#************* M A I N ****************************************************************

#formato percorso: 'C:/xxxxx/yyyyy/'
percorso = 'C:/Users/David/Dropbox/viralbeat/Melanoma/0 - Dati/Twitter/'

#il file avrà nome: tag_tweets.csv
tag = 'Melanoma'

#scegli se ricercare tutte le lingue inserendo ['all'] o delle specifiche lingue inserendo i relativi codici ISO (es. ['en', 'it', 'fr', 'de', 'es', 'ru']
language_list =['it']

#inserisci le keyword da ricercare (es. ['love', 'loving', '<3'])
keyword_list = ['#melanoma'] 

#inserisci il numero di tweet massimo desiderato; non è possibile recuperare tweet più vecchi di una settimana circa; la velocità di raccolta è 70k/h circa
n_results = 1000

api = twitter.Api(consumer_key='lwjmr20qkR0rxUsyEYIQ2w', consumer_secret='LWv0nkqLCoBCU1NqVksGm3aewIuSZSabIqkIvyXuwM', access_token_key='380829941-8yMP80wQznZwRvItrPlpRr6T00yhOXfPnXq937bW', access_token_secret='DbcK1m5ll5mjIEE2Ha1fFmXRBkU7L2g8c56tLoZbR9Q')

search_tweets(tag, language_list, keyword_list)
print 'end'

#_______________________________________________________________________________________




