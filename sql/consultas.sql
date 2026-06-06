-- Precio promedio por tipo de propiedad
SELECT tipo_de_propiedad, AVG(precio) AS precio_promedio FROM propiedades GROUP BY tipo_de_propiedad ORDER BY precio_promedio DESC;

-- Precio promedio por cantidad de ambientes
SELECT ambientes, AVG(precio) AS precio_promedio_por_ambientes FROM propiedades GROUP BY ambientes ORDER BY precio_promedio_por_ambientes DESC;

-- Precio promedio por barrio
SELECT barrio, AVG(precio) AS precio_promedio_por_barrio FROM propiedades GROUP BY barrio ORDER BY precio_promedio_por_barrio DESC;

-- Cantidad de propiedades por ciudad
SELECT ciudad, COUNT(*) AS cantidad_propiedades FROM propiedades GROUP BY ciudad ORDER BY cantidad_propiedades DESC;

-- Cantidad de propiedades por barrio
SELECT barrio, COUNT(*) AS cantidad_propiedades FROM propiedades GROUP BY barrio ORDER BY cantidad_propiedades DESC;