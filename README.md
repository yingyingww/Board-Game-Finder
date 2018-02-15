Our project is currently a fully functional web app which accepts up to four criteria and searches a large database to 
return a set of boardgames which fit the input requirements. Users can search on the basis of number of players, length
of play, type of gameplay, and suitable age, or using any combination of these.

Features:
-A homepage with a set of dropdown menus and a bar which only accepts numbers as input which allow the user
to input their preferences.
-A results page which shows users 10 games which relevant information such as name, number of players, and category,
as well as a photo of the game's cover art.
-A random-game selector which displays data for a random game in top 100 ranked games.
-An About page, which describes the in greater detail what each criteria entails.


In order to execute the web page, users begin at the home page, on which they select or type in criteria for any, all,
or none or the possible filtering mechanisms. They are then taken to the results page, which shows them up to 10 games 
with their selected features. Users can then use the navigation bar to find a different set of games. If they would
prefer, users can also execute using the 'random game' button, which displays a single random game.

One feature we would have liked to implement is a way in change the sorting mechanism on the results page. This feature 
would have allowed users to select sorting type, for instance by length of play, when viewing their results. Currently,
our project only orders resulting games by rank.

We retrieved our data from a user's post on Kaggle.com, on which it is listed as available for projects. 
Link to data: https://www.kaggle.com/mrpantherson/board-game-data




# Board-Games-web-project
This repo contains code for the database-driven web project. It consists of the following files:

createtable.sql: A Python script used to create a database and set up the table(s), including table columns and types.

boardGames.csv: A comma-space delimited text file containing data on 5000 board games from the website boardgamegeek.com. We retrieved this data from a user's post on Kaggle.com, on which it is listed as available for projects. 
Link to data: https://www.kaggle.com/mrpantherson/board-game-data

[web project D] Project Plan Assignment.pdf: A pdf file outlining the inital goals and format of our project.

boardGameFinderAPI.py: A Python script which transmits search information from the HTML to our SQL queries using Flask.

datasource.py: A Python script which creates strings for SQL queries based on which criteria are selected by the user.


psycopg-2.py: A Python script that executes SQL queries using the psycopg2 library.

Templates folder:

index.html: An HTML file of the homepage for our web app, which allows users to input specific criteria to search the 
database for different board games

results.html: An HTML file which displays the game data retieved from the SQL query.

noResults.html: An HTML file which displays no result found with chosen criteria to the user 

about.html: An HTML file which displays the purpose of this game finder and explains how it works


Static folder:

prelim.css: A css file containing the style basis for our web app.

