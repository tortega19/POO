def palindromo(palabra):
    palabra = palabra.lower()  
    longitud = len(palabra)
    
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - 1 - i]:
            return False
    return True
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    if palindromo(palabra):
        print("Es un palindromo.")
    else:
        print("No es un palindromo.")

"""
Defini la funcion 'palindromo' que recibe una palabra como argumento.
Dentro de la funcion, converti la palabra a minusculas para asegurarme de que
la comparacion no sea sensible a mayusculas y minusculas. Luego, calcule la longitud
de la palabra y utilice un bucle para comparar los caracteres desde el inicio
y el final de la palabra, avanzando hacia el centro. Si en algun momento los
caracteres no coinciden, la funcion devuelve False. Si el bucle termina sin
encontrar diferencias, la funcion devuelve True, indicando que la palabra
es un palindromo.
"""