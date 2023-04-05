from fastapi import status
from fastapi.testclient import TestClient
from models import User
from main import app

client = TestClient(app)

def test_get_users():
    response = client.get('/users')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 3  # Verificar se a resposta contém 3 usuários

def test_post_user():
    user = User(id=4, nome="João da Silva", cpf="98765432100", chip="1111111111")
    response = client.post('/users', json=user.dict())
    assert response.status_code == status.HTTP_201_CREATED

def test_get_user():
    response = client.get('/users/1')
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['nome'] == 'Carlos Hansi Lopes'  # Verificar se o nome do usuário corresponde ao esperado

def test_get_user_not_found():
    response = client.get('/users/100')
    assert response.status_code == status.HTTP_404_NOT_FOUND
