'''
    psycopg2-test.py
    Jeff Ondich, 1 Oct 2013
    Modified by Amy Csizmar Dalal, 24 January 2018

    This is a short example of how to access a PostgreSQL database in Python.
'''

import psycopg2
import getpass

# Get the database login info. *** REPLACE THE DATABASE NAME AND USER WITH YOUR USERNAME ***
database = 'adalal'
user = 'adalal'
password = getpass.getpass()

# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print('Connection error: ', e)
    exit()

# Query the database
try:
    cursor = connection.cursor()
    query = 'SELECT quakedate, quaketime, mag, latitude, longitude, place  FROM earthquakes WHERE mag>7 ORDER BY mag DESC'
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    # An alternative to "for row in cursor.fetchall()" is "for row in cursor". The former
    # brings all the data into memory in your program, while the latter brings data in
    # small pieces (one row at a time, I think, but I haven't verified it yet).

except Exception as e:
    print('Cursor error', e)
    connection.close()
    exit()

connection.close()
