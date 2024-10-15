import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"

#1получение ключа
def test_UG2(login = "shevedasha@ya.ru", password = "ivs9;3O1", 
             companyID = "4073b2bb-8803-466e-a3d7-32ccda6987f0"):
    payload = {
        "login": login,
        "password": password,
        "companyId": companyID 
        }
    keys = requests.post(base_url+'/auth/keys', json=payload)
    key = keys.json()

    assert keys.status_code == 201

#2список проектов
def test_projects():
    payload = {
        "login": "shevedasha",
        "password": "ivs9;3O1",
        "companyId": "4073b2bb-8803-466e-a3d7-32ccda6987f0"
        }
    my_heders = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eXeJQIw0OUHwcjbr7tnNjWEehLa9DOlyxPM-3i6gedM0tnFjihRiV-c9Pov034MT"
    }
    resp = requests.get(base_url+'/projects')
    full_list = resp.json()

    assert len(full_list) > 0

#3создать новый проект

def test_new_projects():
    payload = {
        "login": "shevedasha",
        "password": "ivs9;3O1",
        "companyId": "4073b2bb-8803-466e-a3d7-32ccda6987f0"
        }
    my_heders = {
        "Content-Type": "application/json",
        "Authorization": "Bearer s7SMnbOLAbCuymBN8kAt+EjnVVqANZbEtPW49ATBRgWteA03QZdMMxdxKyMLEQPS"
    }
    new = {
    "title": "Справки для студентов",
    "users": {
        "634682e6-e192-43c2-ad22-8b0d8f4d650b": "admin"
        }
    }
   
    response = requests.post(base_url+'/projects')
    new_new = response.json()
    
    assert response.status_code == 201
