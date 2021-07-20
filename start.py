#!/usr/bin/python
# -*- coding: utf-8 -*-

# Signspeech
# Copyright (C) 2019 Javier O. Cordero Pérez <javier@imaginary.tech>.

# This file is part of Signspeech.

# Signspeech is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Signspeech is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Signspeech.  If not, see <https://www.gnu.org/licenses/>.

print ("""
╔═╗╦╔═╗╔╗╔╔═╗╔═╗╔═╗╔═╗╔═╗╦ ╦
╚═╗║║ ╦║║║╚═╗╠═╝║╣ ║╣ ║  ╠═╣
╚═╝╩╚═╝╝╚╝╚═╝╩  ╚═╝╚═╝╚═╝╩ ╩

Signspeech  Copyright (C) 2019  Javier O. Cordero Pérez

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; check LICENSE for details.

  ┬  ┌─┐┌─┐┌┬┐┬┌┐┌┌─┐  ┬  ┬┌┐ ┬─┐┌─┐┬─┐┬┌─┐┌─┐
  │  │ │├─┤ │││││││ ┬  │  │├┴┐├┬┘├─┤├┬┘│├┤ └─┐
  ┴─┘└─┘┴ ┴─┴┘┴┘└┘└─┘  ┴─┘┴└─┘┴└─┴ ┴┴└─┴└─┘└─┘
""")

# Imports
import azure.cognitiveservices.speech as speechsdk
import os
import subprocess
import stanfordnlp
import requests
import shutil # - - This module helps to transfer information from 1 file to another 
from bs4 import BeautifulSoup
from operator import itemgetter, attrgetter, methodcaller
import speech_recognition as sr

# Download models on first run
stanfordnlp.download('en')   # This downloads the English models for the neural pipeline
# Sets up a neural pipeline in English
nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos,lemma,depparse', treebank='en_ewt', use_gpu=False, pos_batch_size=3000) # Build the pipeline, specify part-of-speech processor's batch size


def getSpeech():
  text="Hello"
  return text

#   
def parse(text):
  # Process text input
  doc = nlp(text) # Run the pipeline on text input

  print ("""
  ┌─┐┌─┐┬─┐┌─┐┌─┐┬─┐┌┬┐  ┌┬┐┬─┐┌─┐┌┐┌┌─┐┬  ┌─┐┌┬┐┬┌─┐┌┐┌
  ├─┘├┤ ├┬┘├┤ │ │├┬┘│││   │ ├┬┘├─┤│││└─┐│  ├─┤ │ ││ ││││
  ┴  └─┘┴└─└  └─┘┴└─┴ ┴   ┴ ┴└─┴ ┴┘└┘└─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘
  """)

  for sentence in doc.sentences:
  
    translation = translate(sentence)

    result = []
    for word in translation[0]:
      result.append((word['text'].lower(), word['lemma'].lower()))
    print("\nResult: ", result, "\n")

    print ("""
  ┌─┐┌─┐┬    ┬─┐┌─┐┌─┐┬─┐┌─┐┌─┐┌─┐┌┐┌┌┬┐┌─┐┌┬┐┬┌─┐┌┐┌
  ├─┤└─┐│    ├┬┘├┤ ├─┘├┬┘├┤ └─┐├┤ │││ │ ├─┤ │ ││ ││││
  ┴ ┴└─┘┴─┘  ┴└─└─┘┴  ┴└─└─┘└─┘└─┘┘└┘ ┴ ┴ ┴ ┴ ┴└─┘┘└┘
    """)
    display(translation)

  return doc


# add a word into the dictionary and return dictionary
def wordToDictionary(word):
  dictionary = {
    'index': word.index,
    'governor': word.governor,
    'text': word.text.lower(),
    'lemma': word.lemma.lower(),
    'upos': word.upos,
    'xpos': word.xpos,
    'dependency_relation': word.dependency_relation,
    'feats': word.dependency_relation,
    'children': []
  }
  return dictionary

