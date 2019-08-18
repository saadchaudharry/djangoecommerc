from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name='about'),
    path("Tracker/",views.Tracker,name='tracker'),
    path("products/<int:myid>",views.productt,name='productVie'),
    path("ContactUs/",views.contact,name='contactus'),
    path("search/",views.search,name='search')
]