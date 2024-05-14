import datos
from datos import *
#crud de planes de datos internet
def modificar_planes(datos, planes):
    datos=dict(datos)
    if planes == "planes internet":
        plan = input("Ingresa el plan de internet: ")
        for i in range(len(datos["planes internet"])):
            if datos["planes internet"][i]["tipo"] == plan:
                print("******************************")
                print("¿que te gustaria cambiar?")
                print("1). para cambiar el tipo")
                print("2). para cambiar la capacidad")
                print("3). para cambiar el precio")

                print("0). para salir")

                opc=int(input("ingrese la opcion"))
                print("*************************")
                if opc == 1:
                    datos["planes internet"][i]["tipo"]= input("ingrese el nuevo tipo: ")
                    print("guardado con exito")
                    print("--------------------------------")
                elif opc == 2:
                    datos["planes internet"][i]["capacidad"]= input("ingrese la nueva capacidad: ")
                    print("guardado con exito")
                    print("-------------------------------------------")
                elif opc == 3:
                    datos["planes internet"][i]["precio mes"]=int(input("cambiar el precio: "))
                    print("guardado con exito")
                    print("--------------------------------") 

                elif opc == 0:
                    break 
            
    elif  planes == "planes datos":
        plan = input("Ingresa el plan de datos: ")
        for i in range(len(datos["planes datos"])):
             if datos["planes datos"][i]["tipo"] == plan:
                print("******************************")
                print("¿que te gustaria cambiar?")
                print("1). para cambiar el precio mensual")
                print("2). para cambiar capacidad x mes ")
                print("3). para cambiar el precio semanal")
                print("4). para cambiar capacidad x mes ")

                print("0). para salir del programa")

                opc=int(input("ingrese la opcion"))
                print("*************************")
                if opc == 1:
                    datos["planes datos"][i]["mensual"]= int(input("ingrese el nuevo precio: "))
                    print("guardado con exito")
                    print("--------------------------------")
                elif opc == 2:
                    datos["planes datos"][i]["capacidad mes"]=input("ingrese el nuevo paquete de gb: ")
                    print("guardado con exito")
                    print("-------------------------------------------")
                elif opc == 3:
                    datos["planes datos"][i]["semanal"]=int(input("ingrese la nuevo precio: "))
                    print("guardado con exito")
                    print("----------------------------------------------")

                elif opc == 4:
                    datos["planes datos"][i]["capacidad semana"]= input("ingrese el nuevo paquete de gb: ") 
                    print("guardado con exito")
                    print("---------------------------------------------") 

                elif opc == 0:
                    break 
             
    return datos 

def agregar_planes_de_internet(datos):
    datos = dict(datos)
    internet={}
    internet["tipo"]=input("ingrese el nuevo tipo de internet: ")
    internet["capacidad"]=input("ingrese la nueva capacidad del internet: ")
    internet["precio mes"]=int(input("ingrese el precio que quiera agregar: "))

    datos["planes internet"].append(internet)
    print("nueva forma de internet agregada con exito")
    return datos

def eliminar_plan_de_internet(datos):
    datos=dict(datos)
    tipo=input("ingrese el tipo de internet: ")
    for i in range(len(datos["planes internet"])):
        if datos["planes internet"][i]["tipo"] == tipo:
            datos["planes internet"].pop(i)
            print("plan elimiado")
            return datos
    print("plan no existe")
    return datos   

def mostrar_planes_de_internet(datos):
    datos=(datos)
    for value in range(len(datos["planes internet"])):
        print(value) 
        print(f" Tipo de Plan de internet: {datos["planes internet"][value]["tipo"]}")
        print("---------------------------------------------------------------")
        print(f" Capacidad: {datos["planes internet"][value]["capacidad"]}")
        print(f" pago por mes: {datos["planes internet"][value]["precio mes"]}")
        print("---------------------------------------------------------------")

def mostrar_planes_De_datos (datos):
    datos=dict(datos)
    for value in range(len(datos["planes datos"])):
        print(f" Tipo de Plan de datos: {datos["planes datos"][value]["tipo"]}")
        print("---------------------------------------------------------------")
        print(f"Capacidad por mes: {datos["planes datos"][value]["capacidad x mes"]}")
        print(f"Capacidad de pago por mes: {datos["planes datos"][value]["mensual"]}")
        print(f"Capacidad por mes: {datos["planes datos"][value]["capacidad x semana"]}")
        print(f"Capacidad por pago mes: {datos["planes datos"][value]["semanal"]}")
        print("---------------------------------------------------------------")
        
            

#crud de los productos(celulares)

def añadir_telefonos(datos):
    datos=dict(datos)
    celular={}
    for i in range(len(datos["productos"])):
        celular["marca"]=input("ingrese la marca: ")
        celular["modelo"]=input("ingrese el modelo: ")
        celular["almacenamiento"]=input("ingrese el almacenamiento en GB o TB: ")
        celular["camara trasera principal"]=input("ingrese los mpx de la camara principal: ")
        celular["bateria"]=input("ingrese el mah de la bateria: ")
        celular["precio"]=int(input("ingrese el precio del dispositivo en COP: "))
        datos["productos"][i]["telefonos"].append(celular)
        print("telefono registrado con exito")
    return datos
