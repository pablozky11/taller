print ("***Salpicon***")
print ("*****")
print ("0. Salir")
print ("1. Registrar Frutas")
print ("2. Costo Total Salpicon")
print ("3. Mostrar Frutas por Precio de mayor a menor")
print ("4. Mostrar Cual fruta es mas cara")
print ("5. Mostrar Cual fruta es mas barata")
print ("******")

opcion=90
salpicon=[]

while (opcion != 0):
  
  
  opcion=int(input("Digita una opcion: "))
  if opcion == 1:
    cantidad = int(input("Ingrese la cantidad de frutas: "))
    for fruta in range(cantidad):
      frutas={}
      #fruta= fruta+1
      frutas["nombre"] = input("ingrese el nombre de la fruta: ")
      frutas["id"] = input("ingrese el id: ")
      frutas["precio"] = int(input("ingrese el precio unitario: "))
      frutas["cantidad"] = int(input("ingrese la cantidad: "))
      salpicon.append(frutas)
      
  elif opcion==2 :
    for fruta in salpicon: 
      print (fruta)
      ##precio = fruta["precio"] * fruta["cantidad"]
      #print(precio)
    '''precioSalpicon = precio + precio
    print("El precio del salpicon es :")
    print(precioSalpicon)'''
  elif opcion==3 :
    for fruta in salpicon: 
      print (fruta)
    
      
  
    
      
      