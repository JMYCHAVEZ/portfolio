import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(),"Recetas") # esto es para ver saber la ruta para llegar a recetas

def contar_recetas(ruta): # esta funcion lo que me va a traer es la CANTIDAD TOTAL DE RECETAS
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"): # para traer todas las recetas que terminen en txt de todos los directorios
        contador = contador + 1 # el contador para que me diga cuantas son en cantidad
    return contador

def inicio(): # no necesita parametro porque va a ser lo primero que se va a ejecutar en nuestro programa
    system("cls")
    print("*" * 50)
    print("*" * 5 +" Bienvenido al administrador de recetas "+"*" * 5)
    print("*" * 50)
    print("\n")
    print(f" Las recetas se encuentran en {mi_ruta}") # la primera variable que creamos
    print(f" Total recetas: {contar_recetas(mi_ruta)}") # le pasamos como parametro mi ruta para
    # que pueda buscar dentro de mi ruta
    eleccion_menu = "x" # ponemos que tiene que ser de un digito
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7): # creamos un loop while para que se eje
        print("Elije una opcion: ")                                               #cute siempre que NO ponga un numero
        print("""                                                                 
        [1] Leer Receta
        [2] Crear Receta Nueva
        [3] Crear Categoria Nueva
        [4] Eliminar Receta
        [5] Eliminar Categoria
        [6] Salir del Programa""")
        eleccion_menu = input()

    return int(eleccion_menu)
    # is numeric es para saber si hay un numero
    # esta es la condicion que se va a tener que repetir



def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categoria = Path(ruta) # para el uso interno de la funcion tiene el contenido de la ruta q pasamos
    lista_categorias = [] # en esta lista vamos a devolver con nombre de carpetas
    contador = 1 #para ir mostrando carpetas con ese numero.

    for carpeta in ruta_categoria.iterdir(): # va a iterar en cada carpeta. y vamos a poder usar.name
        carpeta_str = str(carpeta.name) # ESTO ES PARA TRAER EL NOMBRE DE SOLO ESA CARPETA
        print(f"[{contador}] - {carpeta_str}") # esto me muestra CUANDO ELIJO UNA OPCION" [1] - Carnes"
        lista_categorias.append(carpeta) # ALMACENAMOS EN LA LISTA LO QUE ESTA ADENTOR DE LA CARPETA
        # ALMACENAMOS: [1] - Entrecot al Malbec.txt
        contador = contador + 1 # esto es para que se siguen sumando los contador, [1], [2], [3]
        #sino aparececia todas las categorias con un [1] . carnes [1] ensaladas.

    return lista_categorias


def elegir_categoria(lista): #una lista de las cat que puede elegir
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista)+1):# le ponemos mas una
        eleccion_correcta = input("\nElije una categoria: ")                                         # porque nunca cuenta hasta ese
                                                                                                    #nuevo que agregamos
    return lista[int(eleccion_correcta)-1] # para que nos de el indice correcto.
                                        # para cuando agreguemos una nueva categoria, elija bien

def mostrar_recetas(ruta): #para saber en donde estan las recetas
    print("Recetas: ")
    ruta_receta = Path(ruta) # para saber en donde ubicas las recetas.
    lista_recetas = []
    contador = 1

    for receta in ruta_receta.glob("*.txt"): # para que me traiga todas las recetas que haya ruta receta
        receta_str = str(receta.name) # si no ponemos el .name (nos trae toda la ruta)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador = contador + 1
    return lista_recetas

def elegir_receta(lista):
    eleccion_receta = "x" # para asegurarnos de que sea incorrecto
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input("\n Elije una receta: ")
    return lista[int(eleccion_receta) - 1] # para que se equipare con los numeros del indice

def leer_receta(receta):
    print(Path.read_text(receta)) # metodo path para leer un archivo.

def crear_receta(ruta): # necesita que le pasemos una ruta para que sepa donde crearla
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta,nombre_receta) # esta ruta llega solo hasta categoria

        if not os.path.exists(ruta_nueva): # SI NO EXISTE
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento esta receta ya existe")
    #esta funcion no tiene que devolver nada. SOLAMENTE CREA.

def crear_categoria(ruta): # necesita que le pasemos una ruta para que sepa donde crearla
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta,nombre_categoria) # esta ruta llega solo hasta categoria

        if not os.path.exists(ruta_nueva): # SI NO EXISTE
            Path.mkdir(ruta_nueva) #crear una nueva carpeta, un nuevo directorio
            print(f"Tu nueva categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento esta categoria ya existe")
    #esta funcion no tiene que devolver nada. SOLAMENTE CREA.

def eliminar_receta(receta): # que receta tiene que eliminar
    Path(receta).unlink() # metodo para eliminar un archivo
    print(f" La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria).rmdir() # esto eliminar la carpeta / directorio
    print(f" La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "v":
        eleccion_regresar = input("\nPresiones V para volver al menu: ")

finalizar_programa = False

while not finalizar_programa:

    menu = inicio() #la funcion que inicia todo el juego

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoria.")
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()

    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()

    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()

    elif menu ==6:
        finalizar_programa = True




