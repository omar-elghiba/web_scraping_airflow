# main.py
from fastapi import FastAPI
from pymongo import MongoClient
from typing import List
from pydantic import BaseModel, Field


# Define a Pydantic model for your MongoDB documents
class Item(BaseModel):
    title: str

app = FastAPI()

client = MongoClient('srv2.omarelghiba.com:6005')
db = client['my_database_1']
collection = db['my_collection_1']

@app.get("/items/", response_model=List[Item])
async def read_items():

    items = list(collection.find({}, {"_id": 0, "Title": 1}))

    for item in items:
        item["title"] = item.pop("Title")
    return items