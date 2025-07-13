import datetime as dt
import uuid

class Transaction:
    def __init__(self, type_, amount, category, note, date=None):
        self.id = str(uuid.uuid4()) # unique ID
        self.type = type_.lower()   #income or expense
        self.amount = amount
        self.category = category.lower()
        self.note = note
        self.date = date if date is not None else dt.datetime.now().isoformat()   #yyyy-MM-DD

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.date
        }