#Code snippet 3: detecting topics
#Import pandas and transformers, define model
import pandas as pd
import tweetnlp
model = tweetnlp.load('topic_classification')	

#Load input data, select tweets column
df = pd.read_csv('tweets_elclasico.csv', sep='\t')
text = df.text
#Create empty lists for text and label
t = []
l = []

for text in text: #loop to process all tweets, picking label for strongest topic
  try:
    r = model.topic(text)['label'][0]
    t.append(text)
    l.append(r)
  except:
    pass
  

#Create empty data frame, convert lists to pandas series and add to df. Save to csv
s_df = pd.DataFrame()
t = pd.Series(t)
l = pd.Series(l)
s_df['text'] = t.values
s_df['label'] = l.values
s_df.to_csv('topic_labelling.csv', index=False, sep='\t')
