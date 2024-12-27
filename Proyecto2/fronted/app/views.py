from django.shortcuts import render, redirect
from .forms import LoginForm, FileForm
import requests
import json
from django.core.cache import cache
from django.http import HttpResponse


base_endpoint = 'http://localhost:3000'

context = {
    'file_content': None,
    'xml_binary': None
}

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

                response = requests.post(sign_in_endpoint, data=json_data, headers=headers)
                response = response.json()

                redirection_page = redirect('login')

                match response['Rol']:
                    case 'admin':
                        # With cache
                        # cache.set('uid', response['Id'], timeout=None)

                        # With cookies
                        redirection_page = redirect('admin_load_users')
                        redirection_page.set_cookie('uid', response['Id'])

                        return redirection_page
                    case 'user':
                        redirection_page = redirect('app')
                        redirection_page.set_cookie('uid', response['Id'])
                        
                        return redirection_page
                    case _:
                        return render(request, 'login.html')



            return render(request, 'login.html')
    except Exception as e:
        print(f'Error: {e}')
        return render(request, 'login.html')


def administration(request):
    return render(request, 'administration.html')

def admin_load_users(request):
    return render(request, 'load_users.html')

def admin_load_users_xml(request):
    ctx = {
        'content': None
    }

    try:
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)

            if form.is_valid():
                file = request.FILES['file']

                #guardamos el binario
                xml = file.read()
                decodified_xml = xml.decode('utf-8')

                #guardamos el contenido del archivo en nuestro context global
                context['xml_binary'] = xml
                context['file_content'] = decodified_xml
                #guardamos el contenido del archivo en nuestro context local
                ctx['content'] = decodified_xml

                return render(request, 'load_users.html', ctx)
    except Exception as e:
        print(f'ERROR: {e}')
        return render(request, 'load_users.html')


def admin_send_users_xml(request):
    try:
        if request.method == 'POST':
            xml = context['xml_binary']
            if xml is None:
                return render(request, 'load_users.html')
            
            #Peticion al backend
            endpoint_load_users = f'{base_endpoint}/users/load.json'

            response = requests.post(endpoint_load_users, data=xml)
            response = response.json()
            
            context['xml_binary'] = None
            context['file_content'] = None

            return render(request, 'load_users.html')
    except:
        return render(request, 'load_users.html')

def admin_users(request):
    ctx = {
        'users': None
    }

    endpoint_users = f'{base_endpoint}/users.json'

    response = requests.get(endpoint_users)
    data = response.json()
    
    ctx['users'] = data

    return render(request, 'users.html', ctx)

def admin_users_xml(request):
    ctx = {
        'xml_content':None
    }

    endpoint_xml = f'{base_endpoint}/users.xml'
    
    response = requests.get(endpoint_xml)
    data = response.text

    ctx['xml_content'] = data

    return render(request, 'xml_users.html', ctx)

def logout(request):
    #si estas usando cache
    #cache.delete('id_user')
    #si estas usando cookies
    response = redirect('login')
    response.delete_cookie('uid')
    return response

def app(request):
    return render(request, 'app.html')