import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Carga de datos (ajusta los nombres de archivo si tienen espacios)
base_path = 'base-de-datos-challenge1-latam'
tiendas = {
    'Tienda 1': pd.read_csv(os.path.join(base_path, 'tienda_1 .csv')),
    'Tienda 2': pd.read_csv(os.path.join(base_path, 'tienda_2.csv')),
    'Tienda 3': pd.read_csv(os.path.join(base_path, 'tienda_3.csv')),
    'Tienda 4': pd.read_csv(os.path.join(base_path, 'tienda_4.csv'))
}

# Unificación con trazabilidad
df_global = pd.concat(tiendas.values(), keys=tiendas.keys()).reset_index(level=0).rename(columns={'level_0': 'Tienda'})

# Inspección rápida de salud de los datos
print("=== INFO ===")
df_global.info()

print("\n=== HEAD ===")
print(df_global.head())

print("\n=== VALORES NULOS ===")
print(df_global.isnull().sum())

# Revisión de tipos de datos antes del casteo
print("\n=== TIPOS DE DATOS INICIALES ===")
print(df_global.dtypes)
