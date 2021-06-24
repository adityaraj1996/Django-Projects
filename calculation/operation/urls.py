from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('operation', views.operation, name='add'),

]