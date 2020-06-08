from fastapi import FastAPI
from scarpe import run as scrape_runner

app = FastAPI()


@app.get("/")
def hellow():
    return{"data": [5, 6, 7]}


@app.post("/box-office-mojo-scraper")
def boxpffice_scrape_view():
    scrape_runner()
    return{"data": [1, 2, 3]}
