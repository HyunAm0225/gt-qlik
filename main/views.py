from django.shortcuts import render
import requests
from requests_ntlm import HttpNtlmAuth
import os
from accounts.decorators import *
from menu.models import Menu
from chart.models import Chart

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
    username = request.user
    print(username)
    payload = f'{{"UserDirectory":"desktop-cmq34np","UserId" :"{username}"}}'
    print(payload)

    headers = {
    'x-Qlik-Xrfkey': 'abcdefghijklmnop',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload, cert=cert, verify=False)

    qlik_ticket = response.json()['Ticket']
    menu_list = Menu.objects.order_by('menu_rank')
    chart_list = Chart.objects.order_by('chart_rank')

    first_menu = menu_list[:1]
    # print(first_menu)
    # print(menu_list)

    return render(request, 'index.html',{'qlik_ticket':qlik_ticket,'menu_list':menu_list,'chart_list':chart_list,'first_menu':first_menu})