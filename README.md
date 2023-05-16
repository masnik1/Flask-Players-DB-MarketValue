<p align="center">
  <img src="https://raw.githubusercontent.com/masnik1/Flask-Players-MarketValue-Web-Scrapper/main/ProjectLogo.png">
</p>

# 📁 About the project

The project is designed to build using Flask, on building a application to check football players market value.
The application uses the Pika technology, which is an implementation of the RabbitMQ protocol, the goal of this project was to work as a receiver of an MQTT thread, and receive the searched data using this technology.

First, we can search on a local database(SQLAlchemy) the player name and club and return infos about his age, position and market value. 
If the player isn't on the local database, we will do an web scraping on https://www.transfermarkt.com/, which is the most trusted website for footballers informations about marketcap of them and also stats for almost every professional league in the planet. 
Later we use the player name and club to adquire it's values (age, position and market value), then store it in the database.

# Technologies used

SQL Alchemy - https://www.sqlalchemy.org/
Pika for MQTT transactions - https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-rabbitmq-pika.html

