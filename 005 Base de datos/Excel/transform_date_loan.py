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
archivo_excel = 'loan.xlsx'  # Nombre del archivo Excel de entrada
df = pd.read_excel(archivo_excel)

# Verifica las primeras filas para asegurarte de que el archivo se cargó correctamente
print("Primeras filas del archivo:")
print(df.head())

# Verifica si la columna 'aqcisition_date' existe y si tiene datos
if 'aqcisition_date' in df.columns:
    print(f"Columna 'aqcisition_date' encontrada con {len(df['aqcisition_date'])} registros.")
else:
    print("La columna 'aqcisition_date' no se encuentra en el archivo.")

# Aplicar la conversión solo si la columna existe
if 'aqcisition_date' in df.columns:
    df['aqcisition_date'] = df['aqcisition_date'].apply(convertir_fecha)

# Verifica los datos después de la conversión
print("Primeras filas después de la conversión:")
print(df.head())

# Guardar el archivo Excel con las fechas convertidas
archivo_salida = 'datetime_loan.xlsx'  # Nombre del archivo Excel de salida
df.to_excel(archivo_salida, index=False)

print(f"Las fechas han sido convertidas y guardadas en {archivo_salida}")
