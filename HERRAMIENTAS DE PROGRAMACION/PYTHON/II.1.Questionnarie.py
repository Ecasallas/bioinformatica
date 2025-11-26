#!/usr/bin/env python3
# -*- Introduction: variables, assignments, expressions -*-
# author: Estefani Casallas Samper
# date: 26th november 2025
#----------------------------------------------------------------------
""" Este script contiene ejercicios introductorios sobre variables, 
 asignaciones y expresiones en Python."""
#----------------------------------------------------------------------


## 1. 
# este es el inicio del código
counter = 0

# luego hay estos tres incrementos
counter = counter + 1
counter = counter + 1
counter = counter + 1
# entonces, el contador vale 3

# al final, este es el resultado
result = 'A' * counter

""" el valor de result es 'AAA', porque el contador vale 3 y 
se multiplica la cadena 'A' por 3, resultando en 'AAA' """


## 2.
# este es el inicio del código
x = 10   #se puede ignorar este valor inicial de x, no afecta al resultado final
operation = 'X' + '+' + '2'

# se operan las cadenas
'X' + '+' + '2'   # resulta en la cadena 'X+2'
# entonces, el valor de operation es 'X+2', que es una cadena
""" el valor de operation es la cadena 'X+2', 
porque se concatenan las cadenas 'X', '+' y '2' """


## 3.
# este es el inicio del código
ten = '10'    #cadena
operation = ten + '/' + '2'

#se analiza el tipo de dato
ten = '10'    #cadena

#se concatenan las cadenas
ten + '/' + '2'   # resulta en la cadena '10/2'
# entonces, el valor de operation es '10/2', que es una cadena
""" el valor de operation es la cadena '10/2', 
porque se concatenan las cadenas '10', '/' y '2' """


## 4.
#se concatrenan las cadenas
result = '10' + '/' + '2'
#se evalúa la expresión matemática
result = eval(result)

print (result)
""" el valor de result es 5.0, porque la función 
eval evalúa la cadena '10/2' como una expresión 
matemática, resultando en 5.0 """


## 5. 
#se analiza los tipos de datos
# address es una cadena (string)
# 2 es un entero (int)
address = 'C/ Mayor, '
address = address + 2
print(address)
""" este código genera un error de tipo (TypeError), 
porque intenta concatenar una cadena 
con un entero, lo cual no es permitido en Python. """


## 6.
#se asigna valor de 4 a la variable x y se define result como una cadena
x = 4
result = 'x * 2'
#se aplica eval para evaluar la expresión matemática en la cadena
result = eval(result)
print(result)
""" el valor de result es 8, 
porque la función eval evalúa la cadena 'x * 2' 
como una expresión matemática, utilizando el valor de x (que es 4),
resultando en 8. """   


## 7.
#se asigna valor de 5 a la variable x
x = 5
#se define result como una cadena que representa una expresión matemática
result = x * 4
# el resultado de x * 4 es 20, pero 20 es un entero, no una cadena
result = eval(eval(result))
print(result)
""" el valor de result es un error de tipo (TypeError), 
porque eval espera una cadena como argumento, 
pero se le está pasando un entero (20). """   


## 8.
#se asigna valor de 3 a la variable x   
x = 3
#se evalúa la expresión 'X + 4'
result = eval('X + 4')
""" el valor de result es un error de nombre (NameError), 
porque 'X' (mayúscula) no está definido en el código. 
La variable definida es 'x' (minúscula). """  


## 9.
#se asigna a x una cadena que representa otra expresión matemática
x = " '2+3' "
#se evalúan las expresiones anidadas
result = eval(eval(x))
print(result)
""" el valor de result es 5, porque la primera evaluación de eval(x) 
convierte la cadena " '2+3' " en la cadena '2+3', y la segunda evaluación 
eval('2+3') calcula la suma, resultando en 5. """


## 10.
#se asigna a x una cadena que representa una tupla de números
x = '2,3,4'
#se evalúan las expresiones anidadas
result = eval(eval(x))
print(result)
""" el valor de result es un error de sintaxis (SyntaxError), 
porque la cadena '2,3,4' no es una expresión válida en Python. 
Para que eval pueda interpretarla correctamente, debería estar 
formateada como una tupla, es decir, '(2,3,4)'. """