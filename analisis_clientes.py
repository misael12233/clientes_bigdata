# Importamos la función conectar desde el archivo prueba.py
from conexion import conectar

# Importamos pandas para trabajar los datos como tabla
import pandas as pd



def p1_cargar_datos():
    # Cargamos los datos desde el archivo CSV
    df = pd.read_csv("clientes_bigdata_1000.csv", encoding="latin-1", sep=";", dtype={"telefono": str})
    print("✅ CSV cargado (datos originales)")
    print(df.head(5))

    # Mostrar cantidad de filas y columnas
    print("\n===== DIMENSIONES DEL DATAFRAME =====")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

    # mostrar los tipos de datos
    print("\n===== TIPOS DE DATOS =====")
    print(df.dtypes)

    return df

def p2_exploracion_depuracion(df):
    # Creamos una copia del DataFrame para trabajar los datos limpios
    df_limpio = df.copy()

    # identificar cuantos valores nulos existen por columna
    print("\n===== VALORES NULOS POR COLUMNA =====")    
    print(df.isnull().sum())

    # Limpiar espacios al inicio y al final en las columnas de texto
    df_limpio["nombre"] = df_limpio["nombre"].str.strip()
    df_limpio["apellido"] = df_limpio["apellido"].str.strip()
    df_limpio["ciudad"] = df_limpio["ciudad"].str.strip()
    df_limpio["correo"] = df_limpio["correo"].str.strip()
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].str.strip()
    print("\n========= Espacios en blanco eliminados en columnas de texto =========")
    print(df_limpio.head(10))

    # Unificar formato de texto en columnas como nombre, apellido, ciudad y estado_cliente
    df_limpio["nombre"] = df_limpio["nombre"].str.title()
    df_limpio["apellido"] = df_limpio["apellido"].str.title()
    df_limpio["ciudad"] = df_limpio["ciudad"].str.title()
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].str.title()
    print("\n========= Formato de texto unificado en columnas de texto =========")
    print(df_limpio.head(10))

    # Reemplazar valores como None, NULL, NaN y vacíos por nulos reales.
    df_limpio["nombre"] = df_limpio["nombre"].replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["apellido"] = df_limpio["apellido"].replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["ciudad"] = df_limpio["ciudad"].replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["correo"] = df_limpio["correo"].replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].replace(r"^\s*$", pd.NA, regex=True)
    print("\n========= Valores vacíos reemplazados por nulos reales =========")
    print(df_limpio.head(10))

    # Asignar valores por defecto donde sea necesario, por ejemplo: ciudad = "Desconocido", estado_cliente = "Sin Estado"
    df_limpio["ciudad"] = df_limpio["ciudad"].fillna("Desconocido")
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].fillna("Sin Estado")
    df_limpio["correo"] = df_limpio["correo"].fillna("desconocido")
    print("\n========= Valores por defecto asignados en columnas ciudad y estado_cliente =========")
    print(df_limpio.head(10))

    # Eliminar registros duplicados.
    df_limpio = df_limpio.drop_duplicates()
    print("\n========= Registros duplicados eliminados =========")
    print(df_limpio.head(10))

    # Revisar y mostrar cuántos correos no cumplen con un formato básico válido.
    correos_invalidos = df_limpio[~df_limpio["correo"].str.contains("@", na=False)]
    print("\n========= Correos inválidos encontrados =========")
    print(f"Cantidad: {len(correos_invalidos)}")
    print(correos_invalidos["correo"].head(10))

    # mostrar el total de registros después de la depuración
    print("\n===== TOTAL DE REGISTROS DESPUÉS DE LA DEPURACIÓN =====")
    print(f"Total registros: {len(df_limpio)}")

    # mostrar la información del DataFrame limpio después de la depuración
    print("\n===== INFORMACIÓN DEL DATAFRAME LIMPIO =====")
    print(df_limpio.info())

    # Crear una versión depurada del DataFrame.
    df_limpio.to_csv("clientes_limpio.csv", index=False)
    print("\n========= DataFrame depurado y guardado como 'clientes_limpio.csv' =========")

    return df




def main():
    # Cargar los datos desde el CSV
    df = p1_cargar_datos()
    # Explorar y depurar los datos
    p2_exploracion_depuracion(df)

if __name__ == "__main__":
    main()