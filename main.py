from flask import Flask, request
from database import db
import os

app = Flask(__name__)

CONTACTS = [{"name":"Ingrid"}]

@app.route('/')
def index():
    documents = db.my_collection.find()
    return {"documents": documents}

@app.route('/hello')
def hello():
    return "hello"

@app.route('/contacts', methods=['POST'])
def update_contact():
    name = request.json['name']
    contact = {"name":name}
    CONTACTS.append(contact)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=os.getenv("PORT", default=5000))