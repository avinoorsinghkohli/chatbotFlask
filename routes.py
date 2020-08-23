from app import app
from flask import Flask, render_template, url_for, redirect, flash, get_flashed_messages, request
import requests
import sys
output=[]
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method=='POST':
        result=list(request.form.values())[0]
        if result.lower() =="restart":
            output.clear()
        else:
            try:
                print(result)
                r=requests.post("http://localhost:5002/webhooks/rest/webhook",json={"message":str(result)})
                print(r)
                bot_message=""

                print(r.json())
                for i in r.json():
                    
                    if "text" in i.keys():

                        bot_message=bot_message+i['text']
                        #print(f"{i['text']}")

                    if "image" in i.keys():
                        bot_message=bot_message+i['image']
                        #print(f"{i['image']}")
                    
                output.extend([("message avi", result), ("message bot", bot_message)])
                
                
            except:
                print("Invalid Output\n")
                print(sys.exc_info()[0])
                output.extend([("message avi", result), ("message bot", "Error")])
        print(output)
        return render_template("home.html", result=output)
    return render_template("home.html", result=output)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', result=output)