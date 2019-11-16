from django.urls import path
from . import views

app_name = "dmain"

urlpatterns = [
    path('',views.index, name = 'index'),
]