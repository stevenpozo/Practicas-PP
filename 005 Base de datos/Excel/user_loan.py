import pandas as pd

# Cargar el archivo Excel
ruta_archivo = "user.xlsx"  # Reemplaza con la ruta de tu archivo
df = pd.read_excel(ruta_archivo)

# Función para dividir nombres y apellidos
def separar_nombre_apellido(nombre_completo):
    partes = nombre_completo.split()
    apellidos = " ".join(partes[:2])  # Primeros dos elementos como apellidos
    nombres = " ".join(partes[2:])   # El resto como nombres
    return pd.Series([apellidos, nombres])

# Aplicar la separación
df[['Apellidos', 'Nombres']] = df['APELLIDO Y NOMBRE'].apply(separar_nombre_apellido)

# Guardar el archivo actualizado
df.to_excel("usuarios_actualizado.xlsx", index=False)
print("Archivo actualizado guardado como 'usuarios_actualizado.xlsx'")
