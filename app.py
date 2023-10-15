from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print(request.args)
    return render_template("form.html")
 
 
@app.route("/mysite")
def hello():
    return "Hello World"