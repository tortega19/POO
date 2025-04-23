def mayor_suma(lista):
    if len(lista) < 2:
        return None  
    max_suma = lista[0] + lista[1]  
    for i in range(1, len(lista) - 1):
        suma = lista[i] + lista[i + 1]
        if suma > max_suma:
            max_suma = suma
    return max_suma
if __name__ == "__main__":
    numeros = input("Introduce una lista de números separados por espacios: ")
    lista = list(map(int, numeros.split()))
    resultado = mayor_suma(lista)
    if resultado is not None:
        print(f"La mayor suma de dos números consecutivos es: {resultado}")
    else:
        print("La lista debe contener al menos dos números.")
"""
Defini la funcion 'mayor_suma' que recibe una lista de numeros como argumento.
Dentro de la funcion, verifique si la lista tiene al menos dos elementos. Si no es asi,
devuelvo None. Luego, inicialice 'max_suma' con la suma de los dos primeros elementos
de la lista. A continuacion, utilice un bucle para recorrer la lista y calcular
la suma de cada par de elementos consecutivos. Si la suma actual es mayor que
'max_suma', actualizo 'max_suma'. Al final, la funcion devuelve la mayor suma
encontrada. En la parte principal del programa, pedi al usuario que ingresara
una lista de numeros separados por espacios, los convierti a enteros y aplique
'mayor_suma'. Finalmente, imprimi el resultado o un mensaje de error si la lista
no contenia suficientes numeros.
"""