from app import app, db
from flask import request, redirect, render_template
from app.models import Users, Messages
from app.registerLogical import *
import sqlalchemy

@app.route('/')
def index():
    return render_template("register.html")

@app.route('/register')
def register():
    usernameData = request.args.get("NameInput")
    passwordData = request.args.get("PasswordInput")
    verifyPasswordData = request.args.get("VerifyPasswordInput")
    
    if checkPassword(passwordData, verifyPasswordData) == False:
        return render_template("register.html", validMess = "<p style=\"color: red\">Passwords do not match</p>")
    
    try:
        db.session.add(Users(username = usernameData, password = passwordData))
        db.session.commit()
    except:
        return render_template("register.html", validMess = "<p style=\"color: red\">This name already exists</p>")

    return redirect("/all", code=302)

@app.route('/send')
def send():
    return render_template("send.html")

@app.route('/send_check')
def send_check():
    usernameData = request.args.get("NameInput")
    passwordData = request.args.get("PasswordInput")
    messageData = request.args.get("MessageInput")
    
    sql = sqlalchemy.text(f"SELECT * FROM Users WHERE username='{usernameData}' AND password='{passwordData}'")
    result = db.session.execute(sql)
    user = result.fetchone()

    if user:
        db.session.add(Messages(userId = user.id, message = messageData))
        db.session.commit()
        return redirect("/all", code=302)
    else:
        return render_template("send.html", validMess = "<p style=\"color: red\">Invalid username or password</p>") 

@app.route('/all')
def getAllMes():
    sql = sqlalchemy.text("SELECT username, message FROM Users, Messages WHERE Users.id = Messages.userId")
    chat = []
    for responce in db.session.execute(sql):
        chat.append(f"<p>{responce.username}: {responce.message}</p><br />")
    return render_template("all_messages.html", data = "".join(chat))