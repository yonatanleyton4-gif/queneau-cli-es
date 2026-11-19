import time
from tqdm import tqdm

print("¡HOLA BRO, BIENVENIDO ;) !")
print("!Cargando modulos¡\n")

# Simulamos que estamos cargando 20 cosas
for i in tqdm(range(20), desc="Cargando elementos"):
    time.sleep(0.2)  # Hace una pausa de 0.2 segundos para que la barra se vea avanzar

print("\n✅ ¡Carga completada!")