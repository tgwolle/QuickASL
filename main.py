from flask import Flask, render_template, url_for, flash, redirect, request
# from forms import processQuery
import flask
#from audio import printWAV
import time, random, threading
from turbo_flask import Turbo
from flask_behind_proxy import FlaskBehindProxy
import requests
#import shutil # - - This module helps to transfer information from 1 file to another 
#from bs4 import BeautifulSoup
app = Flask(__name__)
turbo = Turbo(app)
proxied= FlaskBehindProxy(app)

letters = {
  "A": "static/images/A.png",
  "B": "static/images/B.png",
  "C": "static/images/C.png",
  "D":"static/images/D.png",
  "E":"static/images/E.png",
  "F": "static/images/F.png",
  "G":"static/images/G.png",
  "H": "static/images/H.png",
  "I":"static/images/I.png",
  "J": "static/images/J.png",
  "K":"static/images/K.png",
  "L":"static/images/L.png",
  "M":"static/images/M.png",
  "N":"static/images/N.png",
  "O":"static/images/O.png",
  "P":"static/images/P.png",
  "Q":"static/images/Q.png",
  "R":"static/images/R.png",
  "S":"static/images/S.png",
  "T":"static/images/T.png",
  "U":"static/images/U.png",
  "V":"static/images/V.png",
  "W":"static/images/W.png",
  "X":"static/images/X.png",
  "Y":"static/images/Y.png",
  "Z":"static/images/Z.png",
  ".": "static/images/period.png",
  ",": "static/images/comma.png",
  "?": "static/images/qs.png",
  "!": "static/images/exc.png",
  "+":"static/images/empty.png"
 
}

# stores list of the image links to the letters from user input globally
user_words = [""]

@app.route("/")                          # this tells you the URL the method below is related to
def home():
    user_words.clear()
    return render_template('index.html', subtitle='Home Page')
   
@app.route("/learn-more")
def about():
    return render_template('about.html', subtitle='Learn More')
   
@app.route("/main_page", methods=['GET'])
def main_page():
    todos = user_words
    print(todos)
#     if todos == None:
#             flash(f'Input cannot be empty', 'failed')
#             return redirect(url_for('main_page'))
    return render_template('main_page.html',todos=todos)
#   return render_template('main_page.html', subtitle='Main Page')
  
'''def processInput(ls):
  output_list=[]
  for word in ls:
    for letter in word:
      output_list.append(letters[letter])
    output_list.append(letters["empty"]) 
  return output_list
  '''

# Clears images from display
# test redirect works
@app.route('/clear_images')
def clear_images():
    user_words.clear()
    return redirect(url_for('main_page'))

# returns true if input is valid  
def is_valid_input(x):
  is_valid_input = True
  for l in x:
    if l not in letters:
      return False 
  return is_valid_input
  
def get_input():
  input = user_words
#    with app.test_request_context():
#         from flask import request
#         input = request.form.get('user_input')
  print(input)
  return input

# V3  
# Check that input is valid: can't be numbers 
#   Test could be check what happens when enter valid input/ invalid
# Processes the input information and displays it.
@app.route('/process_query', methods=['POST'])
def process_query():
  text = request.form.get('user_input')
  
  words = text.upper().replace(" ","+")
  try:
    user_words.remove("")
  except:
    print("empty not found")
  #output_list=[]
  for character in words:
      user_words.append(letters[character])
#     if form.validate_on_submit()

  return redirect(url_for('main_page'))

#   if is_valid_input(user_words):
#     return redirect(url_for('main_page'))
#   else:
#     flash(f'Input is invalid', 'error')
#     return redirect(url_for('main_page'))
      # This is probably where we would add the flash
      #  if is_valid_input(user_words) redirect else flash statement
    
  
# if page not found direct to page not found page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# if bad direct request redirect to error page
@app.errorhandler(400)
def page_not_found(e):
    return render_template('400.html'), 400

# if error direct to error page
@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500

# if flask error direct user to error page
@app.errorhandler(Exception)
def page_not_found(e):
  return render_template('500.html'), 500


# returns list of words from input in upper case.
# V2
# @app.route('/process_query', methods=['POST'])
# def process_query():
#     #data = flask.request.form  # is a dictionary
#     #input = data['user_input']
#     input= "H"
#     input_in_list = input.upper().split(' ') 
#     output_list=[]
#     for word in input_in_list:
#       for letter in word:
#         output_list.append(letters[letter])
#       output_list.append(letters["empty"])
      
#     #print("letter"+ input)
#     #print(output_list)
#     #same= '<img src="' + str(output_list[0]) + '"/>'
#     #print(same)
#     return render_template('main_page.html', same=output_list)

# V1
# @app.route("/process", methods=['GET', 'POST'])   
# def process_query():
#     form = processForm()
#     if form.validate_on_submit(): 
#       user = form.enter.data
#       user = user.upper().split(' ') 
#       output_list=[]
#       for word in user:
#         for letter in word:
#           output_list.append(letters[letter])
#           output_list.append(letters["empty"])
      
#       print("letter"+ input)
#       print(output_list)
#       same= '<img src="' + str(output_list[0]) + '"/>'
#       print(same) 
#       return render_template('main_page.html', same=same)
#       return render_template('process.html', title='Process', form=form, same=same )
  
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")