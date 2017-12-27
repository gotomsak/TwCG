import tweepy
import os
from flask_bootstrap import Bootstrap
from flask import *



CONSUMER_KEY=os.environ.get('Ckey')
CONSUMER_SELECT=os.environ.get('Csecret')
ACCESS_TOKEN=os.environ.get('Akey')
ACCESS_SELECT=os.environ.get('Asecret')

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SELECT)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SELECT)

api=tweepy.API(auth)

app=Flask(__name__)

bootstrap=Bootstrap(app)




@app.route("/follow")
def follow():
    message="キーワードを入力してくだしゃい"
    return render_template("follow.html",message=message)


@app.route("/follow_result",methods=['POST'])
def follow_result():
    key=request.form['key']
    print(key)
    count=100
    searth_result=api.search(key,count=count)
    for result in searth_result:
        username=result.user.json['screen_name']
        user_id=result.user.name
        print(user_id)
        user=result.user.name
        print(user)
        tweet=result.text
        print(tweet)
        time=result.created_at
        print(time)
        try:
            api.create_favorite(user_id)
            print(user)
            print('ライクしました')
            api.create_friendship(user_id)
            print('フォローしました')
        except:
            print('すでにしています')
        print('#################')
        return render_template('follow_result.html', result=result)









if __name__ == "__main__":
    app.run(debug=True)
