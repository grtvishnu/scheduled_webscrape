from fastapi import FastAPI
from scrape import run as scrape_runner
app = FastAPI()


@app.get("/box-office-mojo-scraper")
def scraper_view():
    return{"data": [1, 2, 3]}
