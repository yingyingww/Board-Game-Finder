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
	def getGamesByCriteria(self, numPlayers, inputAge, category, inputTime):
		select_clause = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames'
		
		if numPlayers == "N/A" and inputAge == "N/A" and category == "N/A" and inputTime == "N/A":
			where_clause = ''
		else: where_clause = ' WHERE '
		
		if (numPlayers!= "N/A"):
			where_clause = 'WHERE' + getNumPlayersWhere(numPlayers)
			if (inputAge!= "N/A"):
				where_clause = where_clause + 'AND' + getMinAgeWhere(inputAge)
			if(category!= "N/A"):
				where_clause = where_clause + 'AND' + getCategoryWhere(category)
			if(inputTime!= "N/A"):
				where_clause = where_clause + 'AND' + getTimeWhere(inputTime)

		elif (inputAge!= "N/A"):
			where_clause = 'WHERE' + getMinAgeWhere(inputAge)
			if(category!= "N/A"):
				where_clause = where_clause + 'AND' + getCategoryWhere(category)
			if(inputTime!= "N/A"):
				where_clause = where_clause + 'AND' + getTimeWhere(inputTime)
		
		elif (category!= "N/A"):
			where_clause = 'WHERE' + getCategoryWhere(category)
			if(inputTime!="N/A"):
				where_clause = where_clause + 'AND' + getTimeWhere(inputTime)
		else:
			where_clause = 'WHERE ' + getTimeWhere(inputTime)
			
		query = select_clause + where_clause + ' ORDER BY rank ASC LIMIT 10'
		return query
		
	
	def getNumPlayersWhere(self, numPlayers):
		where = 'max_players >= ' + str(numPlayers) + ' AND min_players <= ' + str(numPlayers) 
		return where
	def getMinAgeWhere(self, inputAge):
		where = 'min_age <= ' + str(inputAge) 
		return where
    	
	def getCategoryWhere(self, category):
		where = 'mechanic = ' + str(category) 
		return where
    	
	def getTimeWhere(self, inputTime):
		where = 'max_time >= ' + inputTime + ' AND min_time <= ' + inputTime  
		return where
	def getGamesByNumPlayers(self, numPlayers):
        	numPlayers = str(numPlayers)
        	query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' + numPlayers + 'ORDER BY rank ASC LIMIT 10'
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
        
  
	def getRandomGame(self, RanNumber):
        	query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames WHERE rank =' + str(RanNumber)
        
        
# Query the database
def main():
    try:
        cursor = connection.cursor()
        gameSearch = DataSource()
        query = gameSearch.getGamesByCriteria(4,11,"N/A", 60);
        	 
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
