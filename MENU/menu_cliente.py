from datos import*
from serviyprodu import*

def opc_cliente(opc,datos,ruta2):
    if opc < 0:
        return "debe ser entero"
    if opc ==1:
        datos= mostrar_planes_de_internet(datos)
        guardar_datos(datos,ruta2)
    elif opc == 2: 
        datos=mostrar_planes_De_datos(datos)
        guardar_datos(datos,ruta2)
    elif opc == 3:
        datos= agregar_planes_de_internet(datos)
        guardar_datos(datos,ruta2)
  
    