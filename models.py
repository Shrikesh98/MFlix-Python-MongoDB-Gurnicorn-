from datetime import datetime
from bson.objectid import ObjectId


class Comments:
    def __init__(self, _id=0, name=str(), email=str(), movie_id=ObjectId, text=str(), date=datetime):
        self._id = _id
        self.name = name
        self.email = email
        self.movie_id = movie_id
        self.text = text
        self.date = date
