from fastapi import FastAPI
from scrape import run as scrape_runner
app = FastAPI()


@app.post("/box-office-mojo-scraper")
def boxpffice_scrape_view():
    scrape_runner()
    return{"data": [1, 2, 3]}
