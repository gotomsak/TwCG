import tweepy
import os
import json
from flask_bootstrap import Bootstrap
from flask import *
from dotenv import load_dotenv
from os.path import join, dirname
import csv
import re

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app=Flask(__name__)

#bootstrap=Bootstrap(app)
user_id = []
user = []
tweet_list = []
time = []
screen = []
tweet_data=[]
CONSUMER_KEY = os.environ.get('Ckey')
CONSUMER_SELECT = os.environ.get('Csecret')
ACCESS_TOKEN = os.environ.get('Akey')
ACCESS_SELECT = os.environ.get('Asecret')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SELECT)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SELECT)

api = tweepy.API(auth)

@app.route("/")
def index():

    message="キーワードを入力してくだしゃい"
    return render_template("index.html",message=message)


@app.route("/follow",methods=['POST'])
def follow():

    regex=r'RT @.*:'
    regex1=r'https://'
    regex2=r'http://'
    name=request.form['name']
    count=request.form['count']
    search_results=api.search(q=name,count=int(count))

    for result in search_results:

        user_id0 = result.id
        user_id.append(user_id0)
        user0=result.user.name
        user.append(user0)
        print(user_id0)
        screen0=result.user.screen_name
        screen.append(screen0)
        print(screen0)
        tweet0=result.text
        tweet_list.append(tweet0)
        print(tweet0)

        time0=result.created_at
        time.append(time0)
        tweet0=re.sub(regex1, '', tweet0)
        tweet0=re.sub(regex2, '', tweet0)
        matchOBJ=re.match(regex,tweet0)

        if matchOBJ:
            matchOBJ=matchOBJ.group()

            ms=matchOBJ[4:]
            ms1=ms[:-1]
            print(ms1)

        try:
            if matchOBJ:
                api.create_friendship(ms1)
            print(user0)
            api.create_friendship(screen0)
            print('フォローしました')
            api.create_favorite(user_id0)
            print('ライクしました')



        except:
            print('すでにしています')
        print('#################')

    return render_template('follow_result.html', user_id=user_id,user=user,tweet=tweet_list,time=time)






@app.route("/unfavorite",methods=['POST'])
def unfavorite():
    count=100
    cc=0
    delname=request.form['delname']
    #search_results=api.search(q=delname,count=count)
    search_results = api.favorites()
    for result in search_results:
        user_id0=result.id
        user_id.append(user_id0)
        user0=result.user.name

        try:
            print(user0)

            api.destroy_favorite(user_id0)
            cc=cc+1
        except:
            print("エラー")
        print(cc)
    return render_template('follow_result.html',user_id=user_id)





if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=8080)
    #app.run(debug=True)