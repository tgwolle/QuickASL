from flask import Flask, render_template, url_for, flash, redirect
#from audio import printWAV
import time, random, threading
from turbo_flask import Turbo
import requests
import shutil # - - This module helps to transfer information from 1 file to another 
from bs4 import BeautifulSoup
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

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(400)
def page_not_found(e):
  return render_template('400.html'), 400

@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

@app.errorhandler(Exception)
def page_not_found(e):
  return render_template('500.html'), 500


  
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")