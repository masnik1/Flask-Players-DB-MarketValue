import os

import mysql.connector
import numpy as np
import pandas as pd
import sqlalchemy

PASSWORD_DB = ''
HOST_DB = 'localhost'
PORT_DB = '3306'
TABLENAME_PLAYERS = 'players_tmk_database'

def insert_players_values(name, age, club, position, market_value):
    Y = pd.DataFrame(data = {'Nome': [name], 'Idade': [age], 'Posição': [position], 'Clube': [club], 'ValorMercado': [market_value]})
    engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{TABLENAME_PLAYERS}')
    Y.to_sql(name='players', con=engine,if_exists='append', index=False)

def load_player(player_name, team_name):
    engine = sqlalchemy.create_engine(f'mysql+pymysql://root:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/{TABLENAME_PLAYERS}')
    dbConnection = engine.connect()

    Y = pd.read_sql(f"select * from players_tmk_database.players WHERE Nome = '{player_name}' ", dbConnection)

    pd.set_option('display.expand_frame_repr', False)

    dbConnection.close()

    return Y