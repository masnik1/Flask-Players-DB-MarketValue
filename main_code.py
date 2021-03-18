from flask import Flask, render_template, request
from app import buscar_jogador
import pandas as pd
from sql_data import insert_players_values, load_player
from mqtt_queues import send_message_to_checker
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():

    return render_template('index.html', value='')

@app.route("/busca", methods=['POST', 'GET'])

def busca():
    NAME_PLAYER = request.args.get('name')
    TEAM_PLAYER = request.args.get('team')
    string_sender = NAME_PLAYER + ' ' + TEAM_PLAYER

    dataframe = load_player(NAME_PLAYER, TEAM_PLAYER)
    if dataframe.empty:
        try:
            name, age, club, position, market_value = buscar_jogador(NAME_PLAYER, TEAM_PLAYER)
            string_sender = name + ',' + age + ',' + club+ ',' + position  + ',' +market_value
            string_return = send_message_to_checker(string_sender, 'check_player')
            dataframe = load_player(NAME_PLAYER, TEAM_PLAYER)
        except:
            pass
    if dataframe.empty:
        string_return = 'Informações não encontradas'
    else:
        string_return = dataframe.Nome[0] + ', jogador do: ' + dataframe.Clube[0] + ' possui: ' + dataframe.Idade[0] + ' anos' + ', joga de: ' + dataframe.Posição[0] + ' e seu valor de mercado é: ' + dataframe.ValorMercado[0]

    return render_template('index.html', value=string_return)
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)

