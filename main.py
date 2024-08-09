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
        json.dump(dataMedi,outfile,indent=4)
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
        json.dump(dataCom,outfile,indent=4)
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
        json.dump(dataPac,outfile)

#Proveedores
def abrirProveedores():
    mijsonProveedores=[]
    with open('proveedores.json', 'r', encoding='utf=8') as openfile:
        mijsonProveedores = json.load(openfile)
    return mijsonProveedores

def guardarProveedores(dataPro):
    with open('proveedores.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataPro,outfile)


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
            seleccion = int(input("(1).Registrar Venta | (2).Registrar Compra: | (3).Salir \nIngrese opcion: "))
            
            booleanoMenu = False
        except ValueError:
            input("ingrese un valor valido")
            system("cls")

    if seleccion == 1:
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
            print(contamed,"|",i["nombre"],"| Precio: $",i["precio"],"| Cantidad Disponible",i["stock"],"|")
            contamed +=1

        eleMedi =int(input("ingrese el ID del medicamento: "))
        nombreMedi = medi[eleMedi-1]["nombre"]
        cantidad = int(input("ingrese la vantidad Vendida: "))
        preciMed = medi[eleMedi-1]["precio"]
        print(f"Precio: ",preciMed)

        total = preciMed*cantidad

        stock =medi [eleMedi-1]["stock"]
        totalStock = stock - cantidad

        medi[eleMedi-1]["stock"]= totalStock

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

        guardarMedicamentos(medi)

        guardarVentas(generalVen)
        print(f"| Fecha de Venta: ",fe,"| Paciente: ",nombrePaci,"| Direccion: ",direccionPaci, "\n ""| Empleado: ", nombreemple, "| Cargo: ",cargoEmple,"\n" "| ",nombreMedi,"|", cantidad,"|", preciMed,"|", total,"\n| Cantidad Disponible", totalStock,)
        input("guardado con exito")
        system("cls")
    if seleccion == 2:
        Prove = abrirProveedores()
        conta = 1
        medi = abrirMedicamentos()
        contamed = 1

        print("-----------")
        print("Proveedores")
        print("-----------")
        for i in Prove:
            print(conta,i["nombre"])
            conta +=1

        elePro = int(input("Ingrese el id del proveedor: "))
        nombrePro = Prove[elePro-1]["nombre"]
        contactoPro = Prove[elePro-1]["contacto"]


        print("------------")
        print("Medicamentos")
        print("------------")
        for i in medi:
            print(contamed,"|",i["nombre"],"| Cantidad Disponible",i["stock"],"|")
            contamed +=1

        eleMedi =int(input("ingrese el ID del medicamento: "))
        nombreMedi = medi[eleMedi-1]["nombre"]
        cantidad = int(input("ingrese la cantidad comprada: "))
        preciMed = int(input("Ingrese el Precio de Compra: "))
        print(f"Precio: ",preciMed)

        total = preciMed*cantidad
        stock =medi [eleMedi-1]["stock"]
        totalStock = stock + cantidad

        medi[eleMedi-1]["stock"]= totalStock
        compras=abrirCompras()
        for i in compras:
            fecha = date.today()
            fe = fecha.isoformat()
            
            
            compras["compras"].append( {
        "fechaCompra": fe,
        "proveedor": {
            "nombre": nombrePro,
            "contacto": contactoPro
        },
        "medicamentosComprados": [
            {
                "nombreMedicamento": nombreMedi,
                "cantidadComprada": cantidad,
                "precioCompra": preciMed,

                "total": total
            }
        ]
    }
            )

        guardarMedicamentos(medi)

        guardarCompras(compras)
        print("compra Guardada con exito :)")

        print(f"| Fecha de Compra: ",fe,"| Proveedor: ",nombrePro,"| Contacto: ",contactoPro, "\n| Medicamento", nombreMedi, "|",cantidad, "|",preciMed,"|", total, "\n Cantidad Disponible", totalStock)
        input("Presione enter para continuar")
        system("cls")


    if seleccion == 3: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        booleanoMenu = False
        break