# 📊 Alura Store Challenge - Business Intelligence & Data Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

Este repositorio contiene la solución analítica al **Alura Store Challenge**. A través de un análisis profundo de datos de ventas, logística y satisfacción del cliente, evaluamos el rendimiento de cuatro sucursales para tomar una decisión estratégica de alto nivel para negocio: **¿Cuál de las cuatro tiendas debería venderse o cerrarse para optimizar el capital de la empresa?**

## 🎯 Propósito del Análisis

El proyecto simula un entorno real de Toma de Decisiones Basadas en Datos (Data-Driven Decision Making). El objetivo es consolidar bases de datos dispersas, sanear la información, extraer KPIs (Indicadores Clave de Rendimiento) y emitir una recomendación ejecutiva sustentada en 5 pilares:

1. **Facturación Total y Ticket Promedio**
2. **Distribución de Ventas por Categoría**
3. **Calificación y Satisfacción del Cliente (NPS Proxy)**
4. **Productos Estrella y Laggards**
5. **Eficiencia Logística (Costo de envío)**

## 📂 Estructura del Proyecto

```text
📁 alura-store-challenge/
│
├── 📓 AluraStoreLatam.ipynb      # Notebook principal con todo el código, análisis gráfico e informe final.
├── 📄 README.md                  # Documentación del proyecto (Este archivo).
│
└── 📁 base-de-datos-challenge1-latam/  # Carpeta con los Datasets originales (si se corre en local)
    ├── tienda_1.csv
    ├── tienda_2.csv
    ├── tienda_3.csv
    └── tienda_4.csv
```

> *Nota: El notebook está configurado para importar los CSVs directamente desde las URLs del repositorio original de Alura si se ejecuta en Google Colab.*

## 📈 Ejemplos de Gráficos e Insights Obtenidos

Durante el análisis se generaron diversas visualizaciones para sustentar el Informe Final. Algunos hallazgos clave incluyen:

### 1. Ingreso Total (Gráfico de Barras)

Se comprobó que la **Tienda 1 lidera** indiscutiblemente la generación de capital bruto (> $1.15 Billones), mientras que la **Tienda 4** cierra la lista demostrando debilidad en captación de volumen.

### 2. Dispersión de Satisfacción (Boxplot)

Se evaluó el riesgo de retención de marca. Las Tiendas 2 y 3 poseen los clientes más felices (medias sostenidas > 4.0), mientras que la Tienda 1 y la Tienda 4 muestran las peores calificaciones, con asimetrías preocupantes hacia la baja puntuación.

### 3. Distribución Geográfica (Scatter Plot - Desafío Extra 🌍)

Se incluyó un mapeo geoespacial basado en `Latitud` y `Longitud` donde el tamaño de cada punto representa el valor del ticket de compra. Esto permitió visualizar la densidad del alcance logístico de las sucursales.

## 🚀 Cómo Ejecutar el Notebook

La forma más sencilla y recomendada de evaluar este proyecto es a través de Google Colab:

1. **Vía Google Colab (Recomendado):**
   - Sube el archivo `AluraStoreLatam.ipynb` a tu Google Drive y ábrelo con Google Colaboratory.
   - El entorno en la nube ya contiene las librerías necesarias (`pandas`, `matplotlib`, `seaborn`).
   - Ve a `Entorno de ejecución` > `Ejecutar todas` (O presiona `Ctrl + F9`). Los datos se descargarán automáticamente de la red.

2. **Ejecución Local (Jupyter Notebook / VSCode):**
   - Clona este repositorio: `git clone https://github.com/tu-usuario/alura-store-challenge.git`
   - Asegúrate de tener Python instalado junto con las dependencias:

     ```bash
     pip install pandas matplotlib seaborn
     ```

   - Abre el archivo `AluraStoreLatam.ipynb` y ejecuta las celdas secuencialmente.

---
*Desarrollado como proyecto portfolio por Maxi para la formación de Foundation Data Science de Alura.*
