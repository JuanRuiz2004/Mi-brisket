def menu_principal():
    print("¡BIENVENIDO AL MENU DE ADMINISTRADOR!")
    print("***************************************")
    print("Ingrese la opción que requiera")
    print("1). usuarios")
    print("2). Modinternet ")
    print("3). Modtelevisores")
    print("4). modtelefonos")
    print("5). clientes")
    print("11. para salir")
    print("***************************************")
    

def menu_cliente():
    print("BIENVENIDO CLIENTE DE CLARO")
    print("*******************************************************")
   
    print("1). para MOSTRAR los planes de internet")
    print("2)- para MOSTRAR los planes de datos ")
    print("3). para Comprar ")
    print("11). para salir")

#opc usuarios
def menu_usuarios():
    print("***************************************")
    print("Ingrese la opción que requiera")
    print("1. para INGRESAR un nuevo usuario")
    print("2. para ELIMINAR un usuario")
    print("3. para MODIFICAR ussuario")
    print("4. para MOSTRAR usuarios ")
    print("11. para salir")
    print("***************************************")
    
    
#opc servicios y productos
def menu_servicios():
    print("BIENVENIDO AL MENU DE SERVICIOS")
    print("************************************************")
    print("1). para modificar planes datos e internet ")
    print("2). para ELIMINAR planes de internet")
    print("3). para AGREGAR planes de internet ")
    print("4). para MOSTRAR planes de datos e internet")
#opc servicios y productos 
def menu_televisor():
    print("BIENVENIDO AL MENU DE TELEVISORES")
    print("**************************************************")
    print("1). para MODIFICAR productos( televisores) ")
    print("2). para ELIMINAR productos( televisores)")
    print("3). para AGREGAR productos (televisores) ")
    print("4). para MOSTRAR productos(televisores)")

def menu_telefonos():
    print("BIENVENIDO AL MENU DE TELEFONOS")
    print("**************************************************")
    print("1). para MODIFICAR productos(telefonos) ")
    print("2). para ELIMINAR productos(telefonos)")
    print("3). para AGREGAR productos (telefonos) ")
    print("4). para MOSTRAR productos(telefonos)")

#opc ventas
def ventascliente():
    print("1). para COMPRAR planes de datos ")
    print("2). para COMPRAR planes de internet")
    print("3). para COMPRAR televisores")
    print("4). para COMPRAR celulares")

#contraseña si es menu admin o cliente regular

            
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1       
    


