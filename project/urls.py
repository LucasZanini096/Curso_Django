"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from blog import views as blog_views
from home import views as home_views

# HTTP Request (Cliente) <-> HTTP Response -> Stateless ( não há modifcação de dados entre o cliente e o servidor)
# MVT (Variação de MVC -> Model View Controlers)
#Envio uma requisição com dados para o servidor, e este servidor deve me enviar um resposta em relação a minha requisição


def my_view (request): #Sempre devo retornar algo em minha view, sendo a resposta em relação a minha request
    return HttpResponse("Uma mensagem para alguém especial")

#Function based view -> função de view
#Há tambem as views de classes !

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('home.urls')), #Estou incluindo todas as urls aninhadas em relação a um app
    path('blog/', include('blog.urls')),
    #path('my_view/', my_view) #Quando eu crio uma nova path em meu projeto, o Django já entende que não é necessário ter página de introdução do Framework
                              #Nenhuma URL pode começar com /

    path('admin/', admin.site.urls)
]
