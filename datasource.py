'''
    psycopg2-test.py
    Jeff Ondich, 1 Oct 2013
    Modified by Amy Csizmar Dalal, 24 January 2018
    This is a short example of how to access a PostgreSQL database in Python.
'''

import psycopg2
import getpass

# Get the database login info. 
database = 'xaviert'
user = 'xaviert'
password = getpass.getpass()

# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print('Connection error: ', e)
    exit()

class DataSource:
    
    
    def getGamesByNumPlayers(self, numPlayers):
        numPlayers = str(numPlayers)
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'ORDER BY rank ASC'
        return query
    
    
    def getGamesByMinAge(self, inputAge):
        inputAge = str(inputAge) 
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE min_age <=' + inputAge + 'ORDER BY rank ASC'
        return query
        
        
    def getGamesByCategory(self, category):
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'ORDER BY rank ASC'
        return query
    
    def getGamesByMaxTime(self, inputTime):
        inputTime = str(inputTime)
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_time >= ' + inputTime + 'AND min_time <= ' + inputTime + 'ORDER BY rank ASC'
        return query
  
# Query the database
def main():
    try:
        cursor = connection.cursor()
        gameSearch = DataSource()
        query = gameSearch.getGamesByNumPlayers(4);
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
   
if __name__ == "__main__":
    main()
