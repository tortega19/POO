def calculadora(a, b, operador):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    elif operador == "/":
        if b == 0:
            return "Error: División por cero"
        return a / b
    else:
        return "Error: Operador no válido"
if __name__ == "__main__":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /): ")
    resultado = calculadora(a, b, operador)
    print(f"El resultado es: {resultado}")
"""
Defini la funcion 'calculadora' para recibir dos numeros y un operador.
Dentro de la funcion, use condicionales para determinar que operacion se debia
realizar (ya fuera suma, resta, multiplicacion o division) y ejecute la operacion
correspondiente. Tambien me asegure de manejar el caso de division por cero,
asi que si el usuario intentaba dividir entre cero, el programa mostraba un
mensaje de error en lugar de hacer la operacion. Luego pedi al usuario
que ingresara los dos numeros y el operador por teclado y al final mostre
el resultado de la operacion seleccionada.
"""