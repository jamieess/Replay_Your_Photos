from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index2.html')


# @app.route('/memo', methods=['POST'])
# def post_article():
#
#     url_receive = request.form['url_give']
#     comment_receive = request.form['comment_give']
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get( url_receive, headers=headers )
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#
#     og_image = soup.select_one('meta[property="og:image"]')
#     og_title = soup.select_one('meta[property="og:title"]')
#     og_description = soup.select_one('meta[property="og:description"]')
#
#     title = (og_title['content'])
#     image = (og_image['content'])
#     description = (og_description['content'])
#
#     doc = {
#         'title' : title,
#         'url' : url_receive,
#         'comment' : comment_receive,
#         'image' : image,
#         'description' : description
#     }
#     db.alonememo.insert_one(doc)
#
#     #print(doc)
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})
#
#
# @app.route('/memo', methods=['GET'])
# def read_articles():
#
#     # DB 5개 가지고오
#     memoInfo = list(db.alonememo.find({}, {"_id": False}))
#     #print(memoInfo)
#     #response["result"] == "sucess")
#     # #Json 만들어서
#     returnVal = {"result" : "success", "memolist": memoInfo}
#
#
#     #클라이언트에 주기
#     return jsonify(returnVal)
#
#     return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)