# ==========================================================
# ARCHIVO: prueba.py
# OBJETIVO:
# Este archivo contiene una función para conectarse a MySQL.
# La idea es separar la conexión del resto del programa
# para que el código quede más organizado y reutilizable.
# ==========================================================

import mysql.connector
from mysql.connector import Error


def conectar():
    """
    Esta función intenta conectarse a la base de datos MySQL.
    Si la conexión es exitosa, devuelve el objeto de conexión.
    Si ocurre un error, devuelve None.
    """

    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",               # Dirección del servidor MySQL
            port=3308,                     # Puerto de MySQL en XAMPP
            user="root",                   # Usuario de MySQL
            password="",                   # Contraseña del usuario
            database="clientes_bigdata",   # Nombre de la base de datos
            charset="utf8mb4",             # Soporte para caracteres especiales
            use_unicode=True,              # Soporte Unicode
            autocommit=False               # No confirmar cambios automáticamente
        )

        print("✅ Conectado a MySQL correctamente")
        return conn

    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None


# Este bloque solo se ejecuta si abrimos este archivo directamente
if __name__ == "__main__":
    conn = conectar()

    if conn:
        print("Conexión de prueba exitosa")

        # Creamos un cursor para ejecutar una consulta simple
        cursor = conn.cursor(dictionary=True)

        # Consulta para verificar hora del servidor
        cursor.execute("SELECT NOW() AS fecha_hora_actual;")

        # Mostramos el resultado
        resultado = cursor.fetchone()
        print(resultado)

        # Cerramos cursor y conexión
        cursor.close()
        conn.close()
        print("✅ Conexión cerrada")