# order words? for grammar? returns reordered structure
def getMeta(sentence):
  # sentence.print_dependencies()
  englishStruct = {}
  aslStruct = {
    'rootElements':[],
    'UPOS': {
      'ADJ':[], 'ADP':[], 'ADV':[], 'AUX':[], 'CCONJ':[], 'DET':[], 'INTJ':[], 'NOUN':[], 'NUM':[], 'PART':[], 'PRON':[], 'PROPN':[], 'PUNCT':[], 'SCONJ':[], 'SYM':[], 'VERB':[], 'X':[]
    }
  }
  reordered = []
  # aslStruct["rootElements"] = []

  # Make a list of all tokenized words. This step might be unnecessary.
  words = []
  for token in sentence.tokens:
    # print(token)
    for word in token.words:
      
      print(word.index, word.governor, word.text, word.lemma, word.upos, word.dependency_relation) # , word.feats)
      # # Insert as dict
      # words.append(wordToDictionary(word))
      # Insertion sort
      j = len(words)
      for i, w in enumerate(words):
        if word.governor <= w['governor']:
          continue
        else:
          j = i
          break
      # Convert to Python native structure when inserting.
      words.insert(j, wordToDictionary(word))
  # # Python sort for converted words
  # words.sort(key=attrgetter('governor', 'age')) # , reverse=True
  # words.sort(key=words.__getitem__) # , reverse=True
  reordered = words

  # Deprecated aslStruct code...
  # While there exist words that haven't been added to the tree.  
  # englishStruct['root'] = wordToDictionary(words[0])
  #     # Create list of words for each UPOS
  #     aslStruct['UPOS'][word.upos].append(word)
  # 
  # # Sort each UPOS list
  # # print(aslStruct['UPOS'])
  # for upos, uposList in aslStruct['UPOS'].items():
  #   # print(upos, uposList)
  #   uposList.sort(key=attrgetter('governor'))
  #   print(upos, uposList)

  # Identify Root Elements
  # for word in token.words:
    # if word.dependency_relation == "root":
      # aslStruct["rootElements"].append(word)
      # Get related elements
      # Ident topics & comments

  # print("\n", aslStruct, "\n")
  return reordered

# get tone of sequence returns the translation and tone
def getLemmaSequence(meta):
  tone = ""
  translation = []
  for word in meta:
    # Remove blacklisted words
    if (word['text'].lower(), word['lemma'].lower()) not in (('is', 'be'), ('the', 'the'), ('of', 'the'), ('is', 'are'), ('by', 'by'), (',', ','), (';', ';'), (':'), (':')):
      
      # Get Tone: get the sentence's tone from the punctuation
      if word['upos'] == 'PUNCT':
        if word['lemma'] == "?":
          tone = "?"
        elif word['lemma'] == "!":
          tone = "!"
        else:
          tone = ""
        continue
      
      # Remove symbols and the unknown
      elif word['upos'] == 'SYM' or word['upos'] == 'X':
        continue
      
      # Remove particles
      if word['upos'] == 'PART':
        continue

      # Convert proper nouns to finger spell
      elif word['upos'] == 'PROPN':
        fingerSpell = []
        for letter in word['text'].lower():
          print(letter)
          spell = {}
          spell['text'] = letter
          spell['lemma'] = letter
          # Add fingerspell as individual lemmas
          fingerSpell.append(spell)
        print(fingerSpell)
        translation.extend(fingerSpell)
        print(translation)

      # Numbers
      elif word['upos'] == 'NUM':
        fingerSpell = []
        for letter in word['text'].lower():
          spell = {}
          # Convert number to fingerspell
          pass
          # Add fingerspell as individual lemmas
          fingerSpell.append(spell)

      # Interjections usually use alternative or special set of signs
      elif word['upos'] == 'CCONJ':
        translation.append(word)
      
      # Interjections usually use alternative or special set of signs
      elif word['upos'] == 'SCONJ':
        if (word['text'].lower(), word['lemma'].lower() not in (('that', 'that'))):
          translation.append(word)
      
      # Interjections usually use alternative or special set of signs
      elif word['upos'] == 'INTJ':
        translation.append(word)

      # Adpositions could modify nouns
      elif word['upos']=='ADP':
        # translation.append(word)
        pass

      # Determinants modify noun intensity
      elif word['upos']=='DET':
        pass

      # Adjectives modify nouns and verbs
      elif word['upos']=='ADJ':
        translation.append(word)
        # pass

      # Pronouns
      elif word['upos'] == 'PRON' and word['dependency_relation'] not in ('nsubj'):
        translation.append(word)

      # Nouns
      elif word['upos'] == 'NOUN':
        translation.append(word)

      # Adverbs modify verbs, leave for wh questions
      elif word['upos']=='ADV':
        translation.append(word)
      
      elif word['upos']=='AUX':
        pass

      # Verbs
      elif word['upos']=='VERB':
        translation.append(word)

  # translation = tree
  return (translation, tone)

