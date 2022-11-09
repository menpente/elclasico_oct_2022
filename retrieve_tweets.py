## Code snippet 1: retrieve tweets based on hashtag
#Import tweepy and pandas, pass on keys and create API object
import tweepy 
import pandas as pd
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

since_id = '1581525346972754000' #Setting since id parameter to extract tweets from El Clásico on
q = 'elclasico' #define query
rm_df = pd.DataFrame() #empty df to store results

#loop below retrieves tweets, parses json and saves to csv. Saving on each iteration to avoid data loss if something breaks.
for tweet in tweepy.Cursor(api.search_tweets, q=q, since_id=since_id, count=200).items():
    json_data = tweet._json
    df = pd.json_normalize(json_data)
    rm_df = rm_df.append(df)
    print (len(rm_df.index))# see df size to keep track of progress
    rm_df.to_csv('tweets_elclasico.csv', index=False, sep='\t')