def eliminar_producto(datos):
    datos=dict(datos)
    modelo= input("ingrese el modelo a eliminar: ")
    for i in range(len(datos["productos"])):
        for i in range(len(datos["telefonos"])):
            if datos["telefonos"][i]["modelo"]==modelo:
                datos["telefonos"].pop(i)
                print("telefono eliminado")
                return datos
    print("telefono no encontrado") 
    return datos 

def mostrar_telefonos(datos):
    datos=dict(datos) 
    for  i in range(len(datos["productos"])):
        for value in range(len(datos["productos"][i]["telefonos"])):
            print(f" marca de telefono: {datos["productos"][i]["telefonos"][value]["marca"]}")
            print("---------------------------------------------------------------")
            print(f"modelo de telefono: {datos["productos"][i]["telefonos"][value]["modelo"]}")
            print(f"almacenamiento del telefono: {datos["productos"][i]["telefonos"][value]["almacenamiento"]}")
            print(f"Capacidad camara trasera: {datos["productos"][i]["telefonos"][value]["camara trasera principal"]}")
            print(f"Capacidad bateria: {datos["productos"][i]["telefonos"][value]["bateria"]}")
            print(f"precio del producto: {datos["productos"][i]["telefonos"][value]["precio"]}")
            print("---------------------------------------------------------------")


def modificar_telefonos(datos,productos):   
    datos=dict(datos)
    if productos == "productos":
        tipo_p=input("ingrese el tipo de producto (telefono): ")
    for i in range(len(datos["productos"])):
        if datos["productos"]["telefonos"][i]["marca"]==tipo_p:
            print("**********************************")
            print("¿que te gustaria cambiar?")
            print("1). para cambiar la marca")
            print("2). para cambiar la modelo")
            print("3). para cambiar el almacenamiento")
            print("4). para cambiar la camara trasera principal")
            print("5). para cambiar el mah de bateria")
            print("6). para cambiar el precio")

            print("0). para salir ")


            opc=int(input("ingresa la opcion: "))
            print("****************************")
            if opc == 1:
                datos["productos"]["telefonos"][i]["marca"]= input("ingrese la nueva marca: ")
                print("-----------------------------")
            elif opc == 2:
                datos["productos"]["telefonos"][i]["modelo"]= input("ingrese el nuevo modelo: ")
                print("-----------------------------")
            elif opc == 3:
                datos["productos"]["telefonos"][i]["almacenamiento"]= input("ingrese el nuevo elmacenamiento: ")
                print("-----------------------------")
            elif opc == 4:
                datos["productos"]["telefonos"][i]["camara trasera principal"]= input("ingrese la nueva camara: ")
                print("-----------------------------")
            elif opc == 5:
                datos["productos"]["telefonos"][i]["bateria"]= input("ingrese el nuevo mah de bateria: ")
                print("-----------------------------")
            elif opc == 6:
                datos["productos"]["telefonos"][i]["precio"]=int(input("ingrese el nuevo precio: "))
                print("-----------------------------")

            elif opc == 0:
                break
    return datos

def modificar_televisores(datos):
        datos=dict(datos)
        tamaño=input("ingrese el tipo de producto con las pulgadas: ")
        for i in range(len(datos["televisores"])):
            if datos["televisores"][i]["pulgadas"]==tamaño:
                print("**********************************")
            print("¿que te gustaria cambiar?")
            print("1). para cambiar la marca")
            print("2). para cambiar la modelo")
            print("3). para cambiar el tamaño rn pulgadas")
            print("4). para cambiar el precio")

            print("0). para salir ")

            opc=int(input("ingresa la opcion: "))
            print("****************************")
            if opc == 1:
                datos["televisores"][i]["marca"]= input("ingrese la nueva marca: ")
                print("-----------------------------")
            elif opc == 2:
                datos["televisores"][i]["modelo"]= input("ingrese el nuevo modelo: ")
                print("-----------------------------")
            elif opc == 3:
                datos["televisores"][i]["pulgadas"]= input("ingrese el nuevo tamaño: ")
                print("-----------------------------")
            elif opc == 4:
                datos["televisores"][i]["precio"]= int(input("ingrese el nuevo precio: "))
                print("-----------------------------")

            elif opc == 0:
                break
        return datos

#crud de los productos(televisores)
def añadir_televisores(datos):
    datos=dict(datos)
    televisor={}
    
    televisor["marca"]=input("ingrese la marca:")
    televisor["modelo"]=input("ingrese el modelo: ")
    televisor["pulgadas"]=input("ingrese el tamaño: ")
    televisor["precio"]= int(input("ingrese el nuevo precio: "))
    datos["televisores"].append(televisor)


    print("televisor registrado con exito")
    return datos

def eliminar_televisores(datos):
    datos=dict(datos)
    tamaño=input("ingrese el tamaño del televisor a eliminar ")
    for i in range(len(datos["televisores"])):
        if datos["televisores"][i]["pulgadas"]==tamaño:
            datos["televisores"].pop(i)
            print("televisor eliminado")
            return datos 
    print("televisor no encontrado")
    return datos

def mostrar_televisor(datos):
    datos=dict(datos)
    lista=[]
    for value in range(len(datos["televisores"])):
        print(value)





