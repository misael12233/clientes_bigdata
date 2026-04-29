# Importamos la función conectar desde el archivo prueba.py
from conexion import conectar
import matplotlib.pyplot as plt
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
    df_limpio["edad"] = df_limpio["edad"].astype(str).str.strip()
    df_limpio["salario"] = df_limpio["salario"].astype(str).str.strip()
    df_limpio["fecha_registro"] = df_limpio["fecha_registro"].astype(str).str.strip()
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].str.strip()
    df_limpio["puntuacion"] = df_limpio["puntuacion"].fillna(0.0)
    df_limpio["telefono"] = df_limpio["telefono"].str.strip()
    

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
    df_limpio["nombre"] = df_limpio["nombre"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["apellido"] = df_limpio["apellido"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["ciudad"] = df_limpio["ciudad"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["correo"] = df_limpio["correo"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["edad"] = df_limpio["edad"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["salario"] = df_limpio["salario"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["fecha_registro"] = df_limpio["fecha_registro"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["puntuacion"] = df_limpio["puntuacion"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    df_limpio["telefono"] = df_limpio["telefono"].replace(["", " ", "nan", "NaN", "NULL", "None"], pd.NA).replace(r"^\s*$", pd.NA, regex=True)
    print("\n========= Valores vacíos reemplazados por nulos reales =========")
    print(df_limpio.head(30))

    # Asignar valores por defecto donde sea necesario, por ejemplo: ciudad = "Desconocido", estado_cliente = "Sin Estado"
    df_limpio["nombre"] = df_limpio["nombre"].fillna("Desconocido")
    df_limpio["apellido"] = df_limpio["apellido"].fillna("Desconocido")
    df_limpio["ciudad"] = df_limpio["ciudad"].fillna("Desconocido")
    df_limpio["correo"] = df_limpio["correo"].fillna("desconocido")
    df_limpio["edad"] = df_limpio["edad"].fillna(0)
    df_limpio["salario"] = df_limpio["salario"].fillna(0.0)
    df_limpio["fecha_registro"] = df_limpio["fecha_registro"].fillna(pd.NA)
    df_limpio["estado_cliente"] = df_limpio["estado_cliente"].fillna("Sin Estado")
    df_limpio["puntuacion"] = df_limpio["puntuacion"].fillna(0.0)
    df_limpio["telefono"] = df_limpio["telefono"].fillna("desconocido")
    
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

    #mostrar 20 correos de la tabla
    print("\n========= 20 CORREOS DE LA TABLA =========")
    print(df_limpio["correo"].head(20))

    # colocar "invalido" a correos que esten vacios antes del @
    df_limpio["correo"] = df_limpio["correo"].where(~df_limpio["correo"].str.startswith("@", na=False), "invalido")
    print("\n========= Correos con formato inválido corregidos (correos que empiezan con '@' ahora son 'invalido') =========")
    print(df_limpio["correo"].head(20))

    # organizar los datos por id_cliente de forma ascendente
    df_limpio = df_limpio.sort_values(by="id_cliente", ascending=True)
    print("\n========= Datos organizados por id_cliente de forma ascendente =========")
    print(df_limpio.head(10))


    return df_limpio

def p3_transformacion(df_limpio):
    

    # crear una columna llamada nombre_completo uniendo nombre y apellido
    df_limpio["nombre_completo"] = df_limpio["nombre"] + " " + df_limpio["apellido"]
    print("\n========= Columna 'nombre_completo' creada uniendo 'nombre' y 'apellido' =========")
    print(df_limpio[["nombre", "apellido", "nombre_completo"]].head(20))

    # crear una columna llamada longitud_nombre con la cantidad de caracteres del nombre completo
    df_limpio["longitud_nombre"] = df_limpio["nombre_completo"].str.len()
    print("\n========= Columna 'longitud_nombre' creada con la cantidad de caracteres del 'nombre_completo' =========")
    print(df_limpio[["nombre_completo", "longitud_nombre"]].head(20))

    # crear una columna llamada año_registro apartir de la columna fecha_registro
    df_limpio["año_registro"] = pd.to_datetime(df_limpio["fecha_registro"], dayfirst=True, errors="coerce").dt.year
    df_limpio["año_registro"] = df_limpio["año_registro"].fillna(0)
    print("\n========= Columna 'año_registro' creada a partir de la columna 'fecha_registro' =========")
    print(df_limpio[["fecha_registro", "año_registro"]].head(20))

    return df_limpio

def p4_analisis_basico(df_limpio):

    #mostrar cuantos clientes hay por ciudad
    clientes_por_ciudad = df_limpio["ciudad"].value_counts()
    print("\n========= Cantidad de clientes por ciudad =========")
    print(clientes_por_ciudad)

    # mostrar cuantos clientes hay por estado
    clientes_por_estado = df_limpio["estado_cliente"].value_counts()
    print("\n========= Cantidad de clientes por estado_cliente =========")  
    print(clientes_por_estado)

    #mostrar los 10 clientes con mayor puntuacion
    top_clientes_puntuacion = df_limpio.sort_values(by="puntuacion", ascending=False).head(10)
    print("\n========= Top 10 clientes con mayor puntuacion =========")
    print(top_clientes_puntuacion[["nombre_completo", "puntuacion"]])

    # mostrar cuantos clientes tienen ciudad desconocida
    clientes_ciudad_desconocida = df_limpio[df_limpio["ciudad"] == "Desconocido"]
    print("\n========= Cantidad de clientes con ciudad desconocida =========")
    print(f"Cantidad: {len(clientes_ciudad_desconocida)}")


    return df_limpio

def p5_guardado(df_limpio):

    # Guardar el DataFrame final en un nuevo archivo CSV
    df_limpio.to_csv("clientes_limpio.csv", index=False)
    print("\n========= DataFrame final guardado como 'clientes_limpio.csv' =========")
    print(df_limpio.head(39))

    # guardar un resumen por ciudad en un archivo csv llamado resumen_clientes_por_ciudad.csv
    resumen_clientes_por_ciudad = df_limpio["ciudad"].value_counts().reset_index()
    resumen_clientes_por_ciudad.columns = ["ciudad", "cantidad_clientes"]
    resumen_clientes_por_ciudad.to_csv("resumen_clientes_por_ciudad.csv", index=False)
    print("\n========= Resumen de clientes por ciudad guardado como 'resumen_clientes_por_ciudad.csv' =========")
    print(resumen_clientes_por_ciudad.head(20))

    return df_limpio

def p6_visualizacion_datos(df_limpio):

    # #generar un grafico de barras con la cantidad de clientes por ciudad
    
    clientes_por_ciudad = df_limpio["ciudad"].value_counts()
    plt.figure(figsize=(10, 6))
    clientes_por_ciudad.plot(kind="bar")
    plt.title("Cantidad de Clientes por Ciudad")
    plt.xlabel("Ciudad")
    plt.ylabel("Cantidad de Clientes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("clientes_por_ciudad.png")
    print("\n========= Gráfico de barras 'clientes_por_ciudad.png' generado con la cantidad de clientes por ciudad =========")  
    plt.show()

    #generar un grafico de torta con la distribucion de clientes por estado
    clientes_por_estado = df_limpio["estado_cliente"].value_counts()
    plt.figure(figsize=(10, 6))
    clientes_por_estado.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Distribución de Clientes por Estado")
    plt.ylabel("")
    plt.savefig("clientes_por_estado.png")
    print("\n========= Gráfico de torta 'clientes_por_estado.png' generado con la distribución de clientes por estado =========")
    plt.show()

    return df_limpio






def main():
    # Cargar los datos desde el CSV
    df = p1_cargar_datos()
    # Explorar y depurar los datos
    df_limpio = p2_exploracion_depuracion(df)
    # Transformar los datos
    df_limpio = p3_transformacion(df_limpio)
    # Realizar el análisis básico
    df_limpio = p4_analisis_basico(df_limpio)
    # Guardar el DataFrame final
    df_limpio = p5_guardado(df_limpio)
    # Visualizar los datos
    p6_visualizacion_datos(df_limpio)

if __name__ == "__main__":
    main()