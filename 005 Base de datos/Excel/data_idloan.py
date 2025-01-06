import pandas as pd

# Cargar el archivo Excel
archivo = 'biblioteca.xlsm'

# Leer las hojas del archivo
df_reportes = pd.read_excel(archivo, sheet_name='REPORTES')
df_libro = pd.read_excel(archivo, sheet_name='LIBRO')
df_usuarios = pd.read_excel(archivo, sheet_name='USUARIOS')

# Crear un diccionario que mapea el CÓDIGO LIBRO al id del libro
codigo_libro_a_id = dict(zip(df_libro['CODIGO GENERAL'], df_libro['id']))

# Crear un diccionario que mapea el APELLIDO Y NOMBRE del usuario al id del usuario
solicitante_a_id_usuario = dict(zip(df_usuarios['APELLIDO Y NOMBRE'], df_usuarios['id']))

# Crear un diccionario que mapea el APELLIDO Y NOMBRE al nombre completo del usuario
solicitante_a_nombre_completo = dict(zip(df_usuarios['APELLIDO Y NOMBRE'], df_usuarios['APELLIDO Y NOMBRE']))

# Reemplazar el CÓDIGO LIBRO en REPORTES por el id correspondiente
df_reportes['CÓDIGO LIBRO'] = df_reportes['CÓDIGO LIBRO'].map(codigo_libro_a_id)

# Reemplazar el SOLICITANTE en REPORTES por el id correspondiente
df_reportes['ID SOLICITANTE'] = df_reportes['SOLICITANTE'].map(solicitante_a_id_usuario)

# Añadir la columna con el nombre completo del solicitante
df_reportes['NOMBRE COMPLETO SOLICITANTE'] = df_reportes['SOLICITANTE'].map(solicitante_a_nombre_completo)

# Guardar el resultado en un nuevo archivo Excel
nuevo_archivo = 'reportes27.xlsx'
df_reportes.to_excel(nuevo_archivo, index=False)

print(f"El archivo de reportes actualizado se guardó como {nuevo_archivo}")
