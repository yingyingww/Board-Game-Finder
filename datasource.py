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
    # The following four methods collect data if  numPlayers, age, category or maxtime was selected alone
    # Just Players
	def getGamesByNumPlayers(self, numPlayers):
		numPlayers = str(numPlayers)
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'ORDER BY rank ASC LIMIT 10'
		return query
	#Just Age
	def getGamesByMinAge(self, inputAge):
		inputAge = str(inputAge) 
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE min_age <=' + inputAge + 'ORDER BY rank ASC'
		return query
	#Just Category
	def getGamesByCategory(self, inputCategory):
		query = "SELECT game_name, avg_time, rank, mechanic, min_age, designer FROM boardgames WHERE mechanic LIKE '%" + inputCategory + "%' ORDER BY rank ASC"
		return query
    #Just Time
	def getGamesByMaxTime(self, inputTime):
		inputTime = str(inputTime)
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_time >= ' + inputTime + 'AND min_time <= ' + inputTime + 'ORDER BY rank ASC'
		return query
	#Players and Age
	def getGamesByPlayersAndAge(self, numPlayers, inputAge):
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + str(numPlayers) + 'AND min_players <= ' + str(numPlayers) + ' AND min_age <=' + str(inputAge) + 'ORDER BY rank ASC LIMIT 10'
		return query
        #players and Time
	def getGamesByPlayersAndTime(self, numPlayers, inputTime):
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + str(numPlayers) + 'AND min_players <= ' + str(numPlayers) + ' AND max_time >= ' + str(inputTime) + 'AND min_time <= ' + str(inputTime) + 'ORDER BY rank ASC LIMIT 10'
		return query
        #players and Category
	def getGamesByPlayersAndCategory(self, numPlayers, inputCategory):
		numPlayers = str(numPlayers)
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + ' AND mechanic LIKE '%" + inputCategory + "%' LIMIT 10 ORDER BY rank ASC'
	#category and Time
	def getGamesByCategoryAndTime(self, inputCategory, inputTime):
		inputTime = str(inputTime)
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE mechanic LIKE '%" + inputCategory + "%' AND  max_time >= ' + inputTime + 'AND min_time <= ' + inputTime + 'LIMIT 10 ORDER BY rank ASC'

    # The following four methods collect data for 
    # a) max age w time
    # b) max age w category

	# Age and time
	def getGamesByAgeAndTime(self, inputAge, inputTime):
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE min_age <=' + str(inputAge) + 'AND max_time >= ' + str(inputTime) + 'AND min_time <= ' + str(inputTime) + 'ORDER BY rank ASC LIMIT 10'
		return query 
        #Age and Category
    #def getGamesByAgeAndCategory(self, inputAge, inputCategory):
	#players, age, category
    #def getGamesByPlayersAgeAndCategory:
	#players, age, time
    #def getGamesByPlayersAgeAndTime:
	#players, category, time
    #def getGamesByPlayersCategoryAndTime:
	#age, category, time
    #def getGamesByAgeCategoryAndTime():
    
    #This method collects data for random game button
	def getRandomGame(self):
		ranNumber = random.randint(1,60)
		query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE rank =' + str(ranNumber)
		return query
        
    #all criteria
	def getGamesByAll(self, numPlayers, inputAge, inputCategory, inputTime):
		numPlayers = str(numPlayers)
		inputAge = str(inputAge)
		inputTime = str(inputTime)
		query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=" + numPlayers + "AND min_players <= " + numPlayers + "AND min_age <=" + inputAge + " AND mechanic LIKE '%" + inputCategory + "%' AND  max_time >= " + inputTime + "AND min_time <= " + inputTime + "LIMIT 10 ORDER BY rank ASC"
	    	return query
        
# Query the database
def main():
    try:
        cursor = connection.cursor()
        gameSearch = DataSource()
        query = gameSearch.getGamesByAll(4,14,'Area Control',100)
        #query = gameSearch.getGamesByCategory('Puzzle')
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
