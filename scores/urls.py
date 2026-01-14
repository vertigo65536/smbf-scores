from django.urls import path
from scores import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.view, name="view"),
    path("rawview/", views.rawview, name="rawview"),
    path("updatescores/", views.updatescores, name="updatescores"),
    path("getslug/", views.getslug, name="getslug"),
    path("getsets/", views.getsets, name="getsets"),
]
