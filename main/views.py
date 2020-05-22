from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth
import os

# Create your views here.

def home(request):
    requests.packages.urllib3.disable_warnings()
    url = "https://localhost:4243/qps/qlik_ticket/ticket?Xrfkey=abcdefghijklmnop"
    # 인증서 경로
    _client = os.path.join(os.path.dirname(__file__),'client.pem')
    _client_key = os.path.join(os.path.dirname(__file__),'client_key.pem')
    cert = (_client,_client_key)
    payload = "\r\n{\r\n  \"UserDirectory\": \"desktop-cmq34np\",\r\n  \"UserId\": \"user\"\r\n}"
    headers = {
    'x-Qlik-Xrfkey': 'abcdefghijklmnop',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload, cert=cert, verify=False)
    # print(response.json()['Ticket'])
    # print(response.json())
    qlik_ticket = response.json()['Ticket']
    # print(qlik_ticket)
    # url_sess = "https://DESKTOP-CMQ34NP/qlik_ticket/qrs/about?Xrfkey=abcdefghijklmnop&Qlikticket={}".format(qlik_ticket)
    # payload_sess  = {}
    # headers_sess = {
    #   'x-Qlik-Xrfkey': 'abcdefghijklmnop'
    # }
    # response = requests.request("GET", url_sess, headers=headers_sess, data = payload_sess, cert=cert, verify=False)
    # print(qlik_ticket)
    # ticket_session =  response.cookies['X-Qlik-Session-ticket']
    return render(request, 'index.html',{'qlik_ticket':qlik_ticket})