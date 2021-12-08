from flask import Flask,render_template,request
import json as js
import requests
import sys
sys.path.append('.gitignore/') 
import secrets

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Welcome!</h1>'

@app.route('/name/<name>')
def hello_name(name):
    return render_template("name.html",name=name)

@app.route('/headlines/<name>')
def top_headlines(name):
    response = requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json?api-key="+secrets.api_key)
    result_from_js=js.loads(response.text)
    result=[]
    num = 1
    for item in result_from_js['results'][0:5]:
        result.append(str(num)+'. '+item['title'])
        num+=1
    return render_template("headlines.html",name=name,result=result)

if __name__=='__main__':
    app.run()