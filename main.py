from typing import Union
import requests
from fastapi import FastAPI, status, Response
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return  roleUsers()
    

@app.get("/roleUsers/{encryptedToken}")
def read_item(encryptedToken : str):
    list=roleUsers()
    for item in list:
        if item["encryptedToken"]==encryptedToken:
            return item
    return Response(status_code= status.HTTP_204_NO_CONTENT)


def roleUsers():
    url='https://630264749eb72a839d6ef2ff.mockapi.io/roleUsers'
    response = requests.get(url, {}, timeout=5)
    return response.json()