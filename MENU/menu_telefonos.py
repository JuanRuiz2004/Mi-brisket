from datos import*
from serviyprodu import*

def opc_telefonos(opc,datos,ruta2):
    if opc < 0:
        return "debe ser entero"
    if opc ==1:
        datos= (datos)
        datos=modificar_telefonos(datos)
        guardar_datos(datos,ruta2)
    elif opc == 2: 
        datos=eliminar_producto(datos)
        guardar_datos(datos,ruta2)
    elif opc == 3:
        datos= añadir_telefonos(datos)
        guardar_datos(datos,ruta2)
    elif opc== 4:
        datos=mostrar_telefonos(datos)
        guardar_datos(datos,ruta2)