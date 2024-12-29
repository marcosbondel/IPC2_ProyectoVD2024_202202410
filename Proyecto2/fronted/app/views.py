import requests
import json
from django.shortcuts import render, redirect
from .forms import LoginForm, FileForm, TextForm
from django.core.cache import cache
from django.http import HttpResponse
import plotly.graph_objs as go
import plotly.offline as pyo


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

                print(f'Response: {response}')

                redirection_page = redirect('login')

                match response['Rol']:
                    case 'admin':
                        # With cookies
                        redirection_page = redirect('admin_load_users')
                        redirection_page.set_cookie('uid', response['Id'])

                        return redirection_page
                    case 'user':
                        redirection_page = redirect('app_create')
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

def app_help(request):
    return render(request, 'help.html')

def app_create(request):
    return render(request, 'create.html')

def app_load_xml_design(request):
    ctx = {
        'content':None
    }
    try:
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            
            if form.is_valid():
                file = request.FILES['file']
                #guardamos el binario
                xml = file.read()
                decodified_xml = xml.decode('utf-8')
                context['xml_binary'] = xml
                context['file_content'] = decodified_xml
                ctx['content'] = decodified_xml

                return render(request, 'create.html', ctx)
    except:
        return render(request, 'create.html')

def app_create_image(request):
    ctx = {
        'content': None,
        'image': None
    }

    try:
        if request.method == 'POST':
            xml = context['xml_binary']

            if xml is None:
                return render(request, 'create.html')
            
            #Obtengo el id del usuario
            #http://localhost:4000/imagenes/carga/:id_usuario
            uid = request.COOKIES.get('uid')
            endpoint_load_image = f'{base_endpoint}/user/{uid}/images.json'

            response = requests.post(endpoint_load_image, data=xml)
            response = response.json()

            # print(f'Response: {response}')

            ctx['content'] = context['file_content']
            ctx['image'] = response['matrix']

            context['xml_binary'] = None
            context['file_content'] = None

            return render(request, 'create.html', ctx)
    except:
        return render(request, 'create.html',ctx)

def app_edit(request):
    return render(request, 'edit.html')

def app_edit_image(request):
    ctx = {
        'image1': None,
        'image2': None
    }

    try:
        if request.method == 'POST':
            form = TextForm(request.POST)

            if form.is_valid():
                action = request.POST.get('action')
                textid = form.cleaned_data['textid']
                filtro = 0

                if action == 'grayscale':
                    filtro = 1
                elif action == 'sepia':
                    filtro = 2

                data = {
                    'id': textid,
                    'filtro': filtro
                }

                #obtengo el id del usuario
                uid = request.COOKIES.get('uid')
                #peticion al backend
                endpoint_edit = f'{base_endpoint}/user/{uid}/images/edit.json'
                #convertimos la data a json
                json_data = json.dumps(data)

                #HEADERS
                headers = {
                    'Content-Type':'application/json'
                }

                #Hacemos la peticion al backend
                response = requests.post(endpoint_edit, data=json_data, headers=headers)
                response = response.json()

                # print(f'Response: {response}')

                ctx['image1'] = response['matrix1']
                ctx['image2'] = response['matrix2']

                return render(request, 'edit.html',ctx)
    except:
        return render(request, 'edit.html')

def admin_stats(request):
    ctx = {
        'plot_div': None,
        'plot_div2': None
    }
    
    endpoint_stats = f'{base_endpoint}/users/stats'

    response = requests.get(endpoint_stats)

    data = response.json()

    # print(f'Response: {data}')

    users = []
    num_images = []
    
    users2 = []
    num_edited = []

    for dato in data['top_3']:
        users.append(dato['uid'])
        num_images.append(dato['num_images'])
    
    for dato in data['edited_images_user']:
        users2.append(dato['uid'])
        num_edited.append(dato['num_edited'])
    
    #Dibujar mi grafica
    trace = go.Bar(
        y=num_images,
        x=users
    )
    
    trace2 = go.Bar(
        y=num_edited,
        x=users2
    )

    layout = go.Layout(
        title='Top 3 | Usuarios con mas imagenes',
        xaxis={
            'title': 'Usuarios',
        },
        yaxis={
            'title': 'Cantidad de imagenes',
        }
    )
    
    layout2 = go.Layout(
        title='Cantidad imagenes EDITADAS por usuario',
        xaxis={
            'title': 'Usuarios',
        },
        yaxis={
            'title': 'Cantidad de editadas',
        }
    )

    fig = go.Figure(data=[trace], layout=layout)
    fig2 = go.Figure(data=[trace2], layout=layout2)

    ctx['plot_div'] = pyo.plot(fig, include_plotlyjs=False, output_type='div')
    ctx['plot_div2'] = pyo.plot(fig2, include_plotlyjs=False, output_type='div')

    return render(request, 'stats.html', ctx)

def app_gallery(request):
    ctx = {
        'figures': None
    }

    uid = request.COOKIES.get('uid')
    endpoint_gallery = f'{base_endpoint}/users/{uid}/gallery.json'

    response = requests.get(endpoint_gallery)
    data = response.json()
    
    ctx['figures'] = data['gallery']

    return render(request, 'gallery.html', ctx)