import numpy as np
from MathParser import PyMathParser

# Inicializamos el analizador de funciones 
mathparser = PyMathParser()
mathparser.addDefaultFunctions()
mathparser.addDefaultVariables()


# Datos de entrada
x = [1.00, 1.20, 1.40, 1.60, 1.80]
y = [0.242, 0.1942, 0.1497, 0.1109, 0.079]


# Completamos la tabla para las funciones
f1_expression = 'ln(x)'
f1 = []

mathparser.expression = f1_expression
for v in x:
    mathparser.variables['x'] = v
    f1.append(mathparser.evaluate())

f2_expression = 'pow(e, (x * -1))'
f2 = []

mathparser.expression = f2_expression
for v in x:
    mathparser.variables['x'] = v
    f2.append(mathparser.evaluate())



# Presentamos los Datos de entrada
print()
print('Presentamos los Datos de entrada')
print()
print("x = %s" % x)
print()
print("y = %s" % y)
print()
print("f1 = [%s] | %s" % (f1_expression, f1))
print()
print("f2 = [%s] | %s" % (f2_expression, f2))
print()
print("w(x) | 1  1  1  1  1")
print()
print()

# Resolvemos los producto escalares:

n = len(x)
f1_f1 = 0
f1_f2 = 0
f2_f1 = 0
f2_f2 = 0

f_f1 = 0
f_f2 = 0

for k in range(n):  # Sumatoria
    f1_f1 += f1[k] * f1[k]
    f1_f2 += f1[k] * f2[k]
    f2_f1 += f2[k] * f1[k]
    f2_f2 += f2[k] * f2[k]

    f_f1 += y[k] * f1[k]
    f_f2 += y[k] * f2[k]

# Armamos las matrices

A = np.array([
    [f1_f1, f2_f1],
    [f1_f2, f2_f2]
])

print('Matriz A')
print(A)

B = np.array([
    [f_f1],
    [f_f2]
])
print()
print('Matriz B')
print(B)

A_inv = np.linalg.inv(A)  # Obtenemos la inversa de la matriz A = A-1

C = np.dot(A_inv,B)  # Producto punto entre las dos matrices

print()
print()
print('Matriz C')
print(C)
print()

c0 = C[0][0]
c1 = C[1][0]

print('la función que mejor representa a los datos respecto del subespacio dado, por el método de los minimos cuadrados es')
print()
print("y = %s * %s + %s * %s" %(c0, f1_expression, c1, f2_expression))
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

result = (c0 * f1_x) + (c1 * f2_x)

print("f(x=%s) = %s" % (q, result))
print()

q = 2
mathparser.expression = f1_expression
mathparser.variables['x'] = q
f1_x = mathparser.evaluate()

mathparser.expression = f2_expression
mathparser.variables['x'] = q
f2_x = mathparser.evaluate()

result = (c0 * f1_x) + (c1 * f2_x)

print("f(x=%s) = %s" % (q, result))
print()

#Calculamos el error del metodo

print('Calculamos el error del método')

delta = 0

for k in range(n):  # Sumatoria
    """
    Sumatoria: += 
    ----
    (c0 * y[k] * f1[k]) => c0 <f,f1>
    ----
    (c1 * y[k] * f2[k]) => c1 <f,f2>
    """
    delta += (y[k])*y[k] - ((c0 * y[k] * f1[k]) + (c1 * y[k] * f2[k]))


e = abs(np.sqrt(delta))

print("El error del método es de: %s" %e)
print()
