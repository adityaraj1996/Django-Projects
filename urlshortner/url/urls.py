from django.urls import path
from . import views

app_name = "url"

urlpatterns = [
    path("", views.urlshort, name="home"),
    path("<str:slugs>", views.urlRedirect, name="redirect")
]
