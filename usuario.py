def nuevo_usuario(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=int(input("Ingrese el documento: "))
    usuario["telefono"]=int(input("Ingrese el telefono: "))
    usuario["direccion"]=input("Ingrese la direccion: ")
    usuario["correo"]=input("ingrese el correo: ")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] < 18
    
    datos["usuarios"].append(usuario)
    print("Participante registrado con éxito!")
    return datos

def eliminar_usuario(datos):
    datos = dict(datos)
    documento =int(input("Ingrese el documento del usuario: "))
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
                datos["usuarios"].pop(i)
                print("cliente eliminado!")
                return datos
    print("cliente no existe")
    return datos
    
def Modificar_usuario(datos):
    datos=dict(datos)
    documento = int(input("Ingrese el documento del usuario a remplazar: "))
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:

            while True:
                print("¿que te gustaria cambiar?")
                print("(1) para modificar el nombre: ")
                print("(2) para modificar el documento: ")
                print("(3) para modificar el telefono: ")
                print("(4) para modificar la direccion: ")
                print("(5) para modificar el correo: ")
                print("(6) para modificar la edad: ")
                

                print("(0) para salir ")
                opc=input("ingrese la opcion: ")
                


                if opc=="1":
                    datos["usuarios"][i]["nombre"]= input("ingrese el nuevo nombre: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")


                elif opc== "2":
                    datos["usuarios"][i]["documento"]=int(input("ingrese el nuevo documento: "))
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="3":
                    datos["usuarios"][i]["telefono"]=int(input("ingrese el nuevo telefono: "))
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="4":
                    datos["usuarios"][i]["direccion"]=input("ingrese la nueva direccion: ")
                    print("se guardo con exito")
                    print("------------------------------------------------")
                
                elif opc=="5":
                    datos["usuarios"][i]["correo"]=input("ingrese el nuevo correo")
                    print("se guardo con exito")
                    print("-------------------------------------------------")
                    
                elif opc=="6":
                    datos["usuarios"][i]["edad"]= int(input("ingrese la nueva direccion: "))
                    print("se guardo con exito")
                    print("------------------------------------------------")

                elif opc=="0":
    
                    break
            break
    return datos

def mostrar_usuario(datos):
    datos=dict(datos)
    for value in range(len(datos["usuarios"])):
        print(value)
        print(f" Los Usuarios: {datos["usuarios"][value]["nombre"]}")
        print("---------------------------------------------------------------")
        print(f"documento: {datos["usuarios"][value]["documento"]}")
        print("---------------------------------------------------------------")
        print(f"telefono: {datos["usuarios"][value]["telefono"]}")
        print("---------------------------------------------------------------")
        print(f"direccion: {datos["usuarios"][value]["direccion"]}")
        print("---------------------------------------------------------------")
        print(f"correo: {datos["usuarios"][value]["correo"]}")
        print("---------------------------------------------------------------")
        print(f"edad: {datos["usuarios"][value]["edad"]}")
        print("---------------------------------------------------------------")

