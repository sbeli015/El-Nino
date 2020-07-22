from flask import Flask,redirect,url_for,render_template,request,session
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key = "password"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login" ,  methods=["POST", "GET"])
def input():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("log.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("input"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("input"))

if __name__ == "__main__":
    app.run(debug=True)
