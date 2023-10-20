from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

POSTGRESQL_URI = "postgres://vpadtlpg:ZxUE-nd_JZGnhoxRp2vWkwA1aKTUdbl9@surus.db.elephantsql.com/vpadtlpg"

connection = psycopg2.connect(POSTGRESQL_URI)
try: 
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE transactions (date TEXT, amount REAL, account TEXT);")
except psycopg2.errors.DuplicateTable:
    pass

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        with connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "INSERT INTO transactions VALUES (%s, %s, %s);", 
                        (
                        request.form.get("date"),
                        float(request.form.get("amount")),
                        request.form.get("account")
                        )
                                )
                    connection.commit()
                except Exception as e:
                   print(f"Error inserting data: {e}")
    return render_template("form.html")
 

@app.route("/transactions")
def show_transactions():
    with connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM transactions;")
                transactions = cursor.fetchall()
    return render_template("transactions.jinja2", entries=transactions)