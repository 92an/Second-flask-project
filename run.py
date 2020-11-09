import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "randomstring123"
messages = []


def add_message(username, message):
    """Adds messages to the list of messages"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})


def get_all_messages():
    """Get all messages sent and seperate the with <br> tag"""
    return "<br>".join(messages)


@app.route("/", methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    if "username" in session:
        return redirect(url_for("user", username=session["username"]))

    return render_template("index.html")


@app.route("/chat/<username>", methods=["GET", "POST"])
def user(username):
    """Display chatt messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username=session["username"]))
    return render_template(
        "chat.html", username=username, chat_messages=messages)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
