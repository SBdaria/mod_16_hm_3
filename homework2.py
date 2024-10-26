from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_dict() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_in_dict(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='DariDari')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='27')]) -> str:
    ind = str(int(max(users, key=int)) + 1)
    users[ind] = f'Имя: {username}, возраст: {age}'
    return f'User {ind} is registered!'


@app.put('/user/{user_id}/{username}/{age}')
async def update_dict(user_id: Annotated[str, Path(description='Enter ID', example='1')],
                      username: Annotated[
                          str, Path(min_length=5, max_length=20, description='Enter username', example='DariDari')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='27')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(description='Enter ID', example='1')]) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'
