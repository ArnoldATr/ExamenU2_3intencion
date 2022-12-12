# Nombre: Arnold Avalos Torres
# No. Control: 18420428
# Fecha: 12 de Diciembre del 2022

def crear_lista():
    archivo_texto = open("libros.txt", "r")
    lineas_texto = archivo_texto.readlines()
    archivo_texto.close()
    listaLibro = []
    for i in lineas_texto[1:]:
        reg = i.split(',')
        dicc = {
            "codigo": reg[0],
            "Nombre": reg[1],
            "Editorial": reg[2],
            "Autor": reg[3],
            "Genero": reg[4],
            "PaisAutor": reg[5],
            "NumeroPaginas": reg[6],
            "AñoEdicion": reg[7],
            "PrecioLibro": reg[8]
        }
        listaLibro.append(dicc)
    for i in listaLibro:
        print(i)

def menu_principal():
    while True:
        print("/******************* Menu Principal ************************/")
        print(" 1. Crear lista ")
        print(" 2. Insertar libro ")
        print(" 3. Grabar lista ")
        print(" 4. Salir ")

        opcion = int(input(" Dame una opcion: "))

        # Opciones a realizar
        if opcion == 1:
            print("Crear lista")
            crear_lista()
        elif opcion == 2:
            print("Insertar un libro")
            # insertar_libro()
        elif opcion == 3:
            print("Grabar la lista")
        elif opcion == 4:
            break
        else:
            print("Opcion Invalida")

menu_principal()



