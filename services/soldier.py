class Soldier:
    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str, rank: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    def __repr__(self):
        return f"Soldier(id={self.id}, name={self.first_name} {self.last_name}, phone={self.phone_number}, rank={self.rank})"

    def to_dict(self) -> dict:
        return {
            "ID": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "rank": self.rank
        }

    @staticmethod
    def from_dict(data: dict) -> "Soldier":
        return Soldier(
            id=data.get("id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            rank=data.get("rank")
        )