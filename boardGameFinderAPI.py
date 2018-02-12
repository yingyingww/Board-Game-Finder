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

app = flask.Flask(__name__)

info = datasource.DataSource()
#info.login()

@app.route('/')
def prelimPage():
    return render_template('Preliminary Page.html')
'''   
@app.route('/results')
def results():
    return render_template('resultPage.html')
'''

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.get('Category')
      cursor = connection.cursor()
      gameSearch = DataSource()
      query = gameSearch.getGamesByCategory(result) 
      final_query = cursor.execute(query)
      return result
      #return render_template("results.html",result = result)
    
@app.route('/random')
def random():
    return render_template('resultPage.html')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    info = datasource.DataSource()
    info.result()
        
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

    app.run(debug = True)
