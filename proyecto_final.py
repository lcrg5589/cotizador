import mysql.connector as mariadb

mariadb_conexion = mariadb.connect(
    host='localhost',
    port='3306',
    user='root',
    password='',
    database='prueba_cot'
)
cursor = mariadb_conexion.cursor()

productos = {
  101:"Pantalla",
  102:"Teclado ",
  103:"Mouse   ",
  104:"RAM     ",
  105:"USB     "
}

precios = {
  101:"300000",
  102:"110000",
  103:"70000",
  104:"140000",
  105:"20000"

}
#creamos listas para llevar el orden los articulos seleccionados por el usuario
prices = []
amount = []
arti = []
subtotal = []

iva = 1.19

#imprimir en pantalla el catalogo
catalogo = '''
Escriba el codigo del producto a cotizar

101 -  Pantalla 15Pul
102 -  Teclado Jannus
103 -  Mouse Jannus
104 -  RAM DDR3 8GB
105 -  USB 8GB

escriba 'fin' para terminar
'''
print("         BIENVENIDO AL COTIZADOR \n      Advance Support and Serviced")

ident1 = int(input("Digite el identificaciòn del cliente: "))
nombre1 = input("Digite el nombre del cliente: ")
direc1 = input("Digite el dirección del cliente: ")
ciudad1 = input("Digite la ciudad del cliente: ")
telefono1 = int(input("Digite el telefono del cliente: "))
correo1 = input("Digite el correo del cliente: ")

print(catalogo)

#mantenemos la ejecucion del catalogo en pantalla con el bucle while, hasta que el usuario escribe 'fin'
while True:
  producto = input("producto: ")

#si el usuario escribe fin, procede con la totalizacion de la cotizacion
  if producto == 'fin':
    break
  else:
    cantidad = int(input("cantidad: "))
    prec = precios[int(producto)]
    articulo = productos[int(producto)]
    arti.append(articulo)
    prices.append(prec)
    amount.append(cantidad)

print("\n")
print("      Advance Support and Serviced")
print("              Cotizaciòn")
print("Nombre: " + nombre1)
print("Identificaciòn: " + str(ident1))
print("Direccion: " + direc1)
print("Telefono: " + str(telefono1))
print("Ciudad: " + ciudad1)
print("Correo: " + correo1)
print("______________________________")
print("Descrpcion         | Cantidad")
print("------------------------------")

for x, i in enumerate(arti):
  cantidad = amount[x]
  print (i, '          |    ', cantidad)

print("\n")

print("\n")
#iteramos sobre la lista de precios de los productos seleccionados
#para multiplicarlos por la cantidad deseada
for x, i in enumerate(prices):
  pos = x
  precio_unidad = i
  cant = amount[pos]
  sub_tot = int(precio_unidad) * cant
  subtotal.append(sub_tot)

print("----------------------------")
sumatoria = sum(subtotal)
subtotal1 = float(sumatoria)
vriva = (sumatoria * float(iva)) - sumatoria
iva1 = float(vriva)
total_con_iva = sumatoria * float(iva)
total1 = float(total_con_iva)
print("Subtotal           |", subtotal1)
print("IVA                |", iva1)
print("Total              |", total1)
print("----------------------------")
print("Contactenos\nCelular: 312 5737457 \ne-mail: asoppoteas@gmail.com \nBogota D.C.")
("\n")

sql = "INSERT INTO cotizacion (nit, nombre, direccion, ciudad, telefono, correo, subtotal, iva, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (ident1, nombre1, direc1, ciudad1, telefono1, correo1, subtotal1, iva1, total1)

cursor.execute(sql, val)
mariadb_conexion.commit()
("\n")
print(cursor.rowcount, "Registro ingresado")
("\n")

try:
    cursor.execute("SELECT id_cotizacion,nit,nombre,direccion,ciudad,telefono,correo,subtotal,iva,total FROM cotizacion")
    for id_cotizacion, nit, nombre, direccion, ciudad, telefono, correo, subtotal, iva, total in cursor:
        ("ID: " + str(id_cotizacion))

except mariadb.Error as Error:
    print("Error: {}".format(Error))

mariadb_conexion.close()
