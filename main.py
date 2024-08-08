import json
from os import system
from datetime import date


def abrirMedicamentos():
    mijsonMedi=[]
    with open('medicamentos.json', 'r', encoding='utf=8') as openfile:
        mijsonMedi = json.load(openfile)
    return mijsonMedi

def guardarMedicamentos(data):
    with open('medicamentos.json', 'w', encoding='utf=8') as outfile:
        json.dump(data,outfile)

def abrirVentas():
    mijsonVentas=[]
    with open('ventas.json', 'r', encoding='utf=8') as openfile:
        mijsonVentas = json.load(openfile)
    return mijsonVentas