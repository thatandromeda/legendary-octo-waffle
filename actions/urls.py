from django.urls import path

from . import views

urlpatterns = [
    #path('actions/<int:id>/', views.permalink),
    path('', views.HomePage),
]