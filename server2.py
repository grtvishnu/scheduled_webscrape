from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return{"data": [1, 2, 3]}


@app.get("/")
def hello_world():
    return{"data": [1, 2, 3]}
