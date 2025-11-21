from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "something_secret_and_spicy"


# ----------- MySQL Connection Function ----------
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="IshuSQLadmin",
        password="Ishuadmin#1",
        database="collegeproject"
    )


# ------------------ HOME ------------------
@app.route("/")
def home():
    return redirect(url_for("login"))   # fixed — only / should redirect


# ------------------ SIGNUP ------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm-password"]

        if password != confirm:
            flash("Passwords do not match!")
            return redirect(url_for("signup"))

        conn = get_db()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users (email, userpassword) VALUES (%s, %s)",
                (email, password)
            )
            conn.commit()
        except mysql.connector.IntegrityError:
            flash("Email already exists!")
            return redirect(url_for("signup"))
        finally:
            conn.close()

        flash("Signup successful! You can now log in ✨")
        return redirect(url_for("login"))

    return render_template("signup.html")


# ------------------ LOGIN ------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT userpassword FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        conn.close()

        if row and row[0] == password:
            #  REDIRECT TO HOMEPAGE
            return redirect(url_for("homepage"))
        else:
            flash("Invalid email or password!")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/quiz")
def quiz():
    return render_template("quizpage.html")

@app.route("/result/fantasy")
def result_fantasy():
    return render_template("fantasy.html")

@app.route("/result/mystery")
def result_mystery():
    return render_template("mystery.html")

@app.route("/result/romance")
def result_romance():
    return render_template("romance.html")

@app.route("/result/scifi")
def result_scifi():
    return render_template("scifi.html")

@app.route("/result/history")
def result_history():
    return render_template("history.html")

@app.route("/result/literary")
def result_literary():
    return render_template("literary.html")

@app.route("/result/horror")
def result_horror():
    return render_template("horror.html")

@app.route("/result/darkacademia")
def result_darkacademia():
    return render_template("darkacademia.html")

@app.route("/result/magicalrealism")
def result_magicalrealism():
    return render_template("magicalrealism.html")

@app.route("/result/romantasy")
def result_romantasy():
    return render_template("romantasy.html")




if __name__ == "__main__":
    app.run(debug=True)
