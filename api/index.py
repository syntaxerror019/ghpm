from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')## lazi
def login():
    return redirect("/download")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/download')
def download():
    return render_template("get.html")

@app.route('/create')
def create():
    return render_template("login.html") #(create account page actually)



@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
