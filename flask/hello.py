from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/python')
def python():
    return 'Python is fun !!!!'

@app.route('/dictionary/<string:word>')
def dictionary(word):
    dictionary = {
        'apple' : '사과',
        'banana' : '바나나',
        'orange' : '오렌지',
        'strawberry' : '딸기'
    }
    result = dictionary.get(word,'나만의 단어장에 없는 단어')

    return f'{word}은(는) {result}입니다'