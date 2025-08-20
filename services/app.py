from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from models.solider import Soldier   # ודא שהקובץ באמת נקרא solider.py
from services.DAL import DAL_mongo
import os

app = FastAPI()


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD", None)
DB = os.getenv("DATABASE", "enemy_soldiers")
COLLECTION = os.getenv("COLLECTION", "soldier_details")


dal = DAL_mongo(HOST, DB, COLLECTION, USER, PASSWORD)


@app.get("/", response_class=HTMLResponse)
def home():
    dal.open_connection()
    return """
    <h1>Choose your option</h1>
    <button onclick="location.href='/create'">Create</button>
    <button onclick="location.href='/read'">Read</button>
    <button onclick="location.href='/update'">Update</button>
    <button onclick="location.href='/delete'">Delete</button>
    """

@app.get("/create", response_class=HTMLResponse)
def create_form():
    return """
    <h2>Create Soldier</h2>
    <form action="/create" method="post" enctype="multipart/form-data">
        ID: <input type="number" name="id"><br><br>
        First Name: <input type="text" name="first_name"><br><br>
        Last Name: <input type="text" name="last_name"><br><br>
        Phone Number: <input type="text" name="phone_number"><br><br>
        Rank: <input type="text" name="rank"><br><br>
        <input type="submit" value="Submit">
    </form>
    """
@app.post("/create", response_class=HTMLResponse)
def create_item(
    id: int = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    phone_number: str = Form(...),
    rank: str = Form(...)
):
    soldier = Soldier(id, first_name, last_name, phone_number, rank)
    dal.insert_one({"first_name":soldier.first_name,"last_name":soldier.last_name,"phone_number":soldier.phone_number,"rank":soldier.rank})
    return f"""
    <h2>✅ Soldier Created Successfully!</h2>
    <p><b>ID:</b> {soldier.id}</p>
    <p><b>Name:</b> {soldier.first_name} {soldier.last_name}</p>
    <p><b>Phone:</b> {soldier.phone_number}</p>
    <p><b>Rank:</b> {soldier.rank}</p>
    <br>
    <button onclick="location.href='/'">Back to Menu</button>
    """
@app.get("/delete", response_class=HTMLResponse)
def delete_form():
    return """
    <h2>Delete Soldier</h2>
    <form action="/delete" method="post" enctype="multipart/form-data">
        Enter Soldier ID to delete: 
        <input type="text" name="id"><br><br>
        <input type="submit" value="Delete">
    </form>
    """
# POST → מקבל את ה־ID ומוחק (כרגע מדמה מחיקה)
@app.post("/delete", response_class=HTMLResponse)
def delete_item(id: int = Form(...)):
    # כאן בעתיד תעשה מחיקה אמיתית מה-DB
    return f"""
    <h2> Soldier id {id} Deleted</h2>
    <p>Soldier with ID <b>{id}</b> has been removed.</p>
    <br>
    <button onclick="location.href='/delete'">Delete Another</button>
    """

@app.get("/update", response_class=HTMLResponse)
def update_form():
    return """
    <h2>Update Soldier Rank</h2>
    <form action="/update" method="post" enctype="multipart/form-data">
        Soldier ID: <input type="number" name="id"><br><br>
        New Rank: <input type="text" name="rank"><br><br>
        <input type="submit" value="Update Rank">
    </form>
    """

# POST → מקבל את ה-ID והדרגה החדשה ומחזיר תשובה
@app.post("/update", response_class=HTMLResponse)
def update_rank(id: int = Form(...), rank: str = Form(...)):
    dal.update_one(id,rank)
    return f"""
    <h2>✅ Soldier Rank Updated</h2>
    <p><b>ID:</b> {id}</p>
    <p><b>New Rank:</b> {rank}</p>
    <br>
    <button onclick="location.href='/update'">Update Another</button>
    """


@app.get("/read", response_class=HTMLResponse)
def read_all():
    soldiers = dal.get_all()


    if not soldiers:
        return "<h2>No soldiers found in the database.</h2>"


    table = "<h2>All Soldiers</h2><table border='1' cellpadding='5'>"
    table += "<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Phone</th><th>Rank</th></tr>"
    for s in soldiers:
        table += f"<tr><td>{s['id']}</td><td>{s['first_name']}</td><td>{s['last_name']}</td><td>{s['phone_number']}</td><td>{s['rank']}</td></tr>"
    table += "</table>"
    return table