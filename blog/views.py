from django.shortcuts import render
from PIL import Image

def home(request):
    return render(request, 'blog/home.html')

def new(request):
    xres = request.GET.get('xres')
    yres = request.GET.get('yres')
    xres=int(xres)
    yres=int(yres)

    return render(request, 'blog/new.html', {'xres':xres, 'yres':yres})