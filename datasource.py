'''
    datasource.py
    Tresa Xavier, Calypso Leonard, Yingying Wang Feb, 6, 2018
    Methods to access our boardgames database.
    Boardgames table created from our 
'''

import psycopg2
import getpass
import random

'''
database = 'xaviert'
user = 'xaviert'
password = 'pencil926ruby'
'''
database = 'wangc2'
user = 'wangc2'
password = 'towel672nose'


# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password, host="localhost")
except Exception as e:
    print('Connection error: ', e)
    exit()

class DataSource:
    # Constructor names may seem gratuitous with inputAge, inputTime and inputCategory 
    # but actually provide helpful context
    # given that age time and category are all terms within our data set 
    # (ex: max_time, min_time, min_age, max_age etc 
    # - felt it was necessary to specify when referring to the users input term 
    
    '''
    def login():
        database = 'xaviert'
        user = 'xaviert'
        password = getpass.getpass()
        try:
            connection = psycopg2.connect(database=database, user=user, password=password)
        except Exception as e:
            print('Connection error: ', e)
            exit()
    '''
    
   ''' def __init__(self, sortType):
        self.sortType = sortType'''
    #Calls for only one criteria
    
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
        min_players, max_players FROM boardgames WHERE min_age <=' + inputAge + 'ORDER BY rank ASC LIMIT 10'
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
        'AND min_players <= ' + numPlayers + ' AND min_age <=' + inputAge + 'ORDER BY rank ASC LIMIT 10'
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
        min_players, max_players FROM boardgames WHERE min_age <=' + inputAge + 'AND max_time >= ' + \
        inputTime + 'AND min_time <= ' + inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query     
    #Age and Category
    def getGamesByAgeAndCategory(self, inputAge, inputCategory):
        inputCategory = str(inputCategory)
        inputAge = str(inputAge)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE min_age <=" + inputAge + " AND mechanic LIKE '%" \
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
        min_players <= " + numPlayers + "AND min_age <=" + inputAge + " AND mechanic LIKE '%" \
        + inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query
        
    #Players, Age, and Time
    def getGamesByPlayersAgeAndTime(self, numPlayers, inputAge, inputTime):
        numPlayers = str(numPlayers)
        inputAge = str(inputAge)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames WHERE max_players >=" + numPlayers + "AND \
        min_players <= " + numPlayers + "AND min_age <=" + inputAge + " AND max_time >= " + inputTime \
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
        min_players, max_players FROM boardgames WHERE min_age <=" + inputAge + " AND mechanic LIKE '%" \
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
        + numPlayers + "AND min_age <=" + inputAge + " AND mechanic LIKE '%" + inputCategory +\
        "%' AND  max_time >= " + inputTime + "AND min_time <= " + inputTime +\
        "ORDER BY rank ASC LIMIT 10"
        return query
    

        
    def getGamesNoCriteria(self):
        query = 'SELECT game_name, avg_time, avg_rating, category, min_age, designer, image_url,\
        min_players, max_players FROM boardgames ORDER BY rank LIMIT 10'
        return query
    
    #This method collects data for the random game button, selecting a random 
    # game from the top 100 ranked games by 
    #choosing a random integer and displaying information for that rank.
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
    
    def search(self, numPlayers, inputAge, inputCategory, inputTime):
        #setting up Boolean values
        noNumPlayer = False
        noInputAge = False
        noInputCategory = False
        noInputTime = False        
        if numPlayers == "":
            noNumPlayer = True
        if inputAge == "":
            noIinputAge = True
            inputAge = 101 #dummy value, no age in the data is larger
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
            
def main():
    #cursor = connection.cursor()
    gameSearch = DataSource()
    #query = gameSearch.getGamesByPlayersAgeAndCategory(2,12,'Card Game')
    #search(self, numPlayers, inputAge, inputCategory, inputTime)
    query = gameSearch.search("4","","Partnership","30")
        
    #cursor.execute(query)
    for row in query:
        print(row)
    exit()
            
if __name__ == "__main__":
    main()
