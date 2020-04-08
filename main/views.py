from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth

# Create your views here.

def home(request):
    url = 'http://desktop-cmq34np/gt_qlik/qrs/app/full?xrfkey=123456789ABCDEFG'
    
    headers = {"X-Qlik-XrfKey": "123456789ABCDEFG",
            "Accept": "application/json",
            "hdr-usr": "DESKTOP-CMQ34NP\\user",
            "Content-Type": "application/json",
            "Connection": "Keep-Alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    
    session = requests.Session()
    session.auth = HttpNtlmAuth('desktop-cmq34np\\user','dktlqkf12', session)
    x = session.get(url, verify=False, headers = headers)

    # resp = requests.get(url,headers=headers)    
    # apps = resp.json
    apps = x.json
    response = render(request, 'index.html',{'x':x,'apps':apps})
    response['hdr-usr'] = "DESKTOP-CMQ34NP\\user"
    response['X-Qlik-xrfkey'] = "123456789ABCDEFG"
    return response