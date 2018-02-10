import os
import json
import request

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some_key"

@app.route("/")
def index():
    return render_template('index.html', page_title='Cats & Co')

@app.route("/about/")
def about():
    data = []
    with open('data/cats.json', 'r') as json_data:
        data = json.load(json_data)
    
    return render_template('about.html', page_title='About', cats_data=data)
    

@app.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {0}, we received your message".format(request.form["name"]))
        
        
    return render_template('contact.html', page_title='Contact')
    

@app.route("/careers/")
def careers():
    return render_template('careers.html', page_title='Careers')
    
@app.route("/about/<cat_name>")
def cat_detail(cat_name):
    cat = {}
    with open("data/cats.json", "r") as json_data:
        data = json.load(json_data)
        for item in data:
            if item["url"] == cat_name:
                cat = item
    
    return render_template('about_cat.html', cat=cat)

if __name__=="__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)