from django.shortcuts import render
from .forms import LoginForm
import requests
import json


base_endpoint = 'http://localhost:3000'

# Create your views here.

#Esta es una vista de ejemplo, pero puedes agregar las que necesites
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def do_login(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            
            if form.is_valid():
                uid = form.cleaned_data['uid']
                password = form.cleaned_data['password']

                sign_in_endpoint = f'{base_endpoint}/sign_in.json'
                data = {
                    'id': uid,
                    'password': password
                }

                json_data = json.dumps(data)

                headers = {
                    'Content-Type': 'application/json'
                }

                response = request.post(sign_in_endpoint, data=json_data, headers=headers)
                response = response.json()

                print(response)

            return render(request, 'login.html')
    except Exception as e:
        print(f'Error: {e}')
        return render(request, 'login.html')