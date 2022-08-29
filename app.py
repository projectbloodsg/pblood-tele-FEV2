from flask import Flask, flash, jsonify, redirect, render_template, request, session
from datetime import datetime
import re
import os
from decouple import config
import requests
from icecream import ic

app = Flask(__name__)
BASE_URL = config('BASE_URL')

def getFirst():
    response = requests.get("{base_url}/messages/root".format(base_url=BASE_URL))
    print(response)
    if response.status_code != 200:
        print("Result not found!")

    return response.json()

def getMessage(id): #get message based on id
    if True in [char.isdigit() for char in id]:
        response = requests.get("{base_url}/messages/id/{Id}".format(base_url=BASE_URL, Id=id))
        if response.status_code != 200:
            print("Result not found!")

        return response.json()
    else:
        return None
    
def getChild(id):
    response = requests.get("{base_url}/messages/child/{childId}".format(base_url=BASE_URL, childId=id))
    if response.status_code != 200:
        print("Result not found!")

    return response.json()

@app.route("/") #this route is the most basic view
def index():
    parent = {}
    children = []
    try:
        parent = getFirst()[0]
        parent_content = parent['content']
        children = getChild(parent['message_id'])
        
    except Exception as e:
        print(e)
    return render_template("index.html",parent = parent, children = children)


# you can also use a particular data type such as int,str
# @app.route('post/<int:id>', methods=['GET', 'POST'])
@app.route('/<string:id>', methods=['GET'])
def render_new_parent(id):
    ic(id)
    parent = {}
    children = []
    try:
        parent = getMessage(id)
        ic(parent)
        children = getChild(parent['message_id'])
        
    except Exception as e:
        print(e)
    return render_template("index.html",parent = parent, children = children)