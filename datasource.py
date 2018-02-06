'''
    datasource.py
    Tresa Xavier, Calypso Leonard, Yingying Feb, 6, 2018
    Methods to access our boardgames database.
'''

import psycopg2
import getpass
import random

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
    # The following four methods collect data if either no of players, age, category or maxtime was selected alone
    def getGamesByNumPlayers(self, numPlayers):
            numPlayers = str(numPlayers)
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'ORDER BY rank ASC LIMIT 10'
            return query
    def getGamesByMinAge(self, inputAge):
            inputAge = str(inputAge) 
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE min_age <=' + inputAge + 'ORDER BY rank ASC'
            return query
    def getGamesByCategory(self, category):
            query = 'SELECT game_name, avg_time, rank, mechanic, min_age, designer FROM boardgames WHERE mechanic LIKE ' + ''%' + category + '%'' + 'ORDER BY rank ASC' 
            return query
    def getGamesByMaxTime(self, inputTime):
            inputTime = str(inputTime)
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_time >= ' + inputTime + 'AND min_time <= ' + inputTime + 'ORDER BY rank ASC'
            return query
        
    # The following four methods collect data for 
    # a) no of players w age
    # b) no of players w time
    # c) no of players w category
    def getGamesByPlayersAndAge(self, numPlayers, inputAge):
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + str(numPlayers) + 'AND min_players <= ' + str(numPlayers) + ' AND min_age <=' + str(inputAge) + 'ORDER BY rank ASC LIMIT 10'
            return query
        
    def getGamesByPlayersAndTime(self, numPlayers, inputTime):
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + str(numPlayers) + 'AND min_players <= ' + str(numPlayers) + ' AND max_time >= ' + str(inputTime) + 'AND min_time <= ' + str(inputTime) + 'ORDER BY rank ASC LIMIT 10'
            return query
        
    #def getGamesByPlayersAndCategory:

    # The following four methods collect data for 
    # a) max age w time
    # b) max age w category
    def getGamesByAgeAndTime(self, inputAge, inputTime):
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE min_age <=' + str(inputAge) + 'AND max_time >= ' + str(inputTime) + 'AND min_time <= ' + str(inputTime) + 'ORDER BY rank ASC LIMIT 10'
            return query 
        
    #def getGamesByAgeAndCategory:
    
    
    #This method collects data for random game button
    def getRandomGame(self):
            ranNumber = random.randint(1,60)
            query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE rank =' + str(ranNumber)
            return query
        
    
    #def getGamesByAll(self, numPlayers, inputAge, category, inputTime0):
        #numPlayers = str(numPlayers)
        #inputAge = str(inputAge)
        #inputTime = str(inputTime)
        #query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'AND min_age <=' + inputAge + ' AND mechanic =' + str(category) + 'AND  max_time >= ' + inputTime + 'AND min_time <= ' + inputTime + 'LIMIT 10 ORDER BY rank ASC'
        
# Query the database
def main():
    try:
        cursor = connection.cursor()
        gameSearch = DataSource()
        #query = gameSearch.getRandomGame()
        query = gameSearch.getGamesByCategory('Puzzle')
        #query = gameSearch.getGamesByPlayersAndAge(2,11)
        #query = gameSearch.getGamesByPlayersAndTime(2,60)
        #query = gameSearch.getGamesByAgeAndTime(12,60)
             
        cursor.execute(query)
        
        for row in cursor.fetchall():
            print(row)


    except Exception as e:
        print('Cursor error', e)
        connection.close()
        exit()

    connection.close()
    
    
if __name__ == "__main__":
    main()
