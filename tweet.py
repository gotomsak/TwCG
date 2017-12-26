import os
from requests_oauthlib import OAuth1Session
from flask import *
import settings
import json


app=Flask(__name__)

app.config['SECRET_KEY']=os.urandom(24)


Post_API='https://api.twitter.com/1.1/statuses/update.json'
tw=OAuth1Session(settings.C_KEY,settings.C_SECRET,settings.A_KEY,settings.A_SECRET)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    return '''<p>ログインしてください<p>'''

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        if username=='admin':
            session['username']=request.form['username']
            return redirect(url_for('index'))
        else:
            return '''<p>ユーザー名が違います</p>'''
    return '''
        <form action="" method="post">
            <p><input type="text" name="username">
            <p><input type="submit" value="Login">
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=='POST':
        msg=request.form['msg']
        url=Post_API
        params={'status':msg,'lang':'ja'}
        req=tw.post(url,params=params)
        if req.status_code==200:
            print("ok")
        else:
            print("Error: %d" % req.status_code)
            res_text = json.loads(req.text)
            print(str(res_text))

        return render_template('index.html',msg=msg)

if __name__=='__main__':
    app.debug=True
    app.run()
