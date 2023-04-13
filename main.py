from fastapi import FastAPI

import pandas as pd

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

#1.Película con mayor duración según año, plataforma y tipo de duración.
@app.get("/get_max_duration/")
async def get_max_duration(year: int, platform: str, duration_type: str):
    
    #Cargamos el dataframe
    df = pd.read_csv("Total_Streaming.csv")
     
    #Filtramos las columnas
    filtered_df = df.loc[(df["year"] == year if year else True) &
                         (df["platform"] == platform if platform else True) &
                         (df["duration_type"] == duration_type if duration_type else True)]
    
    #Encontramos la pelicula con mayor duración
    pelicula = filtered_df.loc[filtered_df["duration_int"].idxmax()]

    return pelicula["Respuesta"]

#2.Cantidad de películas según plataforma, con un puntaje mayor a XX en determinado año.
@app.get("/get_score_count/{platform}/{scored}/{year}")
def get_score_count(platform: str, scored: float, year: int):
    # Seleccionar los registros que corresponden al año y al puntaje especificado
    df_filtered = df.loc[(df['release_year'] == year) & (df['scored'] > scored)]
    
    # Filtrar los registros para obtener solo las películas
    df_movies = df_filtered.loc[df['type'] == 'movie']
    
    # Filtrar los registros para obtener solo las películas que no son documentales
    df_no_doc = df_movies[~df_movies['listed_in'].str.contains('documentary', regex=False)]
    
    # Filtrar los registros para obtener solo las películas que se encuentran en la plataforma especificada
    df_platform = df_no_doc.loc[df['platform'] == platform]
    
    # Contar el número de registros que cumplen los criterios anteriores
    count = len(df_platform)
    
    return count
        #'plataforma': platform,
        #'cantidad': cantidad,
        #'anio': year,
        #'score': scored
    
#3.Cantidad de películas según plataforma
@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma: str):
    
    return {'plataforma': plataforma, 'peliculas': respuesta}

#4.Actor que más se repite según plataforma y año
@app.get('/get_actor/{plataforma}/{anio}')
def get_actor(plataforma: str, anio: int):
    
    return {
        'plataforma': plataforma,
        'anio': anio,
        'actor': respuesta,
        'apariciones': respuesta
    }
#5.La cantidad total de contenidos/productos según el rating de audiencia dado
@app.get('/get_contents/{rating}')
def get_contents(rating: str):

    return {'rating': rating, 'contenido': respuesta}

#6.La cantidad de contenidos/productos que se publicó por país y año
@app.get('/prod_per_county/{tipo}/{pais}/{anio}')
def prod_per_county(tipo: str, pais: str, anio: int):
    
    return {'pais': pais, 'anio': anio, 'peliculas': respuesta}