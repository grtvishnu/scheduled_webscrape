from fastapi import FastAPI
from scarpe import run as scrape_runner
from logger import trigger_log_save
app = FastAPI()


@app.get("/")
def hellow():
    return{"data": [5, 6, 7]}


@app.post("/box-office-mojo-scraper")
def boxpffice_scrape_view():
    scrape_runner()
    trigger_log_save()
    return{"data": [1, 2, 3]}
