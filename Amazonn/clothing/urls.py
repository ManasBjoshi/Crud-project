from django.urls import path
from clothing import views
urlpatterns =[
    path("",views.home, name="home")
]