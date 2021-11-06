from django.urls import path
from api import views


urlpatterns = [
    path('',views.hello_world,name='hello_world'),
    path('<int:pk>',views.hello_world,name='hello_world'),
]
