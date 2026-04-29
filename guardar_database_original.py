from conexion import conectar
import pandas as pd
from sqlalchemy import create_engine, text

# Leer CSV correctamente (🔥 AQUÍ ESTÁ LA CORRECCIÓN)
df = pd.read_csv("clientes_bigdata_1000.csv", encoding="latin-1", sep=";", dtype={"telefono": str})

print("✅ CSV cargado")
print(df.head(50))

# Conexión
engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1:3308/clientes_bigdata")

try:
    # Crear tabla
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT PRIMARY KEY,
            nombre VARCHAR(100),
            apellido VARCHAR(100),
            ciudad VARCHAR(100),
            correo VARCHAR(150),
            edad INT,
            salario FLOAT,
            fecha_registro DATE,
            estado_cliente VARCHAR(50),
            puntuacion FLOAT,
            telefono VARCHAR(15)
        )
        """))
    print("✅ Tabla creada")

    # Convertir fecha
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], dayfirst=True, errors="coerce")

    # Insertar datos
    df.to_sql("clientes", con=engine, if_exists="append", index=False)

    print("✅ Datos insertados correctamente")

except Exception as e:
    print("❌ Error:")
    print(e)