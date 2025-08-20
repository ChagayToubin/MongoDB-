
from fastapi import FastAPI
from ..models.solider import Soldier
app = FastAPI()
dal_solider=Soldier("","","""",""")

@app.get("/")
def insert_data():

    return

