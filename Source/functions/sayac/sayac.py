# YKS-LGS Sayac
import requests
import json

def sayacYks():
    url = "http://www.canermastan.com:8080/yks"
    response = requests.request("GET",url)
    yks = json.loads(response.text)
    return yks

def sayacLgs():
    url = "http://www.canermastan.com:8080/lgs"
    response = requests.request("GET",url)
    lgs = json.loads(response.text)
    return lgs