from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('generate_pdf/hello_world/', generate_helloWorld, name="generate_helloWorld"), 
    path('generate_pdf/form/', generate_form, name="generate_form"), 
    path('generate_pdf/letter/', generate_letter, name="generate_letter"), 
    path('generate_pdf/table/', gen_table, name="gen_table"), 

    path('resume/', resume, name="resume"), 
    path('demo/', demo, name="demo"), 


]