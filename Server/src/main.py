from app import app
from bson import json_util
from flask import render_template, request
from database import post_message, messagecollection


def genNavbar(currentPage):
    navlinks = ""
    pages = {"Home": "/", "Messages": "/messages", "The Team": "/team"}
    for i in pages:
        navlinks += render_template("navlink.html", label=i,
                                    href=pages[i], active=("active" if currentPage == i else ""))
    return render_template("navbar.html", navlinks=navlinks)


@app.route('/')
def index():
    return render_template('index.html', navbar=genNavbar("Home"))


@app.route('/messages')
def messages():
    messagedict = {}
    messagegroups = ""
    for message in messagecollection.find():
        if message['date'] in messagedict:
            messagedict[message['date']] += [message]
        else:
            messagedict[message['date']] = [message]
    for key in messagedict:
        group = messagedict[key]
        messagesingroup = ""
        for message in group:
            print(message)
            messagesingroup += render_template(
                "message.html", content=message['content'], sender=message['sender'])
        messagegroups += render_template("messagegroup.html",
                                         messages=messagesingroup, date=key)
    return render_template('messages.html', navbar=genNavbar("Messages"), messagegroups=messagegroups)


@app.route('/team')
def about():
    return render_template('theteam.html', navbar=genNavbar("The Team"))


@app.route('/api/postmessage', methods=['POST'])
def postmessage():
    print(request.data)
    messagejson = json_util.loads(request.data)
    print(messagejson)
    return post_message(messagejson)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80", debug=True)
