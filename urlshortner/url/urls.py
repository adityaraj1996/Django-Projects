from django.urls import path
from . import views

app_name = "url"

urlpatterns = [
    path("", views.index, name="home"),
    path("urlshort", views.urlshort, name="urlshort"),
    path("<str:slugs>", views.urlRedirect, name="redirect")
]
