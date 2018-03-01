# -*- coding: cp1252 -*-
import csv
import math
import twitter


class search:
    
    api =''
    file_pathname = ''
    tweets_IDs = []
    tweets_w = ''
    n_results = 1000

    def __init__(self, file_path, file_tag, n_results):
        self.api = twitter.Api(consumer_key='lwjmr20qkR0rxUsyEYIQ2w', consumer_secret='LWv0nkqLCoBCU1NqVksGm3aewIuSZSabIqkIvyXuwM', access_token_key='380829941-8yMP80wQznZwRvItrPlpRr6T00yhOXfPnXq937bW', access_token_secret='DbcK1m5ll5mjIEE2Ha1fFmXRBkU7L2g8c56tLoZbR9Q')
        self.file_pathname = file_path+file_tag+'_tweets.csv'
        self.n_results = n_results
        self.init_files()
        self.init_search()

    def init_files(self):
        try:
            tweets_f = open(self.file_pathname, "rb")
            tweets_r = csv.reader(tweets_f, delimiter = '\t')
            self.tweets_IDs = load_tweets_IDs(tweets_r)
        except: pass 
        tweets_f = open(self.file_pathname, "a+")
        self.tweets_w = csv.writer(tweets_f, delimiter = '\t')

    def load_list(tweets_r):
        for tweet in tweets_r:
            tweets_IDs.append(tweet[0])
        return tweets_IDs
    
    
class search_users(search):

    def __init__(self, file_path, file_tag, users, n_results):
        self.users = users
        search.__init__(self, file_path, file_tag, n_results)      
        
    def init_search(self):
        for user in self.users:
            try: self.launch_search(user)
            except: print 'ERROR WHEN LAUNCHING THE SEARCH FOR USER  '+user

    def launch_search(self, user):
        results = self.api.GetUserTimeline(screen_name = user, count = self.n_results)
        i = 0
        for result in results:
            self.save_tweets(result)
            i = i + 1
            print "TWEET OF USER  "+user+'  NUMBER '+str(i)
        if len(results) == 0: print 'NO RESULTS FOR USER  '+user+'. CHECK IF THE USER EXISTS!'

    def save_tweets(self, result):
        try: tweet_id = result.id
        except: tweet_id = 'null'
        try: user_language = result.user.lang
        except: user_language = 'null'
        try: user_name = result.user.screen_name.encode('ascii','replace')
        except: user_name = 'null'
        try: tweet_text = result.text.encode('ascii','replace')
        except:tweet_text = 'null'
        try: tweet_datetime = result.created_at
        except: tweet_datetime = 'null'
        try: user_Nfollowers = result.user.followers_count
        except: user_Nfollowers = 'null'
        self.tweets_w.writerow([tweet_id]+[user_language]+[user_name]+[tweet_text]+[tweet_datetime]+[user_Nfollowers])
            
    
    
#inserisci il percorso (es. percorso = 'c:/prova/'
percorso = 'C:/Users/David/Desktop/T-Lab Course/'

#inserisci la tag (es. tag = 'prova' --> il file si chiamerà prova_tweets.csv)
tag = 'Papa'

#inserisci l'elenco di utenti (es. users = ['david_berra','maxairc'] senza @!)
users = ['Pontifex_it']

#inserisci il numero massimo di risultati per utente (max 200 circa, non va indietro nel tempo indefinitamente, comunque anche di mesi)
n_results = 5000

search_users(percorso, tag, users, n_results)


                     
        
        
