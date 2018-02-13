'''
    boardGameFinderAPI.py
    Calypso Leonard, Tresa Xavier, YingYing Wang
    Flask API used for a board game finder web app
    for CS 257, Winter 2018.
'''

import flask
from flask import render_template, Flask, request
import sys
import api_config
import psycopg2
import templates
import static
import datasource
import json 

app = flask.Flask(__name__)

info = datasource.DataSource()
#info.login()

@app.route('/')
def prelimPage():
    return render_template('index.html')
'''   
@app.route('/results')
def results():
    return render_template('resultPage.html')
'''

@app.route('/results',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      inputCategory = request.form['Category']
      inputTime = int(request.form['Time'])
      inputAge = request.form['Minimum Age']
      inputNumPlayer = request.form['No. of Players']
      query = info.search(inputNumPlayer, inputAge, inputCategory, inputTime)
      return render_template('results.html',result = query)
          
@app.route('/random', methods = ['POST', 'GET'])
def random():
    query = info.getRandomGame()
    return render_template('results.html', result = query)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    info = datasource.DataSource()
        
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    app.run(debug = True)
