from flask import Flask, jsonify
app = Flask(__name__)
dict_eng = {'apple': '사과', 'banana': '바나나', '703': 'hell'}

@app.route('/dictionary/<string:voca>')
def my_eng_voca(voca):
    if voca in dict_eng:
        return f'{voca}은/는 {dict_eng[voca]}'
    else:
        return f'{voca}은/는 나만의 단어장에 없는 단어입니다!'

if __name__ == '__main__':
    app.run(debug=True)