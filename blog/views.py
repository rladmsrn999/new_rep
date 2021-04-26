from django.shortcuts import render
import os
from PIL import Image


def home(request):
    return render(request, 'blog/home.html')

def new(request):
    xres = request.GET.get('xres')
    yres = request.GET.get('yres')
    xres=int(xres)
    yres=int(yres)
    imglist=os.listdir('/home/rladmsrn999/new_rep/blog/static/original')  #호스팅용
    # imglist = os.listdir('./static/original')  #로컬용
    # imglist = imglist.sort()

    for img in imglist:
        image=Image.open('/home/rladmsrn999/new_rep/blog/static/original/{}'.format(img))
        img_resize=image.resize((xres,yres))
        img_resize.save('/home/rladmsrn999/new_rep/blog/static/make/{}'.format(img))

    imglist = os.listdir('/home/rladmsrn999/new_rep/blog/static/make')




    return render(request, 'blog/new.html', {'xres':xres, 'yres':yres, 'imglist':imglist})

