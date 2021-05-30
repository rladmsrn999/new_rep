from django.urls import path
from . import views

urlpatterns = [
    path('', views.new, name='xres'),
    path('', views.new, name='yres'),

]