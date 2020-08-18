import numpy as np
from MathParser import PyMathParser

# Inicializamos el analizador de funciones
mathparser = PyMathParser()
mathparser.addDefaultFunctions()
mathparser.addDefaultVariables()

# Datos de entrada
x = [1.00, 2.00, 3.00, 4.00, 5.00]
y = [2.00, 3.00, 5.00, 7.00, 3.00]


# Completamos la tabla para las funciones básicas 
f1_expression = '1'
f1 = []

mathparser.expression = f1_expression
for v in x:
    mathparser.variables['x'] = v
    f1.append(mathparser.evaluate())

f2_expression = 'x'
f2 = []

mathparser.expression = f2_expression
for v in x:
    mathparser.variables['x'] = v
    f2.append(mathparser.evaluate())

f3_expression = '(x - 4)'
f3 = []

mathparser.expression = f3_expression
for v in x:
    mathparser.variables['x'] = v
    f3.append(mathparser.evaluate())


# Presentamos los Datos de entrada 
print()
print()
print('Presentamos los Datos de entrada')
print()
print("x = %s" % x)
print()
print("y = %s" % y)
print()
print("f1 [%s] = %s" % (f1_expression, f1))
print()
print("f2 [%s] = %s" % (f2_expression, f2))
print()
print("f3 [%s] = %s" % (f3_expression, f3))
print()
print()

# Resolvemos los productos escalares

n = len(x)
f1_f1 = 0
f1_f2 = 0
f1_f3 = 0
f2_f1 = 0
f2_f2 = 0
f2_f3 = 0
f3_f1 = 0
f3_f2 = 0
f3_f3 = 0

f_f1 = 0
f_f2 = 0
f_f3 = 0

for k in range(0, n):  # Sumatoria
    f1_f1 += f1[k] * f1[k]
    f1_f2 += f1[k] * f2[k]
    f1_f3 += f1[k] * f3[k]
    f2_f1 += f2[k] * f1[k]
    f2_f2 += f2[k] * f2[k]
    f2_f3 += f2[k] * f3[k]
    f3_f1 += f3[k] * f1[k]
    f3_f2 += f3[k] * f2[k]
    f3_f3 += f3[k] * f3[k]

    f_f1 += y[k] * f1[k]
    f_f2 += y[k] * f2[k]
    f_f3 += y[k] * f3[k]

A = np.array([
    [f1_f1, f2_f1, f3_f1],
    [f1_f2, f2_f2, f3_f2],
    [f1_f3, f2_f3, f3_f3],
])

print()
print('Matriz A')
print(A)

"""
Matriz A

    5 15 -5
    15 55 -5
    -5 -5 15

"""

B = np.array([
    [f_f1],
    [f_f2],
    [f_f3],
])
print()
print('Matriz B')
print(B)

"""
Matriz B
[
    20
    66
    -14
]
"""

A_inv = np.linalg.inv(A)  # Obtenemos la inversa de la matriz A = A-1

C = np.dot(A_inv,B)  # Producto punto entre las dos matrices

print()
print()
print('Matriz C')
print(C)
"""
Matriz C
[
    -12
     3
    -1
]
"""
print()
print()

c0 = C[0][0]
c1 = C[1][0]
c2 = C[2][0]

print('la función que mejor representa a los datos respecto del subespacio dado, por el método de los minimos cuadrados es')
print("y = %s * %s + %s * %s + %s * %s" %(c0, f1_expression, c1, f2_expression, c2, f3_expression))
print()

print('Aproximamos algunos valores')
print()

q = 1.3
mathparser.expression = f1_expression
mathparser.variables['x'] = q
f1_x = mathparser.evaluate()

mathparser.expression = f2_expression
mathparser.variables['x'] = q
f2_x = mathparser.evaluate()

mathparser.expression = f3_expression
mathparser.variables['x'] = q
f3_x = mathparser.evaluate()

result = (c0 * f1_x) + (c1 * f2_x) + (c2 * f3_x)

print("f(x=%s) = %s" % (q, result))
print()

# Calculamos el error del metodo
print('Calculamos el error del método')
print()

delta = 0

for k in range(0, n):  # Sumatoria
    """
    Sumatoria: += 
    ---
    y[k])**2 => f(x)^2
    ----
    (c0 * y[k] * f1[k]) => c0 <f,f1>
    ----
    (c1 * y[k] * f2[k]) => c1 <f,f2>
    ----
    (c2 * y[k] * f3[k]) => c2 <f,f3>
    """
    delta += (y[k])**2 - ((c0 * y[k] * f1[k]) + (c1 * y[k] * f2[k]) + (c2 * y[k] * f3[k]))

e = np.sqrt(abs(delta))

print("El error del método es de: %s" %e)
print()
# El error del método es de: 11.135528725660043
