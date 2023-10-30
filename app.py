from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect('database.db')

# if connection.is_closed():
#     print("The connection is closed.")
# else:

with conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS transactions (date TEXT, amount REAL, account TEXT);")
    

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO transactions VALUES (?, ?, ?);", (
                request.form.get("date"),
                float(request.form.get("amount")),
                request.form.get("account")
            ))
        conn.commit()
                
    return render_template("form.html")
 

@app.route("/transactions")
def show_transactions():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions;")
        transactions = cursor.fetchall()
    return render_template("transactions.jinja2", entries=transactions)