import json
from os import system
from datetime import date

#Medicamentos
def abrirMedicamentos():
    mijsonMedi=[]
    with open('medicamentos.json', 'r', encoding='utf=8') as openfile:
        mijsonMedi = json.load(openfile)
    return mijsonMedi

def guardarMedicamentos(dataMedi):
    with open('medicamentos.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataMedi,outfile)
#ventas
def abrirVentas():
    mijsonVentas=[]
    with open('ventas.json', 'r', encoding='utf=8') as openfile:
        mijsonVentas = json.load(openfile)
    return mijsonVentas

def guardarVentas(dataVen):
    with open('ventas.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataVen,outfile)
#Compras
def abrirCompras():
    mijsonCompras=[]
    with open('compras.json', 'r', encoding='utf=8') as openfile:
        mijsonCompras = json.load(openfile)
    return mijsonCompras

def guardarCompras(dataCom):
    with open('compras.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataCom,outfile)


#Inicio
        
generalTodo = True

while generalTodo == True:
    generalVen=abrirVentas()
    booleanoMenu = True

    while booleanoMenu == True:
        print("---------------------------------")
        print("            FARMACIA             ")
        print("---------------------------------") 

        try:
            seleccion = int(input("Ver Productos 1: \nVentas 2: \nCompras 3:  \nVer Ventas Realizadas 4: \nVer Compras Realizadas 5: \nIngrese opcion:"))
            
            booleanoMenu = False
        except ValueError:
            input("ingrese un valor valido")
            system("cls")

    if seleccion == 2:
        
        generalVen=abrirVentas()
        for i in generalVen[0]["Ventas"]:
            fecha = date.today()
            fe = fecha.isoformat()
            paciente = input("ingrese el nombre del paciente: ")
            direccion = input("Ingrese la direccion del paciente: ")
            empleado = input("Ingrese el nombre del empleado: ")
            cargo = input("ingrese el cargo del empleado: ")
            generalVen=abrirVentas()
            generalVen[0]["Ventas"].append({
                "fechaVenta": fe,
        "paciente": {
            "nombre": paciente,
            "direccion": direccion
        },
        "empleado": {
            "nombre": empleado,
            "cargo": cargo
        },
        "medicamentosVendidos": [
            {
                "nombreMedicamento": "Paracetamol",
                "cantidadVendida": 2,
                "precio": 20
            }
        ]
            
            }
            )

        guardarVentas(generalVen)
        system("clear")
        input("guardado con exito")
        system("clear")


    if seleccion == 5: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        booleanoMenu = False
        break