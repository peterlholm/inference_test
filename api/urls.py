from django.urls import path

from . import views

urlpatterns = [
    path('v1/inference', views.infer, name="infer"),
    path('infer', views.infer),
    path('finfer', views.finfer),
    path('pinfer', views.pinfer, name="pinfer"),
    path('vinfer', views.vinfer, name="vinfer")
]
