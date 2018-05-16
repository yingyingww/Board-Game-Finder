# Board Game Finder

Our project is currently a fully functional web app which accepts up to four criteria and searches a large database to 
return a set of board games which fit the input requirements. Users can search on the basis of the number of players, length
of play, type of gameplay, and suitable age, or using any combination of these.

## Features:
-A homepage with a set of drop-down menus and a bar which only accepts numbers as input which allows the user
to input their preferences.
-A results page which shows users 10 games which relevant information such as name, number of players, and category,
as well as a photo of the game's cover art.
-A random-game selector which displays data for a random game in top 100 ranked games.
-An About page, which describes in greater detail what each criterion entails.

## Files in this repository
This repo contains code for the database-driven web project. It consists of the following files:

createtable.sql: A Python script used to create a database and set up the table(s), including table columns and types.

boardGames.csv: A comma-space delimited text file containing data on 5000 board games from the website boardgamegeek.com. We retrieved this [data](https://www.kaggle.com/mrpantherson/board-game-data) from a user's post on Kaggle.com, on which it is listed as available for projects. 

[web project D] Project Plan Assignment.pdf: A pdf file outlining the initial goals and format of our project.

boardGameFinderAPI.py: A Python script which transmits search information from the HTML to our SQL queries using Flask.

datasource.py: A Python script which creates strings for SQL queries based on which criteria are selected by the user.

psycopg-2.py: A Python script that executes SQL queries using the psycopg2 library.


Templates folder:

index.html: An HTML file of the homepage for our web app, which allows users to input specific criteria to search the 
database for different board games

results.html: An HTML file which displays the game data retrieved from the SQL query.

noResults.html: An HTML file which displays no result found with chosen criteria to the user 

about.html: An HTML file which displays the purpose of this game finder and explains how it works


Static folder:

prelim.css: A css file containing the styling basis for our web app.

## Author:
* Yingying Wang
* Calypso Leonard
* Tresa Xavier

## Screenshots:
![alt text](screenshots/home.png "home")
