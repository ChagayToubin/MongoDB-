class Soldier:
    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str, rank: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def __repr__(self):
        return f"Soldier(id={self.id}, name={self.first_name} {self.last_name}, phone={self.phone_number}, rank={self.rank})"
