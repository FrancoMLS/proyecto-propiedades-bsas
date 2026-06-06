CREATE DATABASE IF NOT EXISTS proyecto_propiedades;
USE proyecto_propiedades;

CREATE TABLE IF NOT EXISTS propiedades (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    fecha_creacion_publicacion DATE,
    lat DECIMAL(20,16),
    lon DECIMAL(20,16),
    pais VARCHAR(50),
    ciudad VARCHAR(100),
    barrio VARCHAR(100),
    ambientes INT,
    dormitorios INT,
    banios INT,
    metros_cuadrados_totales DECIMAL(10,2),
    metros_cuadrados_cubiertos DECIMAL(10,2),
    precio DECIMAL(15,2),
    moneda VARCHAR(50),
    tipo_de_propiedad VARCHAR(50),
    operacion VARCHAR(50)  
);