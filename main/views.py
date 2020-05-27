from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth
import os
from accounts.decorators import *
from menu.models import Menu

# from deco import *

# Create your views here.
@login_message_required
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

    qlik_ticket = response.json()['Ticket']
    menu_list = Menu.objects.filter(writer=request.user).order_by('menu_rank')

    return render(request, 'index.html',{'qlik_ticket':qlik_ticket,'menu_list':menu_list})