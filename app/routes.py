from flask_restful import Resource
from flask import request

from flask import Flask
import requests
from bs4 import BeautifulSoup

VAR_NAME = 'gabigol'

def buscar_jogador(NAME_PLAYER, TEAM_PLAYER):
    url = f'https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=+{VAR_NAME}&x=0&y=0'

    html =  requests.get(
        url, headers={"User-Agent": "Custom"}
    )
    bs = BeautifulSoup(html.content, "html.parser")
    table = bs.find("table", class_ = "items")

    lista_infos = []
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            print(td.find(text=True))
            lista_infos.append(td.find(text=True))

    name = lista_infos[0]
    age = lista_infos[6]
    club = lista_infos[3]
    position = lista_infos[4]
    market_value = lista_infos[8]



    return name, age, club, position, market_value

