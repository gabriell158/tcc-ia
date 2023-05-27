import requests
from json import loads
from dotenv import load_dotenv
from os import environ
load_dotenv()
BASE_URL = environ['API_URL'] + environ['API_PORT']
def create_model_test():
    res = requests.post(BASE_URL + '/model')
    body = loads(res.text)
    if res.status_code != 200:
        raise Exception('Failed status code: ', res.status_code)
    
    if body['selected'] != False:
        raise Exception('Failed selected: ', body['selected'])
    
    if type(body['clusters']) != type([]):
        raise Exception('Failed clusters type: ', type(body['clusters']))
    
    for item in body['clusters']:
        if type(item) != type({}):
            raise Exception('Failed cluster type: ', type(item))
    print('OK')

def get_models_test():
    res = requests.get(BASE_URL + '/model')
    body = loads(res.text)
    assert type(body) == type([])

def select_model_test(model_id):
    res = requests.post(BASE_URL + '/model/' + model_id)


if __name__ == '__main__':
    get_models_test()
