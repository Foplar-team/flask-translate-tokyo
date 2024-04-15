from flask import Flask, request
from googletrans import Translator
from flask_cors import CORS
import time


app = Flask(__name__)
CORS(app)  # 모든 도메인에서의 요청을 허용하도록 설정

@app.route('/api/translate',methods=['GET', 'POST'])
def translate():
    start_time = time.time()
    # data['script'] : 번역 할 스크립트가 들어있는 객체
    # data['dest'] : 번역 할 타겟 언어가 들어있는 객체 ( en | ko | es )
    data = request.json

    # translator 클래스 선언
    translator = Translator()
    # google translate api에 번역 요청
    result = translator.translate(data['script'], dest=data['dest'])
    print(f'total translate time : {time.time() - start_time}') # 함수 시작, 끝 duration 서버에 기록
    return result.text

