from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/get_max_duration/{anio}/{plataforma}/{dtype}")
def get_max_duration(anio:int ,plataforma:str ,dtype:str):
    df = pd.read_csv(r"df.csv")
    pelicula = df[(df["release_year"] == anio) & (df["platform"] == plataforma) & (df["duration_type"] == dtype)]
    duracionmax = pelicula["duration_int"].idxmax()
    title = pelicula.loc[duracionmax , "title"]
    return {"pelicula: " : title}

@app.get("/get_score_count/{plataforma}/{scored}/{anio}")
def get_score_count(plataforma:str , scored:float , anio:int):
    df = pd.read_csv(r"df.csv")
    peliculas = df[(df["platform"] == plataforma) & (df["score"] >= scored) & (df["release_year"] == anio) & (df["type"]=="movie")]
    numdepeliculas = len(peliculas)
    return {"plataforma" : plataforma , "cantidad" : numdepeliculas , "anio" : anio , "scored" : scored}

@app.get('/get_count_platform/{plataforma}')
def get_count_platform(plataforma:str):
    df = pd.read_csv(r"df.csv")
    peliculas = df[(df["platform"] == plataforma) & (df["type"] == "movie" )]
    contador = len(peliculas)
    return {"plataforma" : plataforma ,"peliculas" : contador}

@app.get('/get_actor/{plataforma}/{anio}')
def get_actor(plataforma:str , anio:int):
    df = pd.read_csv(r"df.csv")
    actor = df[(df["platform"] == plataforma) & (df["release_year"] == anio) & (df["cast"])]
    serie_actores = actor["cast"].str.split(",\s*", expand=True).stack()
    frecuencia_actores = serie_actores.value_counts()
    actor_mas_comun = frecuencia_actores.idxmax()
    apariciones = int(frecuencia_actores.loc[actor_mas_comun])
    return {"plataforma" : plataforma , "anio" : anio , "actor" : actor_mas_comun , "apariciones" : apariciones}

@app.get('/prod_per_county/{tipo}/{pais}/{anio}')
def prod_per_country(tipo:str , pais:str , anio:int):
    df = pd.read_csv(r"df.csv")
    product = df[(df["type"] == tipo) & (df["country"] == pais) & (df["release_year"] == anio)]
    cantidad = {"pais:" : pais , "anio:" : anio , "contenido:" : len(product["type"])}
    return cantidad

@app.get("/get_contents/{rating}")
def get_contents(rating: str):
    df = pd.read_csv(r"df.csv")
    conten = df[(df["rating"] == rating)]
    cantcont = len(conten["rating"])
    return {"rating:" : rating , "contenido:" : cantcont}

