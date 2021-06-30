from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('localhost', 27017)


db = client.project

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    all_oreders = list(db.order.find({}, {'_id': False}))

    return jsonify({'all_oreders': all_oreders})

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    adress_receive = request.form['adress_give']
    phone_receive = request.form['phone_give']

    # DB연결
    doc = {
        'name': name_receive,
        'number': number_receive,
        'adress': adress_receive,
        'phone': phone_receive
    }
    db.order.insert_one(doc)

    return jsonify({'msg':'주문 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)