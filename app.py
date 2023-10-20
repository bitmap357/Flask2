from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

POSTGRESQL_URI = "postgres://vpadtlpg:ZxUE-nd_JZGnhoxRp2vWkwA1aKTUdbl9@surus.db.elephantsql.com/vpadtlpg"

connection = psycopg2.connect(POSTGRESQL_URI)
with connection:
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE transactions (date TEXT, amount REAL, account TEXT);")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form.get("account"))
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO transactions VALUES (%s, %s, %s);" 
                    (
                    request.form.get("date"),
                    float(request.form.get("amount")),
                    request.form.get("account")
                    )
                            )
    return render_template("form.html")
 

@app.route("/transactions")
def show_transactions():
    with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM transactions;")
                transactions = cursor.fetchall()
    return render_template("transactions.jinja2", entries=transactions)