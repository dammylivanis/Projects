import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import numpy
import pandas
import sys
class Tweet():
    def tweets1(self,tweetsno1):
        no1 = pandas.DataFrame(data=[tweet.text for tweet in accountno1tweets],columns=['Tweets'])
        no1['words'] = numpy.array([len(tweet.text.split()) for tweet in accountno1tweets])
        wordsno1 = 0
        for tweet in tweetsno1:
            wordsno1 += len(tweet.text.split())
        print(wordsno1)
        return no1
    def tweets2(self,tweetsno2):
        no2 = pandas.DataFrame(data=[tweet.text for tweet in accountno2tweets],columns=['Tweets'])
        no2['words'] = numpy.array([len(tweet.text.split()) for tweet in accountno2tweets])
        wordsno2 = 0
        for tweet in tweetsno2:
            wordsno2 += len(tweet.text.split())
        print(wordsno2)
        return no2

auth = tweepy.OAuthHandler('OhuFrECuKEhQzJ7cCSpmTVqJu','4LgeBJQTs06ImVGRMWXAeP91hYkW1yJtBOqk2oLvwusGHj0dgn')
auth.set_access_token('2370611869-eB3klCnE095nnZFZXHWTbiiHUGPziIufnTpNwX0', 'tcsLNOBQgz97J875qY9PbDMekbcqbhZWVEiXegnP7IsHK' )
API =tweepy.API(auth)

print("Provide the name of the first account:")
accountno1 = input()
print("Provide the name of the second account:")
accountno2 = input()
acc1 = API.get_user(accountno1)
acc2 = API.get_user(accountno2)
accountno1tweets = API.user_timeline(screen_name="%s" %accountno1,count=10)
accountno2tweets = API.user_timeline(screen_name="%s" %accountno2,count=10)
summary = Tweet()
no1 = summary.tweets1(accountno1tweets)
no2 = summary.tweets2(accountno2tweets)
print (no1.head(4))
print (no2.head(4))
followersaccountno1 = API.get_user(accountno1).followers_count
print("The account of" , accountno1,"has:")
print(followersaccountno1 , "followers")
followersaccountno2 = API.get_user(accountno2).followers_count
print("The account of" , accountno2 , "has:")
print(followersaccountno2,"followers")
productno1 = followersaccountno1 * accountno1tweets
productno2 = followersaccountno2 * accountno2tweets
#stuck in this step...  
if productno1 > productno2 :
    print("The biggest product of followers * Words belongs to :")
    print(accountno1)
elif productno2 > productno1 :
    print("The biggest product of followers * Words belongs to :")
    print(accountno2)
else :
    print("The product of followers * Words is the same to both accounts!")
