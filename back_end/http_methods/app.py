from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

app = FastAPI(title="Simple FastAPI APP", version="1.0.0")
data = [{"name": "Kayla John", "track": "AI Developer", "age": 23},
        {"name": "Jane DOe", "track": "AI Marketer", "age": 25 },
        {"name": "John Mike", "track": "AI Engineer", "age": 23}]

class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    track: Optional[str] = Field(example="Full stack")
    age: int = Field(..., example=25)



@app.get("/", description="This endpoint returns a welcome message")
def root():
    return{"Message": "Welcome to my FASTAPI Application"}

@app.get("/get-data")
def get_data():
    return data

@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    return {"Message": "Data received", "Data": data}

@app.put("/change_data/{id}") # /{id} is a path param used to filter wherever you are storing your data
def change_data(id: int, req: Item):
    data[id] = req.dict()
    print(data)
    return {"Message": "Data Changed", "Data": data}

# Write an endpoint to patch and delete entries from the data var
@app.patch("/update_data/{id}")
def update_data(id: int, req:Item):
    data[id].update(req.model_dump())
    print(data)
    return {"Message": "Data Updated", "Data": data}

@app.delete("/delete_data")
def delete_data(req:Item):
    data.clear()
    return {"Message": "Data Cleared", "Data": []}


if __name__ == "__main__":
    print(os.getenv("host"))
    print(os.getenv("port"))
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))
