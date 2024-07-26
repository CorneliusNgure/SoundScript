from soundscript import app
import os
from flask import render_template, request, redirect, jsonify, url_for
from werkzeug.utils import secure_filename
from soundscript.api_speech_to_text.api_communication import process_transcription

"""
Module defines the routes and their associated logic for the Flask application.

Routes included:
- `/`: Renders the home page.
- `/register`: Handles user registration.
- `/login`: Handles user login.
- `/contact_us`: Handles contact form submissions.
- `/upload_file`: Handles file uploads and processes transcription.
"""
@app.route("/")
def index():
    """
    Renders the home page.

    Route displays the index page of the application and 
    prints the current Flask environment
    and database name to the console for debugging purposes.
    """
    print(f"FLASK_ENV: {os.getenv('FLASK_ENV')}")
    print(app.config["DB_NAME"])
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Handles user registration.

    For GET requests, it renders the registration form. 
    For POST requests, it processes form data, including username, 
    email, password, and confirmation password, 
    and then redirects back to the registration page.

    Returns:
        - A rendered registration form for GET requests.
        - Redirects to the same page for POST requests after processing.
    """
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
    """
    Handles user login.

    For GET requests, it renders the login form. 
    For POST requests, it processes form data, including email 
    and password, and then redirects back to the login page.

    Returns:
        - A rendered login form for GET requests.
        - Redirects to the same page for POST requests after processing.
    """
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        print(email, password)
        
        return redirect(request.url)
    return render_template("login.html")

@app.route("/contact_us", methods=["POST", "GET"])
def contact_us():
    """
    Handles contact form submissions.

    For GET requests, it renders the contact form. 
    For POST requests, it processes form data, including name, email, 
    password, phone, subject, and message, 
    and then redirects back to the contact page.

    Returns:
        - A rendered contact form for GET requests.
        - Redirects to the same page for POST requests after processing.
    """
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

@app.route("/upload_file", methods=["POST", "GET"])
def upload_file():
    """
    Handles file uploads and processes transcription.

    For POST requests, it checks if an audio file is provided, 
    saves it to the configured upload directory, processes the 
    transcription, and then reads and returns the transcript text.

    Returns:
        - A JSON response with a success message and the transcribed text for POST requests.
        - Renders the file upload form for GET requests.
    """
    if request.method == "POST":
        if 'audiofile' not in request.files:
            return jsonify({"message": "No file part in the request"}), 400

        file = request.files["audiofile"]

        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOADS"], filename)
            
            print(f"Saving file to: {file_path}") # debugging

            file.save(file_path)

            # PROCESS TRANSCRIPT
            process_transcription(file_path)

            # # URL for the uploaded file
            # audio_url = url_for('static', filename=f'uploads/{filename}', _external=True)
            # print(f"Audio URL: {audio_url}")
            # transcript_text, transcript_utterances = transcribe_audio(audio_url)

            #READ TRANSCRIPT
            text_filename = file_path + '.txt'
            with open(text_filename, "r") as f:
                transcript_text = f.read()

            return jsonify({
                "message": "File uploaded successfully",
                "transcript": transcript_text,
                }), 200

    return render_template('upload_files.html')