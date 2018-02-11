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
import templates
import static
import datasource  

app = Flask(__name__)

info = datasource.DataSource()
info.login()

@app.route('/')
def prelimPage():
    return render_template('Preliminary Page.html')
    
@app.route('/results')
#def results():

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
        exit()
    info = datasource.DataSource()
    info.login()
    info.getRandomGame()
        
    host = sys.argv[1]
    port = sys.argv[2]
    app.run(host=host, port=port)

   app.run(debug = True)
