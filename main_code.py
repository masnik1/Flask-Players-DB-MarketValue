from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from app import buscar_jogador
import pandas as pd
from sql_data import insert_players_values, load_player
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route("/")
def home():

    return render_template('index.html', value='')

@app.route("/busca", methods=['POST', 'GET'])

def busca():
    NAME_PLAYER = request.args.get('name')
    TEAM_PLAYER = request.args.get('team')
    
    dataframe = load_player(NAME_PLAYER, TEAM_PLAYER)
    if dataframe.empty:
        try:
            name, age, club, position, market_value = buscar_jogador(NAME_PLAYER, TEAM_PLAYER)
            insert_players_values(name, age, club, position, market_value)
            dataframe = load_player(NAME_PLAYER, TEAM_PLAYER)
        except:
            pass
        if dataframe.empty:
            string_return = 'Informações não encontradas'
        else:
            string_return = dataframe.Nome[0] + ', jogador do: ' + dataframe.Clube[0] + ' possui: ' + dataframe.Idade[0] + ' anos' + ', joga de: ' + dataframe.Posição[0] + ' e seu valor de mercado é: ' + dataframe.ValorMercado[0]

    return render_template('index.html', value=string_return)
    
if __name__ == "__main__":
    app.run(debug=True)

