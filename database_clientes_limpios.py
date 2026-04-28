from conexion import conectar
import pandas as pd
from sqlalchemy import create_engine, text

# Leer CSV correctamente
df = pd.read_csv("clientes_limpio.csv", encoding="utf-8", dtype={"telefono": str})

print("✅ CSV cargado")
print(df.head(50))

# Conexión
engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1:3308/clientes_bigdata")

try:
    # Crear tabla
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS clientes_limpios (
            id_cliente INT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            ciudad VARCHAR(100) NOT NULL,
            correo VARCHAR(150) NOT NULL,
            edad INT NOT NULL,
            salario FLOAT NOT NULL,
            fecha_registro DATE NOT NULL,
            estado_cliente VARCHAR(50) NOT NULL,
            puntuacion FLOAT NOT NULL,
            telefono VARCHAR(15) NOT NULL
        )
        """))
    print("✅ Tabla creada")

    # Convertir fecha
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], dayfirst=True, errors="coerce")

    # Insertar datos
    df.to_sql("clientes_limpios", con=engine, if_exists="append", index=False)

    print("✅ Datos insertados correctamente")

except Exception as e:
    print("❌ Error:")
    print(e)