create database clientes_bigdata;

use clientes_bigdata;

create table clientes (
	id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100),
    correo VARCHAR(150),
    edad INT,
    salario DECIMAL(10,2),
    fecha_registro DATE,
    estado_cliente VARCHAR(50),
    puntuacion DECIMAL(5,2),
    telefono VARCHAR(20)
);


select * from clientes_bigdata.clientes;

SELECT COUNT(*) AS total_registros FROM clientes;
