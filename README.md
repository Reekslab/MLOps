# MLOps

datos del Machine Learning, ranks.csv: https://drive.google.com/file/d/1Pcki9gD0dBRCsVcEqqmnEcCrpmRAZKNu/view?usp=share_link

# Contexto
Para este proyecto se nos entregó una data de plataformas de streaming.
A esta data se le hizo varias transformaciones como unir toda la data en un solo dataframe, rellenar nulos, agregar y quitar columnas, etc. Todas estas transformaciones están en el archivo llamado "Transformaciones.ipynb".
Luego queremos facilitar consultas de esta data por medio de una api hecha con FastApi. El archivo que contiene a esta api está como "main.py".
### Las consultas a la api son las siguientes:
/get_max_duration/{anio}/{plataforma}/{dtype} - esta devuelve la pelicula con mayor duración con los filtros de año y plataforma
/get_score_count/{plataforma}/{scored}/{anio} - esta devuelve la cantidad de peliculas con el score seleccionado y su plataforma
/get_count_platform/{plataforma} - esta devuelve la cantidad de peliculas por plataforma
/get_actor/{plataforma}/{anio} - esta devuelve el actor que mas aparece y el número de apariciones 
/prod_per_county/{tipo}/{pais}/{anio} - devuelve la cantidad de peliculas por país 
/get_contents/{rating} - esta devuelve la cantidad de contenido filtrado por tipo de rating

Por ultimo se hizo un modelo de machine learning con los datos.
Dado un id de usuario y de pelicula, el modelo predice con base en las puntuaciones del usuario a peliculas anteriores, si esta nueva pelicula le puede gustar o no
El archivo que lo contiene se llama "Machine learning.ipynb"
