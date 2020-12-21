# INFSCI_2710_Project
* MySQL setup instructions

  * create schema using the file app/ddl_statements.sql

  * edit line 10 in config.py to have the name of your mySQL username, password and schema name (SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:5Qf*6*oD@localhost/SmartPharm')

  * make sure the mysql server is running

* Application Run Instructions

  * install python3.6 or higher

  * install poetry (follow instructions here and add to path: https://python-poetry.org/docs/ )

  * from the base project folder: poetry install 

  * from the base project folder: poetry shell 

  * inside the shell: flask run 

  * open the link created in a browser (set to http://127.0.0.1:5000/)

* Still working on getting Heroku to work but the host url is: https://smartpharm-infsci2710.herokuapp.com/