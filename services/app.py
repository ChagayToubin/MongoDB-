from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from models.solider import Soldier   # ודא שהקובץ באמת נקרא solider.py

app = FastAPI()

# דף הבית עם 4 כפתורים
@app.get("/", response_class=HTMLResponse)
def home():
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
    # כאן בעתיד תשים UPDATE אמיתי ל-DB
    return f"""
    <h2>✅ Soldier Rank Updated</h2>
    <p><b>ID:</b> {id}</p>
    <p><b>New Rank:</b> {rank}</p>
    <br>
    <button onclick="location.href='/update'">Update Another</button>
    """


@app.get("/read", response_class=HTMLResponse)
def read_all():
    soldiers = [
    {"id": 1, "first_name": "David", "last_name": "Levi", "phone_number": "0501234567", "rank": "Captain"},
    {"id": 2, "first_name": "Moshe", "last_name": "Cohen", "phone_number": "0527654321", "rank": "Sergeant"}
]
    # tbh eut kpuebmv pou

    if not soldiers:
        return "<h2>No soldiers found in the database.</h2>"

    # בניית טבלה HTML
    table = "<h2>All Soldiers</h2><table border='1' cellpadding='5'>"
    table += "<tr><th>ID</th><th>First Name</th><th>Last Name</th><th>Phone</th><th>Rank</th></tr>"
    for s in soldiers:
        table += f"<tr><td>{s['id']}</td><td>{s['first_name']}</td><td>{s['last_name']}</td><td>{s['phone_number']}</td><td>{s['rank']}</td></tr>"
    table += "</table>"
    return table