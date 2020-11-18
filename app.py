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

@app.route('/memory', methods=['POST'])
def post_memories():
    img_receive = request.form['img_give']
    youtube_receive = request.form['youtube_give']
    date_receive = request.form['date_give']
    memo_receive = request.form['memo_give']

    youtube_section = youtube_receive.split("=")
    youtube_section2 = youtube_section[1].split("&")

    youtube_code = "https://www.youtube.com/embed/" + str(youtube_section2[0].strip('[]'))

    memory = {
        'img': img_receive,
        'youtube': youtube_code,
        'date': date_receive,
        'memo': memo_receive
    }
    db.memories.insert_one(memory)

    #print(memory)
    return jsonify({'result': 'success', 'memories': '메모가 성공적으로 작성되었습니다!'})


@app.route('/memory', methods=['GET'])
def read_memories():
    memories = list(db.memories.find({}, {"_id": False}))
    # return jsonify({'result': 'success', 'memories': memories})

    # print(memories)
    returnVal = {"result" : "success", "memories": memories}
    #
    #
    # #클라이언트에 주기
    return jsonify(returnVal)

    return jsonify({'result': 'success', 'memories': memories})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)