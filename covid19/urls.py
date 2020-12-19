from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeview, name='home'),
    path('countrywise/', views.countryview, name='country'),
    path('countrieswise/<str:ccode>/', views.cntview, name='countries'),
]
