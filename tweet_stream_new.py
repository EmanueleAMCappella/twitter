# -*- coding: cp1252 -*-
import tweepy
import json
import csv
import time
import twitter

consumer_key = 'lwjmr20qkR0rxUsyEYIQ2w'
consumer_secret = 'LWv0nkqLCoBCU1NqVksGm3aewIuSZSabIqkIvyXuwM'

access_token_key = '380829941-8yMP80wQznZwRvItrPlpRr6T00yhOXfPnXq937bW'
access_token_secret = 'DbcK1m5ll5mjIEE2Ha1fFmXRBkU7L2g8c56tLoZbR9Q'


auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth1.set_access_token(access_token_key, access_token_secret)


class StreamListener(tweepy.StreamListener):
    def on_status(self, tweet):
        pass

    def on_error(self, status_code):
        print 'Error: ' + repr(status_code)
        return False

    def on_data(self, data):
        json_data = json.loads(data)
        try:
            if (json_data["user"]["lang"] in languages) or (languages[0] == 'all'):
                try: tweet_id = str(json_data["id"]).encode('ascii','replace')
                except: tweet_id = 'null'
                try: user_name = json_data["user"]["screen_name"].encode('ascii','replace')
                except: user_name = 'null'
                try: tweet_text = json_data["text"].encode('ascii','replace')
                except: tweet_text = 'null'
                try: tweet_datetime= json_data["created_at"].encode('ascii','replace')
                except: tweet_datetime = 'null'
                try: user_nfollowers = json_data["user"]["followers_count"]
                except: user_nfollowers = 'null'
                tweets_w.writerow([tweet_id]+[user_name]+[tweet_text]+[tweet_datetime]+[user_nfollowers])
                print 'tweet'
        except: pass



############ M A I N #################################################################################


percorso = 'C:/Documents and Settings/Davide/Desktop/Communities/'
tag = 'communities'

languages = ['it']

#inserisci le parole da ricerca NEL TESTO del tweet (anche @mention)
keywords = ['@CocaCola', 'coca-cola']


#inserisci i nomi utenti di cui seguire i tweet (senza @)
users = ['CocaCola']


#________________________________________________________________________________________________


usrIDs = []
api = tweepy.API(auth1)
for usr in users:
    try:
        usrIDs.append(api.get_user(usr).id)
    except: print usr+' not recognized'
l = StreamListener()
streamer = tweepy.Stream(auth=auth1, listener=l)
tweets_f = open(percorso+tag+'_tweets2.csv',"wb")
tweets_w = csv.writer(tweets_f, delimiter = '\t')
i = 0
start_time = time.time()
streamer.filter(track = keywords, follow = usrIDs)
usrIDs
