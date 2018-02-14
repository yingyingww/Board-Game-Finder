'''
    datasource.py
    Tresa Xavier, Calypso Leonard, Yingying Wang 
    Feb. 14th, 2018
    SQL Methods to access our boardgames database 
    and create queries.
'''

import psycopg2
import getpass
import random

# Login to the database
database = 'wangc2'
user = 'wangc2'
password = 'towel672nose'

try:
    connection = psycopg2.connect(database=database, user=user, password=password, host="localhost")
except Exception as e:
    print('Connection error: ', e)
    exit()

# DataSource class to create queries based on certain criteria
class DataSource:
    
    
    # Each of the following methods creates a string SQL query based on input search criteria.
    # Parameters are the user's input criteria, of which there may be up to 4.
    # The string query filters to ensure the games presented have the correct number of players, 
    # are appropriate for the selected age, will not take more than the selected maximum time, 
    # and fall into the user's selected category.
    # If any feature was not selected, it is not used to filter the search.
    
    #Calls for only one criterion
    
    # Just Players
    def getGamesByNumPlayers(self, numPlayers):
        numPlayers = str(numPlayers)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=' + numPlayers + 'AND min_players <= ' \
        + numPlayers + 'ORDER BY rank ASC LIMIT 10'
        return query
    
    #Just Age
    def getGamesByMinAge(self, inputAge):
        inputAge = str(inputAge)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE min_age >=' + inputAge + 'ORDER BY rank ASC LIMIT 10'
        return query
    #Just Category
    def getGamesByCategory(self, inputCategory):
        inputCategory = str(inputCategory)
        query = "SELECT game_name, avg_time, avg_rating, mechanic, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE mechanic LIKE '%" + inputCategory + "%' \
        ORDER BY rank ASC LIMIT 10"
        return query
    #Just Time
    def getGamesByMaxTime(self, inputTime):
        inputTime = str(inputTime)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_time >= ' + inputTime + 'AND min_time <= ' \
        + inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query
    
    #Calls for combinations of two criteria
        
    #Players and Age
    def getGamesByPlayersAndAge(self, numPlayers, inputAge):
        inputAge = str(inputAge)
        numPlayers = str(numPlayers)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=' + numPlayers + \
        'AND min_players <= ' + numPlayers + ' AND min_age >=' + inputAge + 'ORDER BY rank ASC LIMIT 10'
        return query
    #Players and Time
    def getGamesByPlayersAndTime(self, numPlayers, inputTime):
        inputTime = str(inputTime)
        numPlayers = str(numPlayers)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=' + numPlayers + \
        'AND min_players <= ' + numPlayers + ' AND max_time >= ' + inputTime + 'AND min_time <= '\
        + inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query
    #Players and Category
    def getGamesByPlayersAndCategory(self, numPlayers, inputCategory):
        numPlayers = str(numPlayers)
        inputCategory = str(inputCategory)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + \
        "AND min_players <= " + numPlayers + " AND mechanic LIKE '%" + inputCategory + \
        "%' ORDER BY rank ASC LIMIT 10"
        return query
    #Category and Time
    def getGamesByCategoryAndTime(self, inputCategory, inputTime):
        inputTime = str(inputTime)
        inputCategory = str(inputCategory)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE mechanic LIKE '%" + inputCategory + "%' AND  \
        max_time >= " + inputTime + "AND min_time <= " + inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
    # Age and Time
    def getGamesByAgeAndTime(self, inputAge, inputTime):
        inputTime = str(inputTime)
        inputAge = str(inputAge)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE min_age >=' + inputAge + 'AND max_time >= ' + \
        inputTime + 'AND min_time <= ' + inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query     
    #Age and Category
    def getGamesByAgeAndCategory(self, inputAge, inputCategory):
        inputCategory = str(inputCategory)
        inputAge = str(inputAge)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE min_age >=" + inputAge + " AND mechanic LIKE '%" \
        + inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query
        
     #Calls for combinations of three criteria
    
    #Players, Age, and Category
    def getGamesByPlayersAgeAndCategory(self, numPlayers, inputAge, inputCategory):
        numPlayers = str(numPlayers)
        inputAge = str(inputAge)
        inputCategory = str(inputCategory)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + "AND \
        min_players <= " + numPlayers + "AND min_age >=" + inputAge + " AND mechanic LIKE '%" \
        + inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query
        
    #Players, Age, and Time
    def getGamesByPlayersAgeAndTime(self, numPlayers, inputAge, inputTime):
        numPlayers = str(numPlayers)
        inputAge = str(inputAge)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + "AND \
        min_players <= " + numPlayers + "AND min_age >=" + inputAge + " AND max_time >= " + inputTime \
        + "AND min_time <= " + inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
        
    #Players, Category, and Time
    def getGamesByPlayersCategoryAndTime(self, numPlayers, inputCategory, inputTime):
        numPlayers = str(numPlayers)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + "AND min_players <= " \
        + numPlayers + " AND mechanic LIKE '%" + inputCategory + "%' AND  max_time >= " \
        + inputTime + "AND min_time <= " + inputTime + "ORDER BY rank ASC LIMIT 10"
        return query    
        
    #Age, Category, and Time
    def getGamesByAgeCategoryAndTime(self,inputAge,inputCategory,inputTime):
        inputAge = str(inputAge)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE min_age >=" + inputAge + " AND mechanic LIKE '%" \
        + inputCategory + "%' AND  max_time >= " + inputTime + "AND min_time <= " \
        + inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
    
    #Call for a query using all criteria
    def getGamesByAll(self, numPlayers, inputAge, inputCategory, inputTime):
        numPlayers = str(numPlayers)
        inputAge = str(inputAge)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + "AND min_players <= "\
        + numPlayers + "AND min_age >=" + inputAge + " AND mechanic LIKE '%" + inputCategory +\
        "%' AND  max_time >= " + inputTime + "AND min_time <= " + inputTime +\
        "ORDER BY rank ASC LIMIT 10"
        return query
    
    #If no input
    def getGamesNoCriteria(self):
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames ORDER BY rank LIMIT 10'
        return query
    
    # This method creates a string query which selects a random 
    # game from the top 100 ranked games 
    
    def getRandomGame(self):
        ranNumber = random.randint(1,101)
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players  FROM boardgames WHERE rank =' + str(ranNumber)
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
            
        except Exception as e:
            print('Cursor error', e)
            connection.close()
            exit()
            
    # This method determines which getter funciton is to be used in search
    def selectFuntion(self, numPlayers, inputAge, inputCategory, inputTime):
        #setting up Boolean values
        noNumPlayer = False
        noInputAge = False
        noInputCategory = False
        noInputTime = False        
        if numPlayers == "":
            noNumPlayer = True
        if inputAge == "":
            noIinputAge = True
            inputAge = 0 #dummy value, no age in the data is smaller
        if inputCategory == "":
            noInputCategory = True
        if inputTime == "":
            noInputTime = True      
        #determine which criteria to use    
        if not noNumPlayer and not noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByAll(numPlayers, inputAge, inputCategory, inputTime)
        if noNumPlayer and not noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByAgeCategoryAndTime(inputAge,inputCategory,inputTime)
        if not noNumPlayer and noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByPlayersCategoryAndTime(numPlayers, inputCategory, inputTime)
        if not noNumPlayer and not noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByPlayersAgeAndTime(numPlayers, inputAge, inputTime)
        if not noNumPlayer and not noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByPlayersAgeAndCategory(numPlayers, inputAge, inputCategory) 
        if noNumPlayer and not noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByAgeAndCategory(inputAge, inputCategory)
        if noNumPlayer and not noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByAgeAndTime(inputAge, inputTime)
        if noNumPlayer and noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByCategoryAndTime(inputCategory, inputTime)
        if not noNumPlayer and noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByPlayersAndCategory(numPlayers, inputCategory)
        if not noNumPlayer and noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByPlayersAndTime(numPlayers, inputTime) 
        if not noNumPlayer and not noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByPlayersAndAge(numPlayers, inputAge)
        if noNumPlayer and noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByMaxTime(inputTime)
        if noNumPlayer and noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByCategory(inputCategory)
        if noNumPlayer and not noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByMinAge(inputAge) 
        if not noNumPlayer and noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByNumPlayers(numPlayers)
        if noNumPlayer and noInputAge and noInputCategory and noInputTime:
            action = self.getGamesNoCriteria()  
        return action
    
    #Selects and executes SQL search
    def search(self, numPlayers, inputAge, inputCategory, inputTime):
        
        action = selectFunction(numPlayers, inputAge, inputCategory, inputTime)
            
        try:
            cursor = connection.cursor()
            cursor.execute(action)
            if cursor.rowcount == 0:
                action = "Sorry! No games found"
                return action
            else:                
                return cursor.fetchall()
            
        except Exception as e:
            print('Cursor error', e)
            connection.close()
            exit()
            

