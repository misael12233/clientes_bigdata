from conexion import conectar
import pandas as pd
from sqlalchemy import create_engine

# ==========================================================
# ARCHIVO: guardar_database.py

#leemos el csv con pandas
df = pd.read_csv("clientes_bigdata_1000.csv", encoding="latin-1", sep=";")
print("✅ CSV cargado (datos originales)")
print(df.head(5))

# Creamos una conexión a la base de datos usando SQLAlchemy
engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1:3308/clientes_bigdata")
print("✅ Conexión creada")

# Guardamos el DataFrame en la tabla "clientes" de MySQL
try:
    df["fecha_registro"] = pd.to_datetime(
    df["fecha_registro"],
    format="%d/%m/%Y",
    errors="coerce"
    )
    df.to_sql(
        name="clientes", 
        con=engine, 
        if_exists="append", 
        index=False)
    print("✅ Datos guardados en MySQL correctamente")
except Exception as e:
    print(f"❌ Error al guardar datos en MySQL: {e}")   


