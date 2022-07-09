import tweepy
import pandas as pd
from textblob import TextBlob
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

consumer_key = "consumer_key"
consumer_key_secret = "consumer_key_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)

posts=api.user_timeline(screen_name="CandiceAccola", count=100,lang="en",tweet_mode="extended")
i=1
for tweet in posts[0:5]:
  print(str(i)+'.'+' '+tweet.full_text + '\n')
  i=i+1
  
df=pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
def clean_text(text):
  text=re.sub(r'@[A-Za-z0-9]+',' ',text) #for removing '@' mentions
  text=re.sub(r'#','',text) #for removing the '#' symbol
  text=re.sub(r'http\S+',' ',text) #for removing URL's
  text=re.sub(r'\n','',text)

#removing emojis from text
re_emo=re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
text= re_emo.sub(r' ' , text)
return text
  
df['Tweets']=df['Tweets'].apply(clean_text)
df

allw=' '.join([t for t in df['Tweets']])
#for wordcloud
wc=WordCloud(width=2000,height=1500,random_state=15,max_font_size=300,background_color = '#89cdd3').generate(allw)
plt.imshow(wc)
plt.axis('off')

def subj(text):
  return TextBlob(text).sentiment.subjectivity
def polar(text):
  return TextBlob(text).sentiment.polarity
df['Subjectivity']=df['Tweets'].apply(subj)
df['Polarity']=df['Tweets'].apply(polar)
df.head()

def wordscore(score):
  if score<0:
   return 'Negative'
  elif score==0:
   return 'Neutral'
  else:
    return 'Positive'
df['Results']=df['Polarity'].apply(wordscore)
df

j=1
sorted=df.sort_values(by=['Polarity'])
for i in range(0,sorted.shape[0]):
  if(sorted['Results'][i]=='Positive'):
    print(str(j)+')'+sorted['Tweets'][i])
    print()
    j=j+1
    
j=1
sorted=df.sort_values(by=['Polarity'])
for i in range(0,sorted.shape[0]):
  if(sorted['Results'][i]=='Negative'):
    print(str(j)+')'+sorted['Tweets'][i])
    print()
    j=j+1
    
posit=df[df.Results=='Positive']
posit=posit['Tweets']
round((posit.shape[0]/df.shape[0])*100,1)

negit=df[df.Results=='Negative']
negit=negit['Tweets']
round((negit.shape[0]/df.shape[0])*100,1)

df['Results'].value_counts()
plt.title('Tweet Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')
df['Results'].value_counts().plot(kind='pie')
plt.show()
