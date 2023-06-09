#### PROYECTO PRESENTADO POR JULIO CASTAÑO (Tener en cuenta que hay archivos en el Master)

### DESCRIPCION DEL PROYECTO: Diseñar e implementar herramienta tecnólogica para un cliente que provee servicios de agregación de plataformas de streaming para implementar dentro de sus procesos organizacionales.
### ALCANCE DEL PROYECTO

#### 1.Desarrollo de una API y su correspondiente despliegue en Internet de:

- Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración. La función debe llamarse get_max_duration(year, platform, duration_type) y debe devolver sólo el string del nombre de la película.

- Cantidad de películas (sólo películas, no series, etc) según plataforma, con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) y debe devolver un int, con el total de películas que cumplen lo solicitado.

- Cantidad de películas (sólo películas, no series, etc) según plataforma. La función debe llamarse get_count_platform(platform) y debe devolver un int, con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.

- Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) y debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.

- La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año. La función debe llamarse prod_per_county(tipo,pais,anio) deberia devolver la cantidada de contenidos/productos segun el tipo de contenido (pelicula,serie) por pais y año en un diccionario con las variables llamadas 'pais' (nombre del pais), 'anio' (año), 'pelicula' (cantidad de contenidos/productos).

- La cantidad total de contenidos/productos (todo lo disponible en streaming, series, peliculas, etc) según el rating de audiencia dado (para que publico fue clasificada la pelicula). La función debe llamarse get_contents(rating) y debe devolver el numero total de contenido con ese rating de audiencias.

https://henry-laboratorio1.onrender.com/docs

#### 2.Entrenar modelo de machine learning para armar un sistema de recomendación de películas.

- Recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse get_recommendation(titulo: str).

#### DESARROLLO DEL PROYECTO

### Realizar proceso ETL (Extraction, Transform, Load) para preparar los datos que se van a utilizar en la API.

- Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

- Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

- De haber fechas, deberán tener el formato AAAA-mm-dd

- Los campos de texto deberán estar en minúsculas, sin excepciones

- El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

### Realizar el análisis exploratorio de datos (EDA) para utilizar esta información en el entrenamiento del modelo de Machine Learning.


https://youtu.be/nOsQ6rXwUXE

### Herramientas Utilizadas
#### Python
#### Google Colaborate
#### Google Drive
#### GitHub
