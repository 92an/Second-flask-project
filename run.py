import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_message(username, message):
    """Adds messages to the list of messages"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({0}) {1}: {2}".format(now, username, message))


def get_all_messages():
    """Get all messages sent and seperate the with <br> tag"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """Main page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    """Display chatt messages"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """Sends messages"""
    add_message(username, message)
    return redirect("/" + username)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
