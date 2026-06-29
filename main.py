from fastapi import FastAPI,Query
import uvicorn
from typing import Annotated
from schema import QueryParams ,TodoRequest ,UpdateTodo ,UpdateTodoResponse

app = FastAPI(
    title="Fast API CRUD TODO"
)

@app.get("/home" ,response_model=dict,status_code=200)
async def home ():
    return{"message":"Home API"}

@app.get("/query")
async def query(payload:Annotated[QueryParams ,Query()]):
    return payload

@app.post('/todo')
async def create_todo(payload:TodoRequest):
    return payload

@app.put("todo" ,response_model=UpdateTodoResponse)
async def update_todo(payload:UpdateTodo):
    return payload


if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Replace "main" with your filename (without .py)
        host="127.0.0.1",
        port=5000,
        reload=True,
    )