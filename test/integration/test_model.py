import requests
from json import loads
from dotenv import load_dotenv
from os import environ
from time import sleep

load_dotenv()
BASE_URL = environ['API_URL'] + environ['API_PORT']
model_id = ''

def test_create_model():
    global model_id
    res = requests.post(BASE_URL + '/model')
    body = loads(res.text)
    model_id = body['id']
    assert res.status_code == 200
    assert body['selected'] == False
    assert type(body['clusters']) == type([])
    for item in body['clusters']:
        assert type(item) == type({})

def test_get_models():
    res = requests.get(BASE_URL + '/model')
    body = loads(res.text)
    assert res.status_code == 200
    assert type(body) == type([])
    for model in body:
        assert type(model) == type({})
        assert type(model['date']) == type('')
        assert type(model['selected']) == type(False)
        assert type(model['clusters'] == type([]))
        for cluster in model['clusters']:
            assert type(cluster) == type({})

def test_select_model():
    global model_id
    res = requests.post(BASE_URL + '/model/' + model_id)
    assert res.status_code == 200

def test_delete_model():
    global model_id
    res = requests.delete(BASE_URL + '/model/' + model_id)
    assert res.status_code == 200

    

