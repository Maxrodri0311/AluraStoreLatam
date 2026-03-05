import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

sns.set_theme(style='whitegrid')
base_path = 'base-de-datos-challenge1-latam'

# 1. Carga
tiendas = {
    f'Tienda {i}': pd.read_csv(os.path.join(base_path, f'tienda_{i}.csv' if i>1 else 'tienda_1 .csv'))
    for i in range(1, 5)
}
df = pd.concat(tiendas.values(), keys=tiendas.keys()).reset_index(level=0).rename(columns={'level_0': 'Tienda'})
df['Precio'] = df['Precio'].astype(float)
df['Costo de envío'] = df['Costo de envío'].astype(float)
df['Fecha de Compra'] = pd.to_datetime(df['Fecha de Compra'])

print("=== FASE 2: Facturación y Ventas ===")
facturacion = df.groupby('Tienda')['Precio'].sum().reset_index()
facturacion = facturacion.sort_values('Precio', ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(data=facturacion, x='Tienda', y='Precio', hue='Tienda', legend=False, palette='viridis')
plt.title('Facturación Total por Tienda')
plt.ylabel('Ingresos Brutos ($)')
plt.xlabel('Sucursal')
plt.tight_layout()
plt.savefig('facturacion.png')
plt.close()

print("Facturación Total:")
print(facturacion.to_string(index=False))
print("\n[Senior Insight] La facturación total es el primer indicador de volumen. Muestra la capacidad de generación de ingresos brutos de cada sucursal antes de costos operativos.")

ticket_promedio = df.groupby('Tienda').apply(lambda x: x['Precio'].sum() / len(x)).reset_index(name='Ticket Promedio')
print("\nTicket Promedio:")
print(ticket_promedio.to_string(index=False))
print("\n[Senior Insight] El ticket promedio indica el valor medio de cada compra. Tiendas con mayor ticket promedio logran extraer más valor de cada transacción.")

print("\n=== FASE 3: Categorías y Productos ===")
top_categorias = df.groupby(['Tienda', 'Categoría del Producto']).size().reset_index(name='Ventas')
top_categorias = top_categorias.sort_values(['Tienda', 'Ventas'], ascending=[True, False])
top3_cat = top_categorias.groupby('Tienda').head(3)
print("Top 3 Categorías por Tienda:")
print(top3_cat.to_string(index=False))
print("\n[Senior Insight] Conocer el 'market share' interno (las categorías estrella) permite entender el foco comercial de cada tienda.")

prod_stats = df.groupby(['Tienda', 'Producto']).agg(
    Ventas=('Precio', 'count'),
    Calif_Promedio=('Calificación', 'mean')
).reset_index()
prod_stats['Umbral_Volumen'] = prod_stats.groupby('Tienda')['Ventas'].transform(lambda x: x.quantile(0.75))
criticos = prod_stats[(prod_stats['Calif_Promedio'] < 2) & (prod_stats['Ventas'] > prod_stats['Umbral_Volumen'])]
print("\nProductos Críticos (Calificación < 2 y Alto Volumen > P75):")
print(criticos.to_string(index=False) if not criticos.empty else "No hay productos críticos bajo este criterio.")
print("\n[Senior Insight] Los productos críticos son un foco de alerta (Laggards red flag). Dañan recurrentemente la reputación de la marca.")

print("\n=== FASE 4: Análisis Logístico y Satisfacción ===")
envio_prom = df.groupby('Tienda')['Costo de envío'].mean().reset_index(name='Costo Envío Promedio')
print("Costo de Envío Promedio:")
print(envio_prom.to_string(index=False))

ratio_logistico = df.groupby('Tienda').apply(lambda x: x['Costo de envío'].sum() / x['Precio'].sum() * 100).reset_index(name='Ratio Logístico (%)')
print("\nRatio Logístico (% sobre el precio):")
print(ratio_logistico.to_string(index=False))
print("\n[Senior Insight] El Ratio Logístico revela la canibalización del margen de venta por culpa del envío. Un porcentaje alto indica ineficiencia en la red de distribución.")

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Tienda', y='Calificación', hue='Tienda', legend=False, palette='Set2')
plt.title('Dispersión de la Satisfacción del Cliente (NPS Proxy)')
plt.ylabel('Calificación (1-5)')
plt.xlabel('Sucursal')
plt.tight_layout()
plt.savefig('calificacion_boxplot.png')
plt.close()

calif_prom = df.groupby('Tienda')['Calificación'].mean().reset_index(name='Calificación Promedio')
print("\nCalificación Promedio:")
print(calif_prom.to_string(index=False))
print("\n[Senior Insight] El boxplot de la calificación y la media muestran la consistencia en la entrega de valor al cliente (salud de marca debilitada si es baja).")

print("\n=== FASE 5: Informe Estratégico ===")
scorecard = facturacion.merge(ticket_promedio, on='Tienda')\
    .merge(envio_prom, on='Tienda')\
    .merge(ratio_logistico, on='Tienda')\
    .merge(calif_prom, on='Tienda')

print("SCORECARD COMPARATIVO:")
print(scorecard.to_string(index=False))
