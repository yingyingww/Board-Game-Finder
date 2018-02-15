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

# DataSource class to create and execute queries based on certain criteria
class DataSource:
    
    def __init__(self, numPlayers, inputAge, inputCategory, inputTime):
        self.numPlayers = str(numPlayers)
        self.inputAge = str(inputAge)
        self.inputCategory = inputCategory
        self.inputTime = str(inputTime)
        
    # Each of the following methods creates a string SQL query based on input search criteria.
    # The string query filters to ensure the games presented have the correct number of players, 
    # are appropriate for the selected age, will last the correct length of time, 
    # and fall into the user's selected category.
    # If any feature was not selected, it is not used to filter the search.
    
    #Calls for only one criterion

    def getGamesByNumPlayers(self):
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=' + self.numPlayers + 'AND min_players <= ' \
        + self.numPlayers + 'ORDER BY rank ASC LIMIT 10'
        return query

    def getGamesByMinAge(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE min_age >=' + self.inputAge + 'ORDER BY rank ASC LIMIT 10'
        return query

    def getGamesByCategory(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE mechanic LIKE '%" + self.inputCategory + "%' \
        ORDER BY rank ASC LIMIT 10"
        return query

    def getGamesByMaxTime(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_time >= ' + self.inputTime + 'AND min_time <= ' \
        + self.inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query
    
    #Calls for combinations of two criteria

    def getGamesByPlayersAndAge(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=' + self.numPlayers + \
        'AND min_players <= ' + self.numPlayers + ' AND min_age >=' + self.inputAge + 'ORDER BY rank ASC LIMIT 10'
        return query

    def getGamesByPlayersAndTime(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=' + self.numPlayers + \
        'AND min_players <= ' + self.numPlayers + ' AND max_time >= ' + self.inputTime + 'AND min_time <= '\
        + self.inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query

    def getGamesByPlayersAndCategory(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=" + self.numPlayers + \
        "AND min_players <= " + self.numPlayers + " AND mechanic LIKE '%" + self.inputCategory + \
        "%' ORDER BY rank ASC LIMIT 10"
        return query

    def getGamesByCategoryAndTime(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE mechanic LIKE '%" + self.inputCategory + "%' AND  \
        max_time >= " + self.inputTime + "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query

    def getGamesByAgeAndTime(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE min_age >=' + self.inputAge + 'AND max_time >= ' + \
        self.inputTime + 'AND min_time <= ' + self.inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query     

    def getGamesByAgeAndCategory(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE min_age >=" + self.inputAge + "\
        AND mechanic LIKE '%" + self.inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query
        
     #Calls for combinations of three criteria

    def getGamesByPlayersAgeAndCategory(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=" + self.numPlayers + "AND \
        min_players <= " + self.numPlayers + "AND min_age >=" + self.inputAge + " AND mechanic LIKE '%" \
        + self.inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query

    def getGamesByPlayersAgeAndTime(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=" + self.numPlayers + "AND \
        min_players <= " + self.numPlayers + "AND min_age >=" + self.inputAge + " AND max_time >= " + self.inputTime \
        + "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query

    def getGamesByPlayersCategoryAndTime(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=" + self.numPlayers + "AND min_players <= " \
        + self.numPlayers + " AND mechanic LIKE '%" + self.inputCategory + "%' AND  max_time >= " \
        + self.inputTime + "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query    

    def getGamesByAgeCategoryAndTime(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE min_age >=" + self.inputAge + " AND mechanic LIKE '%" \
        + self.inputCategory + "%' AND  max_time >= " + self.inputTime + "AND min_time <= " \
        + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
    
    #Call for a query using all criteria
    def getGamesByAll(self):
        query = "SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE max_players >=" + self.numPlayers + "AND min_players <= "\
        + self.numPlayers + "AND min_age >=" + self.inputAge + " AND mechanic LIKE '%" + self.inputCategory +\
        "%' AND  max_time >= " + self.inputTime + "AND min_time <= " + self.inputTime +\
        "ORDER BY rank ASC LIMIT 10"
        return query
    
    #If no input
    def getGamesNoCriteria(self):
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames ORDER BY rank LIMIT 10'
        return query
    
    # This method creates a string query which selects a random 
    # game from the top 100 ranked games 
    
    def getRandomGame(self):
        ranNumber = random.randint(1,101)
        query = 'SELECT game_name, min_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players, max_time FROM boardgames WHERE rank =' + str(ranNumber)
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
            
        except Exception as e:
            print('Cursor error', e)
            connection.close()
            exit()
            
    # This method determines which getter funciton is to be used in search
    def selectFunction(self):
        action = self.getGamesByAll() #failsafe in case no if statement is entered
        #setting up Boolean values
        noNumPlayer = False
        noInputAge = False
        noInputCategory = False
        noInputTime = False        
        if self.numPlayers == "":
            noNumPlayer = True
        if self.inputAge == "":
            noIinputAge = True
            self.inputAge = str(0) #dummy value, no age in the data is smaller
        if self.inputCategory == "":
            noInputCategory = True
        if self.inputTime == "":
            noInputTime = True      
        #determine which criteria to use    
        if not noNumPlayer and not noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByAll()
        if noNumPlayer and not noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByAgeCategoryAndTime()
        if not noNumPlayer and noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByPlayersCategoryAndTime()
        if not noNumPlayer and not noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByPlayersAgeAndTime()
        if not noNumPlayer and not noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByPlayersAgeAndCategory() 
        if noNumPlayer and not noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByAgeAndCategory()
        if noNumPlayer and not noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByAgeAndTime()
        if noNumPlayer and noInputAge and not noInputCategory and not noInputTime:
            action = self.getGamesByCategoryAndTime()
        if not noNumPlayer and noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByPlayersAndCategory()
        if not noNumPlayer and noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByPlayersAndTime() 
        if not noNumPlayer and not noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByPlayersAndAge()
        if noNumPlayer and noInputAge and noInputCategory and not noInputTime:
            action = self.getGamesByMaxTime()
        if noNumPlayer and noInputAge and not noInputCategory and noInputTime:
            action = self.getGamesByCategory()
        if noNumPlayer and not noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByMinAge() 
        if not noNumPlayer and noInputAge and noInputCategory and noInputTime:
            action = self.getGamesByNumPlayers()
        if noNumPlayer and noInputAge and noInputCategory and noInputTime:
            action = self.getGamesNoCriteria()  
        return action
    
    #Selects and executes SQL search
    def search(self):
        action = self.selectFunction()
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
            

