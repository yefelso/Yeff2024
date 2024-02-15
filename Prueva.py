# Números de emergencia en Perú
numeros_emergencia = {
    "Policía Nacional del Perú": "105",
    "Bomberos": "116",
    "Ambulancias": "117",
    "Emergencias Médicas (SAMU)": "106",
}

# Imprimir los números en la pantalla
print("Números de emergencia en Perú:")
for servicio, numero in numeros_emergencia.items():
    print(f"{servicio}: {numero}")
