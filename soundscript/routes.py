from soundscript import app
import os
from flask import render_template, request, redirect, jsonify
from werkzeug.utils import secure_filename

@app.route("/")
def index():
    print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
    print(app.config["DB_NAME"])
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

@app.route("/uploads", methods=["POST", "GET"])
def upload_file():
    if request.method == "POST":
        if 'audiofile' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files["audiofile"]

        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOADS"], filename))
            return jsonify({"message": "File uploaded successfully"}), 200

    return render_template('uploads.html')