from usuario import*
from datos import*

def opc_usuario(opc,datos, ruta):
    if opc < 0:
        return "debe ser entero"
    if opc == 1:
        datos = nuevo_usuario(datos)
        guardar_datos(datos,ruta)
    elif opc == 2:
       datos= eliminar_usuario(datos)  
       guardar_datos(datos,ruta)
    elif opc ==3:
       datos= Modificar_usuario(datos)
       guardar_datos(datos,ruta)
    elif opc ==4:
        datos=mostrar_usuario(datos)
        guardar_datos(datos,ruta)