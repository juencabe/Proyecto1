from fastapi import FastAPI

import pandas as pd

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

#1.Película con mayor duración según año, plataforma y tipo de duración
@app.get("/get_max_duration")
async def get_max_duration(year: int, platform: str, duration_type: str):
    
    # Cargamos nuestra base de datos
    df = pd.read_csv('Total_Streaming.csv')

    # Filtramos las columnas correspondientes
    filtered_df = df.loc[(df["year"] == year if year else True) &
                         (df["platform"] == platform if platform else True) &
                         (df["duration_type"] == duration_type if duration_type else True)]

    #Encontramos la película con la mayor duración
    pelicula = filtered_df.loc[filtered_df["duration_int"].idxmax()]
    return pelicula["title"]  

#2.Cantidad de películas según plataforma, con un puntaje mayor a XX en determinado año
@app.get("/get_score_count")
def get_score_count(platform: str, scored: float, year: int) -> int:
    
    # Cargamos nuestra base de datos
    df = pd.read_csv('Total_Streaming.csv')
    
    # Filtramos las columnas correspondientes
    filtered_df = df.loc[(df["platform"] == platform) & (df["year"] == year)]

    # Encontramos la cantidad de películas con un puntaje mayor a "scored"
    cantidad = filtered_df.loc[filtered_df["score"] > scored].groupby("platform")["title"].count()[platform]

    return cantidad

#3.Cantidad de películas según plataforma. 
    
@app.get("/get_count_platform")
async def get_count_platform(platform: str) -> int:

    # Cargamos nuestra base de datos
    df = pd.read_csv('Total_Streaming.csv')
    
    # Filtramos las columnas correspondientes
    filtered_df = df[df['platform'] == platform]

    # Contamos la cantidad de películas por plataforma
    plataforma = filtered_df.groupby('platform')['title'].count()[0]

    return plataforma

#4.Actor que más se repite según plataforma y año

@app.get("/get_actor")
async def get_actor(platform: str, year: int):

    # Cargamos nuestra base de datos
    df = pd.read_csv('Total_Streaming.csv')

    # Filtramos las columnas correspondientes
    filtered_df = df[(df['platform'] == platform) & (df['year'] == year)]

    # Dividimos los actores en una lista y la convertimos en un dataframe
    actors_df = filtered_df['cast'].str.split(', ', expand=True)

    # Otenemos el actor que más se repite
    actor_count = actors_df.stack().value_counts().reset_index()
    actor = actor_count.iloc[0]['index']

    return actor
    

#5.La cantidad de contenidos/productos que se publicó por país y año
@app.get('/prod_per_county/{type}/{country}/{year}')
def prod_per_county(type: str, country: str, year: int):

    # Cargamos nuestra base de datos
    df = pd.read_csv('Total_Streaming.csv')
    
    df_filtrado = df[(df['type'] == "type") & (df['country'].str.contains("country")) & (df['year'] == year)]
    num_filas = len(df_filtrado)
    
    return {'pais': country, 'year': anio, 'movie': respuesta}


#6.La cantidad total de contenidos/productos según el rating de audiencia dado
@app.get('/get_contents/{rating}')
def get_contents(rating: str):

    return {'rating': rating, 'contenido': respuesta}


@app.get('/get_recomendation/{title}')
def get_recomendation(title,):
    
    return {'recomendacion':respuesta}