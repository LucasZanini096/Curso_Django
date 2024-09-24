#from django.http import HttpResponse #Me permite renderizar HTML, porém apenas por string
from django.shortcuts import render  #Me permite renderizar um arquivo HTML

context = {
    'text' : "Bem vindo ao home do Django"
}
def home (request): #Function based view -> função de view
    #Há tambem as views de classes !
    return render(
        request,
        "home/home.html", #Busca da pasta templates
        context,
    )