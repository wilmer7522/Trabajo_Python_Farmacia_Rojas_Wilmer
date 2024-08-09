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
        json.dump(dataVen,outfile,indent=4)
#Compras
def abrirCompras():
    mijsonCompras=[]
    with open('compras.json', 'r', encoding='utf=8') as openfile:
        mijsonCompras = json.load(openfile)
    return mijsonCompras

def guardarCompras(dataCom):
    with open('compras.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataCom,outfile)
#Empleados
def abrirEmpleados():
    mijsonEmpleados=[]
    with open('empleados.json', 'r', encoding='utf=8') as openfile:
        mijsonEmpleados = json.load(openfile)
    return mijsonEmpleados

def guardarEmpleados(dataEmp):
    with open('empleados.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataEmp,outfile)
#Paciente
def abrirPacientes():
    mijsonPacientes=[]
    with open('pacientes.json', 'r', encoding='utf=8') as openfile:
        mijsonPacientes = json.load(openfile)
    return mijsonPacientes

def guardarPacientes(dataPac):
    with open('pacientes.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataPac,outfile,indent=4)



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
        emple = abrirEmpleados()
        conta = 1
        pacien = abrirPacientes()
        contapa = 1
        medi = abrirMedicamentos()
        contamed = 1
        print("---------")
        print("Empleados")
        print("---------")
        for i in emple:
            
            print(conta,i["nombre"])
            conta +=1
            
        eleEmple = int(input("Ingrese el id del empleado: "))
        nombreemple = emple[eleEmple-1]["nombre"]
        cargoEmple = emple[eleEmple-1]["cargo"]
        print("---------")
        print("Pacientes")
        print("---------")
        for i in  pacien:
            
            print(contapa,i["nombre"])
            contapa +=1

        elePaci = int(input("Ingrese el id del paciente: "))
        nombrePaci = pacien[elePaci-1]["nombre"]
        direccionPaci = pacien[elePaci-1]["direccion"]

        
        print("------------")
        print("Medicamentos")
        print("------------")
        for i in medi:
            print(contamed,i["nombre"])
            contamed +=1

        eleMedi =int(input("ingrese el ID del medicamento: "))
        nombreMedi = medi[eleMedi-1]["nombre"]
        cantidad = int(input("ingrese la vantidad Vendida: "))
        preciMed = medi[eleMedi-1]["precio"]
        print(f"Precio: ",preciMed)

        total = preciMed*cantidad

        generalVen=abrirVentas()
        for i in generalVen[0]["ventas"]:
            fecha = date.today()
            fe = fecha.isoformat()
            
            generalVen=abrirVentas()
            generalVen[0]["ventas"].append({
                "fechaVenta": fe,
        "paciente": {
            "nombre": nombrePaci,
            "direccion": direccionPaci
        },
        "empleado": {
            "nombre": nombreemple,
            "cargo": cargoEmple
        },
        "medicamentosVendidos": [
            {
                "nombreMedicamento": nombreMedi,
                "cantidadVendida": cantidad,
                "precio": preciMed,
                "total": total
            }
        ]
            
            }
            )

        guardarVentas(generalVen)
        input("guardado con exito")
        system("cls")


    if seleccion == 5: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        booleanoMenu = False
        break