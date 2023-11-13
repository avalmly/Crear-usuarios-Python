#--------------------------------------------------------------------
# Autor: Alberto Valero Mlynaricova
# Fecha: 13/11/2023
#
# Descripción:  Programa que dependiendo del sistema operativo en el que se
#               está se creará un usuario
#-------------------------------------------------------------------

import os                                                                       # Para usar funciones del sistema (Linux)
import subprocess                                                               # Para usar cmdlets de Powershell
import platform                                                                 # Para sacar info del OS
import json                                                                     # Para usar funciones relacionadas con JSON

class Usuario:
    def __init__(self, nombre, os):
        self.nombre = nombre
        self.os = os

def cargar_usuarios_desde_json(nombre_archivo):                                 # Lee un json que contiene una lista de usuarios[nombre, OS]
    with open('lista_users.json', 'r') as archivo:
        contenido = json.load(archivo)
    return contenido['usuarios']

def crear_usuarios(lista_usuarios, os):                                         # Crea un array de objetos
    return [Usuario(usuario['nombre'], usuario['os']) for usuario in lista_usuarios]

def main():
    sistema = platform.system()

    if sistema == 'Windows':
        print('Esto es Windows')
        lista_usuarios = cargar_usuarios_desde_json('lista_users_windows.json')
        usuarios_clase = crear_usuarios(lista_usuarios, sistema)
        for usuario in usuarios_clase:
            if usuario.os == sistema:
                #print(f"Nombre: {usuario.nombre} OS: {usuario.os}")
                resultado = subprocess.run(["powershell", "New-LocalUser -Name 'usuario.nombre' -NoPassword"], capture_output=True, text=True)
                #print(resultado.stdout)                                        # Muestra el resultado por consola de crear el usuario [Debugging]

    elif sistema == 'Linux':
        print('Esto es Linux')
        lista_usuarios = cargar_usuarios_desde_json('lista_users_linux.json')
        usuarios_clase = crear_usuarios(lista_usuarios, sistema)
        for usuario in usuarios_clase:
            if usuario.os == sistema:
                #print(f"Nombre: {usuario.nombre} OS: {usuario.os}")
                os.system("useradd usuario.nombre -p usuario.nombre")

    elif sistema == 'Darwin':
        print('Esto es macOS')
        lista_usuarios = cargar_usuarios_desde_json('lista_users_linux.json')
        usuarios_clase = crear_usuarios(lista_usuarios, sistema)
        for usuario in usuarios_clase:
            if usuario.os == sistema:
                #print(f"Nombre: {usuario.nombre} OS: {usuario.os}")
                os.system("dscl -create /Users/usuario.nombre")                   # Creamos un usuario
                os.system("dscl -passwd /Users/usuario.nombre usuario.nombre")    # Le ponemos de contraseña su nombre de usuario

    else:
        print('Sistema operativo no soportado')

if __name__ == "__main__":
    main()
