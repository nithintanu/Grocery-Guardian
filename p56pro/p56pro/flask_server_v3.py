import flask
import werkzeug
import time
from flask import *

import p56integr1_mod

app = flask.Flask(__name__)

import random 

@app.route('/fetchdata2', methods = ['GET', 'POST'])
def fetchdata2():
    return str(random.randint(25,100))
    #return "17.8,73.2;17.9,73.2;17.8,73.3"

@app.route('/fetchdata', methods = ['GET', 'POST'])
def fetchdata():
    return "17.8,73.2"

# @app.route('/')
# def index():
#     return 'healthcheck:ok'
import json 
@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    result='-'
    #print('---',request.form["description"])
    files_ids = list(flask.request.files)
    print("\nNumber of Received Images : ", len(files_ids))
    image_num = 1
    for file_id in files_ids:
        print("\nSaving Image ", str(image_num), "/", len(files_ids))
        imagefile = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("Image Filename : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        imagefile.save(timestr+'_'+filename)
        image_num = image_num + 1

        #################
        healthcondition='diabetes'
        try:
            if request.form["description"]!='':
                healthcondition=request.form["description"]
        except Exception as exp:
            pass 
        result = p56integr1_mod.p56query(timestr+'_'+filename, healthcondition)
        #################
    print("\n result is ", result)
    #res= {"message":"thank you", "output":"result is "}
    
    #return res, 200

    #message = {'message': 'Success1', 'output':"helo"}
    #print('message is ',message)
    #print('json output is ', json.dumps(message))
    # Convert message to JSON and return with status code 200
    #return jsonify(message), 200
    #return json.dumps(message), 200

    message = {'message': 'Success2', 'output':str(result), 'status':200}

    # Convert message to JSON and return with status code 200
    return jsonify(message), 200

app.run(host="0.0.0.0", port=5000, debug=True)