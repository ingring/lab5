from flask import Flask, request
import os

app = Flask(__name__)

CONTACTS = [{"name":"Ingrid"}]

@app.route('/')
def index():
    return "hei"

@app.route('/hello')
def hello():
    return "hello"

@app.route('/contacts', methods=['POST'])
def update_contact():
    name = request.json['name']
    contact = {"name":name}
    CONTACTS.append(contact)

app.run()