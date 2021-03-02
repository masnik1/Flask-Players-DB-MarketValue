from flask import Flask
import requests
from bs4 import BeautifulSoup
from app import buscar_jogador
import pandas as pd
from sql_data import insert_players_values, load_player
app = Flask(__name__)
NAME_PLAYER = 'Gabriel Barbosa'
TEAM_PLAYER = 'fla'

@app.route("/")
def home():

    return 'Página Inicial'

@app.route("/busca")
def busca():
    
    dataframe = load_player(NAME_PLAYER)
    name, age, club, position, market_value = buscar_jogador(NAME_PLAYER, TEAM_PLAYER)
    insert_players_values(name, age, club, position, market_value)

    return name
    
if __name__ == "__main__":
    app.run(debug=True)