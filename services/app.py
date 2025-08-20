from fastapi import FastAPI
from DAL import SoldierDAL
from soldier import Soldier

app = FastAPI()
dal = SoldierDAL()

@app.get("/soldiersdb/")
def get_all_soldiers():
    soldiers = dal.get_all_soldiers()
    return [s.to_dict() for s in soldiers]

@app.post("/soldiersdb/")
def create_soldier(soldier: dict):
    s = Soldier.from_dict(soldier)
    dal.create_soldier(s.to_dict())
    return {"message": "Soldier created!"}

@app.delete("/soldiersdb/{id}")
def delete_soldier(id: str):
    dal.delete_soldier(id)
    return {"message": f"Soldier ID {id} deleted!"}

@app.put("/soldiersdb/")
def update_soldier_details(soldier: dict):
    s = Soldier.from_dict(soldier)
    dal.update_soldier_details(s.to_dict())
    return {"message": f"Soldier {soldier.get('_id', '')} updated!"}