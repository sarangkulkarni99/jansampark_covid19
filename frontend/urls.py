from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('get_data', views.get_data, name='get_data'),
]