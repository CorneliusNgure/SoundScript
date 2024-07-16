from soundscript import app
from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm-password")

        print(username, email, password, confirm_password)
        return redirect(request.url)
    return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        print(email, password)
        
        return redirect(request.url)
    return render_template("login.html")

@app.route("/contact_us", methods=["POST", "GET"])
def contact_us():
    if request.method == "POST":
        
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        phone = request.form.get("phone")
        subject = request.form.get("subject")
        message = request.form.get("message")
        
        print(name, email, password, phone, subject, message)
        
        return redirect(request.url)
    return render_template("contact_us.html")
