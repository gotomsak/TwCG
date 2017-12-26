from flask import *
import numpy as np

#インスタンス化
app=Flask(__name__)


#メッセージをランダムに表示するメソッド
def picked_up():
    messages=[
        "こんにちは、あなたの名前を入力してください",
        "やあ、お名前はなんですか？",
        "あなたの名前を教えてね"
    ]
    #NumPyのrandom.choiceで配列からランダムに取り出し
    return np.random.choice(messages)

#ここからウェブアプリケーション用のルーティングを記述
#indexにアクセスしたときの処理
@app.route('/')
def index():
    title="ようこそ"
    message=picked_up()
    #index.htmlをレンダリングする
    return render_template('index.html',
                           message=message,title=title)

# /post にアクセスしたときの処理
@app.route('/post',methods=['GET','POST'])
def post():
    title="こんにちは"
    if request.method=='POST':
        #リクエストフォームから「名前」を取得して
        name=request.form['name']
        #index.htmlをレンダリングする
        return render_template('index.html',
                               name=name,title=title)
    else:
        #エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))

if __name__=='__main__':
    app.debug=True#デバックモード有効化
    app.run(host='0.0.0.0')#どこからでもアクセス可能に