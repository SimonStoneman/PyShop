from django.urls import path
from . import views # import views from current dir

urlpatterns = [
    path('', views.index), # for root or homepage
    path('new', views.new)
]