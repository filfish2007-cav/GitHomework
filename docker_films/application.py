import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from settings import settings

app = FastAPI()


class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int


@app.get("/films/{film_id}")
def get_film_by_id(film_id: int):
    with open(settings.data_file_path) as file:
        films = json.load(file)

    for film in films:
        if film["id"] == film_id:
            return film
    raise HTTPException(status_code=404, detail="Film not found")


@app.post("/films")
def create_film(film: Film):
    with open(settings.data_file_path) as file:
        films = json.load(file)

    if len(films) >= settings.MAX_FILMS:
        raise HTTPException(
            status_code=400, detail=f"Досягнуто ліміт фільмів ({settings.MAX_FILMS})"
        )

    films.append(film.model_dump())

    with open(settings.data_file_path, "w") as file:
        json.dump(films, file)

    return {"додано фільм": film.title}


@app.delete("/films")
def delete_film(film_id: int):
    with open(settings.data_file_path) as file:
        films = json.load(file)

    for film in films:
        if film["id"] == film_id:
            films.remove(film)

    with open(settings.data_file_path, "w") as file:
        json.dump(films, file)
