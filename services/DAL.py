
from services.mongo_connect import MongoDBConnection
from services.soldier import Soldier


class SoldierDAL:
    def __init__(self, collection_name="soldier_details"):
        self.collection_name = collection_name


    def create_soldier(self,soldier):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            collection.insert_one(soldier)
            print('Soldier DB')





    def get_all_soldiers(self):
        with MongoDBConnection() as mongo_conn:
            db = mongo_conn.get_db()
            collection = db[self.collection_name]
            soldiers = []
            for doc in collection.find({}):
                soldier = Soldier.from_dict(doc)
                soldiers.append(soldier)
            return soldiers

