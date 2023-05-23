from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from Virustotal import file_hashing
import streamlit as st
from Slang import *

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source, duration=120)
            transcript = recognizer.recognize_google(data, key=None, language='ko-KR')
            text_list = transcript.split()
            print("입력 파일의 총 어색한 단어 점수 : ",slang_filter(text_list=text_list))

            # print(text)
        file.save('./uploads/' + file.filename)
        file_hashing(inputfile=file.filename)
    return render_template('index.html', transcript=transcript)
@app.route("/steamlit")
def streamlit():
    st.write("hello")
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
