def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    return [num for num in lista if primo(num)]
if __name__ == "__main__":
    numeros = input("Ingrese una lista de números separados por comas: ")
    lista_numeros = [int(num) for num in numeros.split(",")]
    primos = filtrar_primos(lista_numeros)
    print("Números primos:", primos)
"""
Defini la funcion 'primo' que verifica si un numero entero es primo, devolviendo 
True si lo es y False si no lo es. Para ello, comprueba si el numero es 
menor que 2 y luego verifica si tiene divisores desde 2 hasta su raiz cuadrada.
Tambien defini la funcion 'filtrar_primos', que recibe una lista de numeros y 
devuelve una nueva lista con solo los primos, usando una comprension de lista.
En la parte principal del programa, pedi al usuario una lista de numeros separados 
por comas, los convierti a enteros, aplique 'filtrar_primos' y luego imprimi la 
lista de numeros primos encontrados.
"""