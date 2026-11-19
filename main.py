import subprocess
import sys 


print("Iniciando Sistema :) \n")

resultado = subprocess.run([sys.executable, "main_.py"])

print("  Sistema iniciado ;) \n")


while True:
    print("\nMenu Principal")
    print("1.Tu Texto")
    print("2.generado al azar")
    print("3.Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        texto_usuario = input("Ingresa tu texto: ")
        print(f"Tu texto es:\n {texto_usuario}")
    elif opcion == "2":
        print("Generando texto al azar...\n")
        texto_azar = subprocess.run([sys.executable, "cientpoem.py"])
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
