from django.urls import path
from projectapp import views

app_name = "projectapp"

urlpatterns = [
path('',views.index_view,name='index')
]