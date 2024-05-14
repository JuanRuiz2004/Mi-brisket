from datos import*
from serviyprodu import*
from compraventa.ventas import*

def opc_servicio(opc,datos,ruta2):
    if opc < 0:
        return "debe ser entero"
    if opc ==1:
        datos= modificar_planes(datos)
        guardar_datos(datos,ruta2)
    elif opc == 2: 
        datos=eliminar_plan_de_internet(datos)
        guardar_datos(datos,ruta2)
    elif opc == 3:
        datos= agregar_planes_de_internet(datos)
        guardar_datos(datos,ruta2)
    elif opc== 4:
        ventas(datos)
        guardar_datos(datos,ruta2)
    