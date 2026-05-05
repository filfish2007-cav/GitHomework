from fastapi import FastAPI
from pydantic import BaseModel

app1 = FastAPI()

class HelloWorld(BaseModel):
    message: str

@app1.get("/greeting")
def greeting() -> HelloWorld:
    return HelloWorld(message="Hello World")