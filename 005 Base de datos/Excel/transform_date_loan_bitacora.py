import pandas as pd
from datetime import datetime

# Función para convertir el formato de la fecha
def convertir_fecha(fecha_str):
    try:
        # Limpiar la cadena: eliminar los guiones y los espacios extra
        fecha_str = fecha_str.replace(' - ', ' ').strip()
        
        # Asegúrate de que la fecha esté en el formato correcto
        print(f"Intentando convertir: {fecha_str}")  # Verificar qué datos se están procesando
        fecha_obj = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M:%S")
        
        # Regresa el formato deseado 'YYYY-MM-DD HH:MM:SS'
        return fecha_obj.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        # Si no es un formato válido, muestra el error y devuelve None
        print(f"Error de conversión para '{fecha_str}': {e}")
        return None

# Leer el archivo Excel
archivo_excel = 'bitacora.xlsx'  # Nombre del archivo Excel de entrada
df = pd.read_excel(archivo_excel)  # Lee todo el archivo sin especificar hoja

# Verifica las primeras filas para asegurarte de que el archivo se cargó correctamente
print("Primeras filas del archivo:")
print(df.head())

# Verifica si las columnas 'FECHA DE PRESTAMO' y 'FECHA DEVOLUCIÓN' existen y si tienen datos
if 'FECHA DE PRESTAMO' in df.columns:
    print(f"Columna 'FECHA DE PRESTAMO' encontrada con {len(df['FECHA DE PRESTAMO'])} registros.")
else:
    print("La columna 'FECHA DE PRESTAMO' no se encuentra en el archivo.")

if 'FECHA DEVOLUCIÓN' in df.columns:
    print(f"Columna 'FECHA DEVOLUCIÓN' encontrada con {len(df['FECHA DEVOLUCIÓN'])} registros.")
else:
    print("La columna 'FECHA DEVOLUCIÓN' no se encuentra en el archivo.")

# Aplicar la conversión solo si las columnas existen
if 'FECHA DE PRESTAMO' in df.columns:
    df['FECHA DE PRESTAMO'] = df['FECHA DE PRESTAMO'].apply(convertir_fecha)

if 'FECHA DEVOLUCIÓN' in df.columns:
    df['FECHA DEVOLUCIÓN'] = df['FECHA DEVOLUCIÓN'].apply(convertir_fecha)

# Verifica los datos después de la conversión
print("Primeras filas después de la conversión:")
print(df.head())

# Guardar el archivo Excel con las fechas convertidas
archivo_salida = 'bitacora_datetime.xlsx'  # Nombre del archivo Excel de salida
df.to_excel(archivo_salida, index=False)

print(f"Las fechas han sido convertidas y guardadas en {archivo_salida}")
