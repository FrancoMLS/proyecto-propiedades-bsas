# 🏠 Análisis del Mercado Inmobiliario - Buenos Aires

Proyecto de análisis de datos sobre el mercado inmobiliario de la Ciudad de Buenos Aires y el Gran Buenos Aires. Incluye procesamiento de datos con Python, almacenamiento en MySQL y visualización en Power BI.

## 🎯 Objetivo

Construir un pipeline de datos completo que permita analizar el mercado inmobiliario porteño, identificando precios promedio por barrio, zona y tipo de propiedad a partir de un dataset de más de 146.000 propiedades.

## 🛠️ Tecnologías utilizadas

- **Python** → procesamiento y carga de datos
- **Pandas** → lectura y transformación del archivo CSV
- **MySQL** → almacenamiento de los datos
- **Power BI** → visualización y dashboard (en desarrollo)

## 📁 Estructura del proyecto

```
proyecto-propiedades-bsas/
│
├── .env.example          → variables de entorno necesarias
├── .gitignore
├── README.md
│
├── data/                 → colocar el CSV aquí (ver sección Dataset)
│
├── sql/
│   ├── schema.sql        → estructura de la base de datos
│   └── consultas.sql     → consultas de análisis
│
└── src/
    └── cargar_datos.py   → script de carga del CSV a MySQL
```

## 📥 Dataset

El dataset no está incluido en el repositorio por su tamaño (173MB).
Podés descargarlo desde Kaggle:
https://www.kaggle.com/datasets/alejandromendivil/bsas-realstate-on-sale

Una vez descargado, colocarlo en la carpeta `data/` con el nombre:
`bsas_realstate_on_sale_properati_dataset_2020.csv`

## 🗄️ Base de datos

El proyecto usa una tabla con las siguientes columnas:

- **fecha_creacion_publicacion** → fecha del anuncio
- **lat, lon** → coordenadas geográficas
- **pais** → país
- **ciudad, barrio** → ubicación
- **ambientes, dormitorios, banios** → características del inmueble
- **metros_cuadrados_totales, metros_cuadrados_cubiertos** → superficie
- **precio, moneda** → precio en USD o ARS
- **tipo_de_propiedad** → Departamento, Casa, PH, etc.
- **operacion** → Venta o Alquiler

## 📊 Análisis disponibles

Las consultas están disponibles en `sql/consultas.sql`.

- Precio promedio por tipo de propiedad
- Precio promedio por cantidad de ambientes
- Precio promedio por barrio
- Cantidad de propiedades por ciudad
- Cantidad de propiedades por barrio

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/FrancoMLS/proyecto-propiedades-bsas.git
cd proyecto-propiedades-bsas
```

### 2. Instalar dependencias
```bash
pip install pandas mysql-connector-python python-dotenv
```

### 3. Configurar variables de entorno
Crear un archivo `.env` basado en `.env.example` y completar con tus credenciales de MySQL:
```
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=proyecto_propiedades
```

### 4. Crear la base de datos
Ejecutar el archivo `sql/schema.sql` en MySQL Workbench.

### 5. Descargar el dataset
Ver sección Dataset y colocar el CSV en la carpeta `data/`.

### 6. Cargar los datos
```bash
python src/cargar_datos.py
```

## 👤 Autor

Franco Lonello Serra - [GitHub](https://github.com/FrancoMLS)