from fastapi import FastAPI
from pydantic import BaseModel

# # task 1

app = FastAPI()
#
# class Response(BaseModel):
#     message: str
#
# @app.post("/hello")
# def hello_world() -> Response:
#     return Response(
#         message="Hello World",
#         )

# # task 2

class HelloWorld(BaseModel):
    message: str

@app.get("/greeting")
def hello() -> HelloWorld:
    return HelloWorld(message="Hello World")


