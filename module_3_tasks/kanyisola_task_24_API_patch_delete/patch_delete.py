from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple FastAPI APP", version="1.0.0")

data = [
    {"name": "Blessing James", "track": "Cloud Computing", "age": 21},
    {"name": "Michael Jameson", "track": "Cloud Computing", "age": 34},
    {"name": "Oscar Piastri", "track": "FI Driver", "age": 24}
    
    ]

class Item(BaseModel):
    name: str = Field(..., example="Christopher Egwukum")
    track: str = Field(..., example="Instructor")
    age: int = Field(..., example=29)


@app.get("/", description="This endpoint returns a welcome message")
def root():
    return {"Message": "Welcome to my FastAPI Application"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: Item):
   data.append (req.model_dump())
   return {"Message": "Data has been successfully received", "Data": data}

@app.put("/ change_data{id}")
def change_data(id:int, req:Item):
    data[id] = req.model_dump()
    print(data)
    return {"Message": "Data has been succssfully changed", "Data": data}

@app.patch("/ update_data{id}")
def update_data(id:int, req:Item):
    data[id].update(req.model_dump())
    return { "Message": "Data has been successfully updated", "Data": data}

@app.delete("/delete_data")
def delete_data(req:Item):
    data.clear()
    return{"Message": "Data has been successfully deleted", "Data": []}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port_1"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port_1")))
