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


    for img in imglist:
        image=Image.open('/home/rladmsrn999/new_rep/blog/static/original/{}'.format(img))
        img_resize=image.resize((xres,yres))
        img_resize.save('/home/rladmsrn999/new_rep/blog/static/make/{}'.format(img))

    image=Image.new("RGB",(xres,yres),(0,0,0))

    im=image.load()
    for x in range(xres) :
        for y in range(yres) :
            if x>int(xres/2) :
                im[x,y]=(255,255,255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/BW1.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres) :
        for y in range(yres) :
            if y>int(yres/2) :
                im[x,y]=(255,255,255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/BW2.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres) :
        for y in range(yres) :
            if x%2==0 and y<int(yres/2):
                im[x,y]=(255,255,255)
            elif x%2==1 and y>=int(yres/2):
                im[x,y]=(255,255,255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Half-Vstripe.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres) :
        for y in range(yres) :
            if y%2==0 and x<int(xres/2):
                im[x,y]=(255,255,255)
            elif y%2==1 and x>=int(xres/2):
                im[x,y]=(255,255,255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Half-hstripe.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if y % 2 == 0:
                im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Hstripe.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if x% 2 == 0:
                im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Vstripe.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (x > int(xres*7/18) and x < int(xres*13/18)) and (y<int(yres/3) or y>int(yres*2/3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk1.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (x > int(xres * 11 / 18) and x < int(xres * 17 / 18)) and (y < int(yres / 3) or y > int(yres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk2.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (x > int(xres * 5 / 18) and x < int(xres * 11 / 18)) and (y < int(yres / 3) or y > int(yres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk3.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (x > int(xres * 1 / 18) and x < int(xres * 7 / 18)) and (y < int(yres / 3) or y > int(yres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk4.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (y > int(yres * 7 / 18) and y < int(yres * 13 / 18)) and (x< int(xres / 3) or x > int(xres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk5.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (y > int(yres * 11 / 18) and y < int(yres * 17 / 18)) and (x < int(xres / 3) or x > int(xres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk6.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (y > int(yres * 5 / 18) and y < int(yres * 11 / 18)) and (x< int(xres / 3) or x > int(xres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk7.png')

    image = Image.new("RGB", (xres, yres), (128, 128, 128))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if (y > int(yres * 1 / 18) and y < int(yres * 7 / 18)) and (x < int(xres / 3) or x > int(xres * 2 / 3)):
                im[x, y] = (0, 0, 0)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Xtalk8.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if x==xres/4 or x==xres/2 or x==xres*3/4 :
                im[x-3, y] = (255, 255, 255)
                im[x-2, y] = (255, 255, 255)
                im[x-1, y] = (255, 255, 255)
                im[x, y] = (255, 255, 255)
                im[x+1, y] = (255, 255, 255)
                im[x+2, y] = (255, 255, 255)
                im[x+3, y] = (255, 255, 255)
            if y==yres/4 or y==yres/2 or y==yres*3/4 :
                im[x, y-3] = (255, 255, 255)
                im[x, y-2] = (255, 255, 255)
                im[x, y-1] = (255, 255, 255)
                im[x, y] = (255, 255, 255)
                im[x, y+1] = (255, 255, 255)
                im[x, y+2] = (255, 255, 255)
                im[x, y+3] = (255, 255, 255)

    image.save('/home/rladmsrn999/new_rep/blog/static/make/LUCU.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if x>=xres/2-xres*7/20 and x<xres/2+xres*7/20  and y>=yres/2-yres*7/20  and y<yres/2+yres*7/20  :
                im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Loading49%.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            # if x >= xres / 2 - xres *5/20  and x < xres / 2 + xres *5/20 and y >= yres / 2 - yres *5/20 and y < yres / 2 + yres *5/20:
            #     im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Loading25%.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if x >= xres / 2 - xres *3/20 and x < xres / 2 + xres *3/20 and y >= yres / 2 - yres *3/20 and y < yres / 2 + yres *3/20:
                im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Loading9%.png')

    image = Image.new("RGB", (xres, yres), (0, 0, 0))
    im = image.load()
    for x in range(xres):
        for y in range(yres):
            if x >= xres / 2 - xres *1/20 and x < xres / 2 + xres *1/20 and y >= yres / 2 - yres *1/20 and y < yres / 2 + yres *1/20:
                im[x, y] = (255, 255, 255)
    image.save('/home/rladmsrn999/new_rep/blog/static/make/Loading1%.png')


    imglist = os.listdir('/home/rladmsrn999/new_rep/blog/static/make')
    imglist.sort()




    return render(request, 'blog/new.html', {'xres':xres, 'yres':yres, 'imglist':imglist})

