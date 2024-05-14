import datos
from datos import *
from menu import*
from serviyprodu import *
from operaciones import*

def ventas(datos,productos):
    datos= dict(datos)
    factura={}
    factura["numero factura"]=int(input("ingrese el numero de factura: "))
    opc = -1
    pedirdc=int(input("ingrese el documento del usuario: "))
    for i in range(len(datos["usuarios"])):
        if pedirdc == datos["usuarios"][i]["documento"]:
            print("que deseas comprar?")
            ventascliente()
            opc = int(input("ingrese una opcion: "))


        if opc == 1:
           print("planes de datos disponibles") 
           mostrar_planes_De_datos(productos)
           tipo = input("¿cual(es) deseas comprar?: ")
           for i in range(len(productos["planes datos"])):
               if productos["planes datos"][i]["tipo"]== tipo:
                   factura[""]
                   tipo2=input("ingrese plan semanal o mensual: ")
                   if tipo2 == "semanal" or tipo2 == "mensual":
                        cantidad=int(input("ingrese cuantos meses va a pagar: "))
                        pagar=valorapagar(productos["planes datos"][i][tipo2],cantidad)
                        return f"el total a pagar es {pagar}"

        elif opc == 2:
            print("planes de internet disponibles")
            mostrar_planes_de_internet(productos)
            tipo= input("¿cual(es) deseas comprar?: ")
            for i in range(len(productos["planes internet"])):
                if productos["planes internet"][i]["tipo"] == tipo:
                    cantidad=int(input("ingrese cuantos meses va a pagar: "))
                    print("el total a pagar es:")
                    return valorapagar(productos["planes internet"][i]["precio mes"],cantidad)
        
        elif opc == 3:
            print("televisores disponibles")
            mostrar_televisor(productos)
            tamaño= input("¿cual(es) deseas comprar ingresar en pulgadas?")
            for i in range(len(productos["televisores"])):
                if productos["televisores"][i]["pulgadas"] == tamaño:
                    cantidad=int(input("ingrese cuantos va a comprar: "))
                    pagar=valorapagar(productos["televisores"][i]["precio"],cantidad)
                    return f"el total a pagar es {pagar}"
                    

        elif opc == 4:
            print("celulares disponibles")
            mostrar_telefonos(productos)
            modelo= input("¿cual(es) deseas comprar?: ")
            for i in range(len(productos["productos"])):
                for j in range(len(productos["productos"][i]["telefonos"])):
                    if productos["productos"][i]["telefonos"][j]["modelo"] == modelo:
                        cantidad=int(input("ingrese cuantos va a comprar: "))
                        pagar=valorapagar(productos["productos"][i]["telefonos"][j]["precio"],cantidad)
                        print(pagar)
                        return f"el total a pagar es {pagar}"
    return "El usuario no ha sido ubicado, parce"
                    
                    

                   

                   
        

   

               


#pedir documento a traves de datos
#al cliente se le van a mostrar los productos
#se le va a pedir ingresar el producto
#pedir cantidades de productos
#multiplicar cantidad x precio 
#se le informa cuanto es el total a pagar
