'''
    boardGameFinderAPI.py
    Calypso Leonard, Tresa Xavier, YingYing Wang
    Flask API used for a board game finder web app
    for CS 257, Winter 2018.
'''

import flask
import sys
import api_config
import psycopg2
import render_template 


app = Flask(__name__)

@app.route('/')
def prelimPage():
    return render_template('Preliminary Page.html')
    

if __name__ == '__main__':
   app.run(debug = True)