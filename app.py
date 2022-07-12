from flask import Flask, jsonify, render_template
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from requests import request

load_dotenv()
mongodbUri = os.environ.get('mongodbUri')

ca = certifi.where()
client = MongoClient(mongodbUri, tlsCAFile=ca)
db = client.liquor


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/join')
def join():
    return render_template("join.html")


@app.route('/signUp', methods=["GET"])
def idCheck_dup():
    id_list = list(db.users.find({}, {"_id": False, "pw": False}))
    return jsonify(id_list)


@app.route('/signUp', methods=["POST"])
def signUp():
    id_receive = request.form['id']
    pw_receive = request.form['pw']

    doc = {
        "userID": id_receive,
        "pw": pw_receive,
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/review')
def review():
    return render_template("review.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
