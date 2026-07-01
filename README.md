# Dashboard de Análisis de Datos de Fórmula 1

## Descripción del Proyecto
Este proyecto es unDasgboard interactivo desarrollado con Flask, Dash y Plotly en python. Su objetivo es visualizar métricas estadísticas y análisis de datos correspondientes a diferentes entidades de la Fórmula 1 (Pilotos, Directores, FIA, y Patrocinadores).

## Conjunto de Datos y Tratamiento
Las tablas de la base de datos utilizada estaban vacías, sin ningún dato cargado, por lo que utilizamos herramientas como Mockaroo y Deepseek para generar datos sintéticos por cada tabla, manteniendo la lógica y estructura de la base de datos. 
 
* Se generarón los datos sinteticos usando Mockaroo y se realizó una limpieza para garantizar consistencia, algunos datos se tuvieron que generar manualmente.
* El dataset incluye información sobre los diferentes aspectos relevantes e historicos de la Formula 1, como información de los circuitos, pilotos o escuderias entre otros.

## Visualizaciones Implementadas
El dashboard contiene gráficas orientadas al análisis estadístico:
1. **Victorias por escuderia**:  Distribución de las victorias obtenidas por cada escuderia.
2. **Pilotos por Nacionalidad**: Proporción de la nacionalidad de los pilotos.
3. **Inversión por Sector**: Proporción del dinero total invertido por cada sector industrial.
4. **Top 10 Pilotos por Puntos**: Lista de los 10 pilotos con la mayor cantidad de puntos obtenidos.

## Instrucciones para Ejecución Local

Para ejecutar este dashboard en un entorno local, siga los siguientes pasos:

## Instrucciones para Ejecución Local

Para ejecutar este dashboard en un entorno local, siga los siguientes pasos:

1. Clone el repositorio localmente ejecutando este comando en la terminal: `git clone https://github.com/SergioVillarreal1277/Dashboard_F1.git`
2. Navegue al directorio del proyecto: `cd Dashboard_F1`
3. Instale las dependencias y librerias necesarias: `pip install dash plotly pandas`
4. Ejecute este comando en la terminal para correr el archivo: `python app.py`
5. Abra un navegador web y acceda a la dirección http que se mostrará en la terminal despúes de ejecutar el archivo