def mismos_caracteres(lista):
    resultado = []
    for palabra in lista:
        if any(sorted(palabra) == sorted(otra_palabra) for otra_palabra in lista if palabra != otra_palabra):
            resultado.append(palabra)
    return resultado
if __name__ == "__main__":
    palabras = input("Introduce palabras separadas por espacios: ").split()
    print("Palabras con los mismos caracteres:", mismos_caracteres(palabras))
"""
Defini la funcion 'mismos_caracteres' que recibe una lista de palabras como argumento.
Dentro de la funcion, cree una lista vacia llamada 'resultado' para almacenar
las palabras que cumplen la condicion. Luego, utilice un bucle para recorrer cada
palabra en la lista, para cada palabra, verifique si hay otra palabra en la lista
que tenga los mismos caracteres, utilizando la funcion 'sorted' y si encuentro una
coincidencia, agrego la palabra a la lista 'resultado'. Luego, la funcion devuelve
la lista de palabras que tienen los mismos caracteres, despues pedi al usuario que
ingresara palabras separadas por espacios en la consola, las dividi en una lista y aplique
'mismos_caracteres'. Finalmente, imprimi la lista de palabras que cumplen la condicion.
"""
