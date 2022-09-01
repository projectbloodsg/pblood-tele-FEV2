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

def newChildMessage(data):
    response = requests.post("{base_url}/messages".format(base_url=BASE_URL),data)
    if response.status_code != 201:
        print("Result not found!")
    return response.json()

def updateMessage(id,data):
    response = requests.put("{base_url}/messages/id/{messageId}".format(base_url=BASE_URL, messageId=id),data)
    if response.status_code != 200:
        print("Result not found!")
    return response.json()

def deleteMessage(id):
    response = requests.delete("{base_url}/messages/id/{messageId}".format(base_url=BASE_URL, messageId=id))
    if response.status_code != 204:
        print("Result not found!")
    return response.json()




@app.route("/", methods=['GET','POST']) #this route is the most basic view
def index():
    if request.method == "GET":
        parent = {}
        children = []
        try:
            parent = getFirst()[0]
            #ic(parent)
            children = getChild(parent['message_id'])
            
        except Exception as e:
            print(e)
        return render_template("index.html",parent = parent, children = children, root = True)


""" you can also use a particular data type such as int,str
    @app.route('post/<int:id>', methods=['GET', 'POST'])"""
@app.route('/<string:id>', methods=['GET','POST'])
def render_new_parent(id):
    if request.method == "GET":
        #ic(id)
        parent = {}
        children = []
        try:
            parent = getMessage(id)
            #ic(parent)
            children = getChild(parent['message_id'])
            
        except Exception as e:
            print(e)
        return render_template("index.html",parent = parent, children = children)
    if request.method == "POST":
        """it will only receive POST if i press "done", and it will update the database from here with the changed content"""
        from_js = request.json #data from javascript

        ic(from_js)
        """EDITING OF MESSAGES"""
        if from_js['type'] == 'edit_message':
            edited_message = from_js['message']
            data = {"content": edited_message,
                "image_url": "",}
            updateMessage(id,data) ####REMEMBER TO ENABLE THIS LATER
        

        """CREATION OF CHILD MESSAGES"""
        if from_js['type'] == 'new_child_message':
            data = {
                "content": from_js['message'],
                "image_url": "",
                "parent_id": from_js['parent_id'],
            }

            newChildMessage(data) ####REMEMBER TO ENABLE THIS LATER
        
        """DELETION OF MESSAGE"""
        if from_js['type'] == 'delete_message':
            ic(deleteMessage(from_js['id']))

        return redirect(request.url)
        