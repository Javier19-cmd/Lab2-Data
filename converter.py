import pandas as pd

def convert_xlsx_to_csv(input_file, output_file):
    # Leer el archivo XLSX utilizando pandas
    df = pd.read_excel(input_file)
    
    # Guardar el DataFrame en un archivo CSV
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Ruta del archivo XLSX de entrada
    input_file_path = "./consumo.xlsx"
    
    # Ruta del archivo CSV de salida
    output_file_path = "./consumo.csv"
    
    # Llamar a la función para convertir el archivo
    convert_xlsx_to_csv(input_file_path, output_file_path)