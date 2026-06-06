import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()
print("Conexión exitosa")

df = pd.read_csv("data/bsas_realstate_on_sale_properati_dataset_2020.csv")

df = df.rename(columns={
    "created_on": "fecha_creacion_publicacion",
    "l1": "pais",
    "l2": "ciudad",
    "l3": "barrio",
    "rooms" : "ambientes",
    "bedrooms" : "dormitorios",
    "bathrooms" : "banios",
    "surface_total" : "metros_cuadrados_totales",
    "surface_covered" : "metros_cuadrados_cubiertos",
    "price" : "precio",
    "currency" : "moneda",
    "property_type" : "tipo_de_propiedad",
    "operation_type" : "operacion"
})

columnas = ["fecha_creacion_publicacion", "lat", "lon", "pais", "ciudad", "barrio", "ambientes", "dormitorios", "banios", "metros_cuadrados_totales", "metros_cuadrados_cubiertos", "precio", "moneda", "tipo_de_propiedad", "operacion"]
df = df[columnas]
print(df.head(5))

for _, row in df.iterrows():
    cursor.execute(
        "INSERT IGNORE INTO propiedades (fecha_creacion_publicacion, lat, lon, pais, ciudad, barrio, ambientes, dormitorios, banios, metros_cuadrados_totales,metros_cuadrados_cubiertos, precio, moneda, tipo_de_propiedad, operacion) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            str(row.get("fecha_creacion_publicacion", "")) or None,
            float(row["lat"]) if pd.notna(row.get("lat")) else None,
            float(row["lon"]) if pd.notna(row.get("lon")) else None,
            str(row.get("pais", "")) or None,
            str(row.get("ciudad", "")) or None,
            str(row.get("barrio", "")) or None,
            int(row["ambientes"]) if pd.notna(row.get("ambientes")) else None,
            int(row["dormitorios"]) if pd.notna(row.get("dormitorios")) else None,
            int(row["banios"]) if pd.notna(row.get("banios")) else None,
            float(row["metros_cuadrados_totales"]) if pd.notna(row.get("metros_cuadrados_totales")) else None,
            float(row["metros_cuadrados_cubiertos"]) if pd.notna(row.get("metros_cuadrados_cubiertos")) else None,
            float(row["precio"]) if pd.notna(row.get("precio")) else None,
            str(row.get("moneda", "") or None),
            str(row.get("tipo_de_propiedad", "") or None),
            str(row.get("operacion", "") or None),
        ) 
        )
    
conn.commit()

