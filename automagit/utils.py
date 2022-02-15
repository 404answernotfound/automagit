import requests
from yaml import load, FullLoader
from datetime import date
import os

today = date.today().strftime("%d%m%Y")


def search_user(username):
    print('search_user was called')
    response = requests.get("https://api.github.com/users/{}/followers".format(username))
    response = response.json()
        
    with open('logs/{}.txt'.format(today), 'w') as file:
        for i, res in enumerate(response):
            file.write(str(res) + '\n')

    with open('config/automa.yaml') as config:
            data = load(config, Loader=FullLoader)
            functions = data["automa"]["functions"]
            os.system(functions["commit"]["eval"])

def project_check():
    """Returns the answer"""
    print('42')

def check_config():
    with open('config/automa.yaml') as config:
        data = load(config, Loader=FullLoader)
        print('Working')