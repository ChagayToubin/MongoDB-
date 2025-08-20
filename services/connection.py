from pymongo import MongoClient

# חיבור למסד
client = MongoClient("mongodb://localhost:27017/")
db = client["enemy_soldiers"]
collection = db["soldier_details"]

# 20 ערכים קבועים בלי 0 בהתחלה
soldiers = [
    {"first_name": "David", "last_name": "Cohen", "phone_number": "1", "rank": "Private"},
    {"first_name": "Moshe", "last_name": "Levi", "phone_number": "2", "rank": "Sergeant"},
    {"first_name": "Yossi", "last_name": "Mizrahi", "phone_number": "3", "rank": "Captain"},
    {"first_name": "Avi", "last_name": "Peretz", "phone_number": "4", "rank": "Lieutenant"},
    {"first_name": "Eli", "last_name": "Katz", "phone_number": "5", "rank": "Corporal"},
    {"first_name": "Shlomi", "last_name": "Bar", "phone_number": "6", "rank": "Major"},
    {"first_name": "Itzik", "last_name": "Avraham", "phone_number": "7", "rank": "Private"},
    {"first_name": "Omer", "last_name": "Sharon", "phone_number": "8", "rank": "Sergeant"},
    {"first_name": "Lior", "last_name": "Halevi", "phone_number": "9", "rank": "Captain"},
    {"first_name": "Tomer", "last_name": "Ronen", "phone_number": "10", "rank": "Lieutenant"},
    {"first_name": "Nir", "last_name": "Amiel", "phone_number": "11", "rank": "Corporal"},
    {"first_name": "Bar", "last_name": "Shmuel", "phone_number": "12", "rank": "Major"},
    {"first_name": "Gal", "last_name": "Ben", "phone_number": "13", "rank": "Private"},
    {"first_name": "Noam", "last_name": "Dayan", "phone_number": "14", "rank": "Sergeant"},
    {"first_name": "Tal", "last_name": "Golan", "phone_number": "15", "rank": "Captain"},
    {"first_name": "Shai", "last_name": "Yadin", "phone_number": "16", "rank": "Lieutenant"},
    {"first_name": "Idan", "last_name": "Shahar", "phone_number": "17", "rank": "Corporal"},
    {"first_name": "Ran", "last_name": "Erez", "phone_number": "18", "rank": "Major"}]

result = collection.insert_many(soldiers)