def translate(parse):
  meta = getMeta(parse)
  translation = getLemmaSequence(meta)
  return translation

def get_url():
# # Web URL
  base_Web_url = "https://www.signasl.org/sign/"
# search_word= input('Enter a search word: ' )
  Web_url= base_Web_url + translation
# # Get URL Content
  r = requests.get(Web_url)
# # Parse HTML Code
  soup = BeautifulSoup(r.content, 'html.parser')
# # List of all video tag
  video_tags = soup.findAll('video')
  video_urls = soup.findAll('source')
# #print(video_urls)
  url = []
  for vid in soup.find_all('source'):
      url = vid['src']
  return url

def display(translation, url):
  folder = os.getcwd()
#   filePrefix = folder + "/QuickASL/videos/"
#   # Alter ASL lemmas to match sign's file names.
#   # In production, these paths would be stored at the dictionary's database.
  files = [ filePrefix + word['text'].lower() + "_.mp4" for word in translation[0] ]
  # Run video sequence using the MLT Multimedia Framework
  print("Running command: ", ["melt"] + files)
  process = subprocess.Popen(["melt"] + files + [filePrefix + "black.mp4"], stdout=subprocess.PIPE)
  result = process.communicate()

def main():

  flag = False

  while not flag:
    # Get text
    print ("""
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐┬─┐  ┌─┐┌─┐┌─┐┌─┐┌─┐┬ ┬
  │ ┬├─┤ │ ├─┤├┤ ├┬┘  └─┐├─┘├┤ ├┤ │  ├─┤
  └─┘┴ ┴ ┴ ┴ ┴└─┘┴└─  └─┘┴  └─┘└─┘└─┘┴ ┴
    """)

    tests = [
      # "Where is the bathroom?",
      # "What is your name?",
      # "I'm Javier.",
      # "My name is Javier.",
      # "Bring your computer!",
      # "It's lunchtime!",
      # "Small dogs are cute",
      # "Chihuahuas are cute because they're small."
    ]

    if len(tests) == 0:
      tests = tests + [ getSpeech() ]

    if len(tests[0]) == 0:
      print("No speech detected... Reattempting.")
    else:
      for text in tests:
        print ("""
  ┌─┐┌┐┌┌─┐┬ ┬ ┬┌─┐┌─┐  ┌─┐┌┐┌┌─┐┬  ┬┌─┐┬ ┬
  ├─┤│││├─┤│ └┬┘└─┐├┤   ├┤ ││││ ┬│  │└─┐├─┤
  ┴ ┴┘└┘┴ ┴┴─┘┴ └─┘└─┘  └─┘┘└┘└─┘┴─┘┴└─┘┴ ┴
        """)

        print("Text to process: ", text, "\n")

        parse(text)

        print('\nPress "Enter" to continue or any type anything else to exit.')
        key = input()
        if key != '':
          flag = True

main()