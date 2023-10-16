from flask import Flask, render_template, request

app = Flask(__name__)
transaction = []

@app.route("/")
def home():
    print(request.form.get("account"))
    transactions.append((
        request.form.get("date"),
        float(request.form.get("amount")),
        request.form.get("account")
    ))
    return render_template("form.html")
 

@app.route("/mysite")
def hello():
    return "Hello World"