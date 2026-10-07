# Daniel Gallegos NC 1392 
# Estructuras if, elif, else
# if Ejemplo 1
a = 33
b = 200
if b > a:
  print("b es mayor que a")
# if Ejemplo 2
numero = 15
if numero > 0:
  print("El numero es positivo")
# if elif Ejemplo 1
a = 33
b = 33
if b > a:
  print("b es mayor que a")
elif a == b:
  print("a y b son iguales")
# if elif Ejemplo 2
calificacion = 75
if calificacion >= 90:
  print("Excelente")
elif calificacion >= 80:
  print("Muy bien")
elif calificacion >= 70:
  print("Bien")
elif calificacion >= 60:
  print("Puedes mejorar")
# if else Ejemplo 1
a = 200
b = 33
if b > a:
  print("b es mayor quw a")
elif a == b:
  print("a y b son iguales")
else:
  print("a es mayor que b")
# if else Ejemplo 2
a = 200
b = 33
if b > a:
  print("b es mayor que a")
else:
  print("b no es mayor que a")
# loops Ejemplo 1
fruits = ["manzana", "durazno", "cereza"]
for x in fruits:
  print(x)
# loops Ejemplo 2
fruits = ["manzana", "durazno", "cereza"]
for x in fruits:
  if x == "durazno":
    break
  print(x)
#ciclo while Ejemplo 1
i = 1
while i < 6:
  print(i)
  i += 1
# ciclo while Ejemplo 2 
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# Daniel Gallegos NC 1392