from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth
import os

# Create your views here.

def home(request):
    requests.packages.urllib3.disable_warnings()
    url = 'http://desktop-cmq34np/gt_qlik/qrs/app/full?xrfkey=123456789ABCDEFG'
    login_url = 'https://localhost:4243/qps/gt_qlik/session?Xrfkey=123456789ABCDEFG'
    xrf = '123456789ABCDEFG'
    headers = {'X-Qlik-xrfkey': xrf,
        "Content-Type": "application/json",
        "X-Qlik-User":"DESKTOP-CMQ34NP\\user",
        "Accept": "application/json",
        "hdr-usr": "DESKTOP-CMQ34NP\\user",
        "Content-Type": "application/json",
        "Connection": "Keep-Alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }
    cert = ('client.pem','client_key.pem')
    
    session = requests.Session()
    session.auth = HttpNtlmAuth('desktop-cmq34np\\user','dktlqkf12', session)
    x = session.get(url, verify=False, headers = headers)
    resp = requests.get(login_url, headers=headers, verify=False, cert=cert)

    # resp = requests.get(url,headers=headers)    
    # apps = resp.json
    apps = x.json
    response = render(request, 'index.html',{'x':x,'apps':apps,'resp':resp})
    response['hdr-usr'] = "DESKTOP-CMQ34NP\\user"
    response['X-Qlik-xrfkey'] = "123456789ABCDEFG"
    return response