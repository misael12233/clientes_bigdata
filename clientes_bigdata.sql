

select * from clientes_bigdata.clientes;

select * from clientes_bigdata.clientes_limpios;


SELECT COUNT(*) AS total_registros FROM clientes_limpios;
SELECT COUNT(*) AS total_registros FROM clientes;
truncate table clientes_limpios;
truncate table clientes;