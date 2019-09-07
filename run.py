import os
from datetime import datetime
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({}) {} : {}".format(now, username, message))

def get_all_messages():
    """Get all messages and separate using with br"""
    return "<br>".join(messages)



@app.route('/')
def index():
    """main page with instructions"""
    return 'To send a message use /USERNAME/MESSAGE'

@app.route('/<username>')
def user(username):
    """Display chat messages, its taking messages from list"""
    return '<h1>Welcome, {0}</h1> {1}'.format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """"Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)

