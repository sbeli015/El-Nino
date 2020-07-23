from flask import Flask,redirect,url_for,render_template,request,session,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key = "password"

db = MySQL(app)

@app.route("/")
def sendhome():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login" ,  methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already a Member.")
            return redirect(url_for("user"))
        return render_template("log.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    stance= None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            stance = request.form["stance"]
            session["stance"] = stance
            flash("Your stance has been entered!")
        else:
            if "stance" in session:
                stance = session["stance"]

        return render_template("user.html",stance=stance)
    else:
        flash("You aren't a Member yet.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"Hope you enjoyed your stay, {user}!", "info")
    session.pop("user", None)
    session.pop("class", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
