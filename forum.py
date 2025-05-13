from typing import Final
from fastapi import FastAPI


@app.get("/get_user/")
async def get_user() -> list[User]:
    return [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 28},
        {"name": "Eve", "age": 22},
        {"name": "Frank", "age": 40},
        {"name": "Grace", "age": 27},
        {"name": "Heidi", "age": 32},
        {"name": "Ivan", "age": 29},
        {"name": "Judy", "age": 31},
    ]
print(get_user())
