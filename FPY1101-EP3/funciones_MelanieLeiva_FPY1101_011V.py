import os
libros=[]

sku_libro= []

def registrar():
    try:
        titulo=input("Ingrese el título del libro que desea registrar: ").upper()
        autor= input("Ingrese el autor del libro: ").upper()
        publicacion= int(input("Ingrese el año de publicación del libro: "))
        sku=input("Ingrese el SKU del libro (6 primeras letras(título)3 primeras letras(autor)): ").upper()

        sku_libro.append(sku)
        if titulo =="" or autor==""or publicacion<=0 or sku=="":
            print("¡Error es registrar!.Intente nuevamente el registro")
        

        libros.append({
            "Título": titulo,
            "Autor": autor,
            "Año de Publicación": publicacion,
            "SKU": sku,
        })
        
        print("Registro exitoso")
    except ValueError:
        print("Error en el dato ingresado, debe intentar nuevamente registrar")

def prestar():
    nombre= input("Ingrese el nombre de usuario para solicitar libro: ")
    sku=("Ingresar el SKU del libro que desea solicitar: ").upper()
    if nombre=="":
        print("Tiene que digitar su nombre ")
    while sku not in sku_libro:
        print("El libro no existe")
        break
    for prestados in libros:
        print(prestados)    

def listar ():
    print("Listar todos los libros Registrados: ")
    for libreria in libros:
        print(libreria)
        break


def imprimir():
    with open ("lista de libros.txt","w")as archivo:
        for libro in libros:
            archivo.write(f"Título:{libro["Título"]}\tAutor:{libro["Autor"]}\tAño de Publicación:{libro["Año de Publicación"]}\tSKU:{libro["SKU"]}\n")
            print("Planilla de todos los libros realizada correctamente.")

def salir():
    nombre=input("Usuario: ")
    run=float(input("Digite su run: "))
    print(f"Programa de finalizacion...\nDesarrollado por: {nombre}\nRun:{run}")

def menu():
    
    while True:
        try:
            print("Bienvenido a la biblioteca. Degite una opcion para comenzar:")
            print("1. Registrar libro")
            print("2.Prestar libro")
            print("3.Listar todos los libros ")
            print("4.Imprimir reporte de préstamos")
            print("5.Salir del programa")

            op=int(input("Ingrese su opcion --> "))

            if op==1:
                registrar()
            elif op==2:
                prestar()
            elif op==3:
                listar()
            elif op==4:
                imprimir()
            elif op==5:
                salir()
            else:
                print("La opcion que ha digitado no es valida")
        except ValueError:
            print("Error: su opcion no esta valida, digite una opción del 1-5, por favor :")
          

        