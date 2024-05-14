#imports
from datos import *
from menu import *
from usuario import *
from serviyprodu import *
from compraventa.ventas import*
from MENU.menu_usuario import*
from MENU.menu_servicios import*
from MENU.menu_televisores import*
from MENU.menu_telefonos import*
from MENU.menu_cliente import*

#Constants
RUTA_BASE_DE_DATOS1 = "usuarios.json"
RUTA_BASE_DE_DATOS2 = "ventas.json"
datos1 = cargar_datos(RUTA_BASE_DE_DATOS1)
datos2 = cargar_datos(RUTA_BASE_DE_DATOS2)

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        opc =0
        menu_usuarios()
        opc=pedir_opcion()
        opc_usuario(opc,datos1,RUTA_BASE_DE_DATOS1)
    elif opc == 2:
        opc=0
        menu_servicios()
        opc = pedir_opcion()
        opc_servicio(opc,datos2,RUTA_BASE_DE_DATOS2)
    elif opc== 3:
        menu_televisor()
        opc = pedir_opcion()
        opc_televisores(opc,datos2,RUTA_BASE_DE_DATOS2)
    elif opc== 4:
        menu_telefonos()
        opc= pedir_opcion()
        opc_telefonos(opc,datos2,RUTA_BASE_DE_DATOS2)
    elif opc== 5:
        menu_cliente()
        opc= pedir_opcion()
        opc_cliente(opc,datos2,RUTA_BASE_DE_DATOS2)
    elif opc == 11:
        print("salio")
        break

guardar_datos(datos1, RUTA_BASE_DE_DATOS1)
guardar_datos(datos2, RUTA_BASE_DE_DATOS2)