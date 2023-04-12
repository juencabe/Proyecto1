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