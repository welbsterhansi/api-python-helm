from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import  User


app = FastAPI()

@app.get('/')
async def root():
    return {"msg": "Welcome to api catalog on version 0.0.1"}

@app.get('/health')
async def health():
    return {"status": "OK"}


users = {
    1: {
        "nome": "Carlos Hansi Lopes",
        "cpf": "65434345567",
        "chip": "85981816758"
    },
    2: {
        "nome": "Felipe Mendes Costa",
        "cpf": "63534345123",
        "chip": "8599991324"
    },
    3: {
       "nome": "Paulo Costinha da Silva",
       "cpf": "62534345333",
       "chip": "8599991223"   
    }
}

@app.get('/users')
async def get_users():
    return users

@app.post('/users', status_code=status.HTTP_201_CREATED)
async def post_user(user: User):
    if user.id is not users:
        users[user.id] = user
        return user
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='409, this id alredy' )


@app.get('/users/{user_id}')
async def get_user(user_id: int):
    try:
        user = users[user_id]
        return user
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='404, Id not found.')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, 
    log_level="info", reload="true" )