# 
# Ejercicios con Python. ---
# Nombre: Angel Orlando Vazquez Morales
# Correr con el comando => python ejercicios.py ---

# Función 1: Calcular los primeros n numeros primos naturales.
def primos(n):
    primos_en_n = []
    for i in range(n + 1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
        if primo:
            primos_en_n.append(i)
    return primos_en_n

# Función 2: Calcular el producto cruz en vectores de 3 componentes.
def producto_cruz(vec1, vec2):
    x1 = vec1[0]
    y1 = vec1[1]
    z1 = vec1[2]
    x2 = vec2[0] 
    y2 = vec2[1]
    z2 = vec2[2]

    x3 = y1 * z2 - y2 * z1
    y3 = x1 * z2 - x2 * z1
    z3 = x1 * y2 - x2 * y1
    return [x3, y3, z3]

# Función 3: ...

def main():
    file = open("ejercicios_python.txt", "r")
    # print(primos(50))
    vector1 = file.readline().split(',') 
    vector2 = file.readline().split(',') 
    print(producto_cruz(vector1, vector2))

main()
