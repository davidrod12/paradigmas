def sumas():
    print("Suma de dos números")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
    return resultado

def restas():
    print("Digite dos numeros para restar")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
    return resultado

def multiplicaciones():
    print("Digite dos numero para multiplicar")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
    return resultado
def division():
    print("Digite dos numero para dividir")
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    resultado = num1 / num2
    print(f"Resultado: {num1} / {num2} = {resultado}")
    return resultado

def main():
    print("1. suma\n2. restas\n3. multiplicacion\n4. division\n5.Salir")
    op = input("Digite la opcion que deseas realizar: (1-5): ")
    if op == "1":
        sumas()
    elif op == "2":
        restas()
    elif op == "3":
        multiplicaciones()
    elif op == "4":
            division()
    elif op == "5":
        print("Saliendo..")  
    else:
        print("Opción no válida. Hasta pronto")


if __name__ == "__main__":
    main()