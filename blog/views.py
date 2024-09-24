#from django.http import HttpResponse
from django.shortcuts import render

def blog (request): 
    return render(request, "blog/index.html") #Criação de mais uma pasta dentro de templates, pois o Django busca em todas as pastas templates dos App arquivos HTML de mesmo nome3

def blog_interno (request): 
    return render(request, "blog/blog_interno.html")
