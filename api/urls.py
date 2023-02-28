from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('infer', views.infer, name="infer"),
    path('tinfer', views.tinfer, name="tinfer"),
    path('finfer', views.tinfer, name="finfer")
]
