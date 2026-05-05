from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
app = FastAPI()
class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int

@app.get("/books")
def get_books() -> List[Book]:
    with open("knigi.json") as file:
        books = json.load(file)
    return books

@app.get("/books/{book_id}")
def get_book_by_id(id: str) -> Book:
    with open("knigi.json") as file:
        books = json.load(file)

    for book in books:
        if book["id"] == id:
            return book

@app.post("/books")
def create_book(book: Book) -> dict:
    with open("knigi.json") as file:
        books = json.load(file)

    books.append(book.model_dump())

    with open("knigi.json") as file:
        json.dump(books, file)
    return {"message": "Book created successfully!"}
