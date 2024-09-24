from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='index'), #Neste caso a raíz em relação a essa path é blog/, na qual está declarada em project.urls
    path('blog_interno/', views.blog_interno, name='blog-interno'),

]