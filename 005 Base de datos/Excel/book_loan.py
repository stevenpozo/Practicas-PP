import pandas as pd

def update_book_status(book_file, loan_file, output_file_excel):
    # Leer los archivos Excel
    book_df = pd.read_excel(book_file)
    loan_df = pd.read_excel(loan_file)

    # Asegurarse de que las columnas necesarias existen
    if 'idbook' not in book_df.columns or 'status' not in book_df.columns:
        raise ValueError("El archivo 'book.xlsx' debe contener las columnas 'idbook' y 'status'.")

    if 'book_idbook' not in loan_df.columns:
        raise ValueError("El archivo 'loan.xlsx' debe contener la columna 'book_idbook'.")

    # Obtener un conjunto de códigos de libros prestados
    loaned_books = set(loan_df['book_idbook'])

    # Actualizar el estado del libro en el DataFrame de book
    book_df['status'] = book_df['idbook'].apply(lambda x: 0 if x in loaned_books else 1)

    # Reemplazar comas por puntos en la columna 'price' (si existe)
    if 'price' in book_df.columns:
        # Convertir la columna 'price' a texto y reemplazar comas por puntos
        book_df['price'] = book_df['price'].astype(str).apply(lambda x: x.replace(',', '.'))

        # Convertir los valores de 'price' a tipo numérico
        book_df['price'] = pd.to_numeric(book_df['price'], errors='coerce')

    # Guardar el resultado en un nuevo archivo Excel con formato adecuado
    book_df.to_excel(output_file_excel, index=False, float_format="%.2f")
    print(f"Archivo Excel actualizado guardado como: {output_file_excel}")


# Archivos de entrada
book_file = "book.xlsx"
loan_file = "loan.xlsx"
output_file_excel = "updated_book.xlsx"

# Ejecutar la función
update_book_status(book_file, loan_file, output_file_excel)
