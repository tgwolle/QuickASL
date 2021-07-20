from flask import Flask, render_template, url_for, flash, redirect
#from audio import printWAV
import time, random, threading
from turbo_flask import Turbo
import azure.cognitiveservices.speech as speechsdk
speech_config = speechsdk.SpeechConfig(subscription="<paste-your-speech-key-here>", region="<paste-your-speech-location/region-here>")
app = Flask(__name__)
turbo = Turbo(app)


@app.route("/")                          # this tells you the URL the method below is related to
def home():
    return render_template('index.html', subtitle= 'Home Page')
   
@app.route("/learn-more")
def about():
    return render_template('about.html', subtitle='Learn More')
   
@app.route("/main_page")
def main_page():
    return render_template('main_page.html')


  
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")