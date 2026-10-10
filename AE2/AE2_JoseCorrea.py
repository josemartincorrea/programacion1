DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
 
 
# funciones
 
def buscar_producto(catalogo, codigo):
    posicion = -1
    for i in range(len(catalogo)):
        if catalogo[i]["codigo"] == codigo:
            posicion = i
            break
    return posicion
 
 
def total_producto(ventas, fila):
    total = 0
    for dia in range(5):
        total = total + ventas[fila][dia]
    return total
 
 
def recaudacion_dia(catalogo, ventas, dia):
    total = 0
    for i in range(len(catalogo)):
        total = total + ventas[i][dia] * catalogo[i]["precio"]
    return total
 
 
# procesos
 
def cargar_producto(catalogo, ventas):
    codigo = int(input("Codigo: "))
    if buscar_producto(catalogo, codigo) != -1:
        print("Ese codigo ya existe")
    else:
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        catalogo.append({"codigo": codigo, "nombre": nombre, "precio": precio})
        ventas.append([0, 0, 0, 0, 0])
        with open("productos.txt", "a") as f:
            f.write(str(codigo) + ";" + nombre + ";" + str(precio) + "\n")
 
 
def registrar_venta(catalogo, ventas):
    dia = int(input("Dia (1 a 5): "))
    codigo = int(input("Codigo: "))
    cantidad = int(input("Cantidad: "))
    fila = buscar_producto(catalogo, codigo)
    if fila == -1 or dia < 1 or dia > 5:
        print("Datos incorrectos, no se registro la venta")
    else:
        ventas[fila][dia - 1] = ventas[fila][dia - 1] + cantidad
        with open("ventas.txt", "a") as f:
            f.write(str(dia) + ";" + str(codigo) + ";" + str(cantidad) + "\n")
 
 
def mostrar_informes(catalogo, ventas):
    print("Unidades vendidas:")
    for i in range(len(catalogo)):
        print(catalogo[i]["nombre"], ":", total_producto(ventas, i))
 
    print("Recaudacion por dia:")
    total = 0
    mejor_dia = 0
    for dia in range(5):
        print(DIAS[dia], ": $", recaudacion_dia(catalogo, ventas, dia))
        total = total + recaudacion_dia(catalogo, ventas, dia)
        if recaudacion_dia(catalogo, ventas, dia) > recaudacion_dia(catalogo, ventas, mejor_dia):
            mejor_dia = dia
 
    maximo = 0
    for i in range(len(catalogo)):
        if total_producto(ventas, i) > maximo:
            maximo = total_producto(ventas, i)
    for i in range(len(catalogo)):
        if total_producto(ventas, i) == maximo and maximo > 0:
            print("Mas vendido:", catalogo[i]["nombre"])
    if total > 0:
        print("Dia de mayor recaudacion:", DIAS[mejor_dia])
 
    print("No se vendieron:")
    for i in range(len(catalogo)):
        if total_producto(ventas, i) == 0:
            print(catalogo[i]["nombre"])
 
    print("Total de la semana: $", total)

 
catalogo = []
ventas = []
 
# uso el "a" para crear el archivo si no existe
with open("productos.txt", "a") as f:
    pass
with open("ventas.txt", "a") as f:
    pass
 
# recuperar lo guardado anterior

with open("productos.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(";")
        catalogo.append({"codigo": int(datos[0]), "nombre": datos[1], "precio": int(datos[2])})
        ventas.append([0, 0, 0, 0, 0])
 
with open("ventas.txt", "r") as f:
    for linea in f:
        datos = linea.strip().split(";")
        fila = buscar_producto(catalogo, int(datos[1]))
        dia = int(datos[0])
        ventas[fila][dia - 1] = ventas[fila][dia - 1] + int(datos[2])
 
opcion = 0
while opcion != 4:
    print("1. Cargar producto  2. Registrar venta  3. Ver informes  4. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        cargar_producto(catalogo, ventas)
    elif opcion == 2:
        registrar_venta(catalogo, ventas)
    elif opcion == 3:
        mostrar_informes(catalogo, ventas)
