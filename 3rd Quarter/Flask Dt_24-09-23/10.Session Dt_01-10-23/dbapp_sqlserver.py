import pyodbc
from flask import Flask, request, render_template

conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=MOEED-1\SQLEXPRESS;DATABASE=pythontest;Trusted_Connection=yes;"


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student")
        rows = cursor.fetchall()
        cursor.close()
        return render_template("viewall.html", records=rows)
    else:
        return "Nothing to Display"


@app.route("/createstudent", methods=["GET", "POST"])
def createstudent():
    return render_template("createstudent.html")


@app.route("/addstudent", methods=["GET", "POST"])
def addstudent():
    if request.method == "POST":
        studentID = request.form["studentID"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        address = request.form["address"]
        city = request.form["city"]

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO Student (StudentID,FName,LName,Address,City) VALUES (?,?,?,?,?)",
            studentID,
            fname,
            lname,
            address,
            city,
        )

        conn.commit()
        cursor.close()
        return render_template("createstudent.html", message="Successfully Added")
    else:
        return "Nothing to Display"


if __name__ == "__main__":
    app.run(debug=True)
