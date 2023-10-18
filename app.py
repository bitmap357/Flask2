from flask import Flask, render_template, request

app = Flask(__name__)
transactions = [
    ("2020-08-25", 70.00, "Checking"),
    ("2020-08-27", 46.00, "Savings"),
    ("2020-08-29", 34.00, "Checking"),
]

@app.route("/", methods=["GET", "POST"])
def home():
    print(request.form.get("account"))
    transactions.append(
        (
        request.form.get("date"),
        float(request.form.get("amount")),
        request.form.get("account")
        )
    )
    return render_template("form.html")
 

@app.route("/transactions")
def show_transactions():
    return "Hello World"