from django.shortcuts import render
import os


def home(request):
    return render(request, 'blog/home.html')

def new(request):
    xres = request.GET.get('xres')
    yres = request.GET.get('yres')
    xres=int(xres)
    yres=int(yres)
    imglist=os.listdir('/home/rladmsrn999/new_rep/blog/static')

    return render(request, 'blog/new.html', {'xres':xres, 'yres':yres, 'imglist':imglist})

