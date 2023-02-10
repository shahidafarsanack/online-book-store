from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from mayflower.models import admindb,catdb,bookdb,contactdb
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login



# Create your views here.


def indexpage(request):
    return render(request,"index.html")

def adminpage(request):
    return render(request,"addadmin.html")

def savedata(request):

    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        img = request.FILES['image']
        us = request.POST.get('uname')
        ps = request.POST.get('pswrd')
        cn = request.POST.get('cnfrm')
    obj = admindb(Name = na,Mobile = mob,Email = em,Image = img,Uname = us,Pswrd = ps,Cnfrm = cn)
    obj.save()
    return redirect(adminpage)

def display(request):
    data=admindb.objects.all()
    return render(request,"displayadmin.html",{'data':data})


def editpage(request, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(request, "editadmin.html", {'data':data})

def updatepage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        us = request.POST.get('uname')
        ps = request.POST.get('pswrd')
        cn = request.POST.get('cnfrm')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=na,Mobile=mob,Email=em,Uname=us,Pswrd=ps,Cnfrm=cn,Image=file)
        return redirect(display)

def deletepage(request, dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(display)


def catpage(request):
    return render(request,"addcategory.html")

def datasave(request):
    if request.method == "POST":
        cn = request.POST.get('name')
        img = request.FILES['imag']
    obj = catdb(Catname=cn,Image=img)
    obj.save()
    return redirect(catpage)

def catdisplay(request):
    dt=catdb.objects.all()
    return render(request,"displaycategory.html",{'dt':dt})

def cateditpage(request, dataid):
    dt=catdb.objects.get(id=dataid)
    print(dt)
    return render(request, "editcat.html", {'dt':dt})

def catupdate(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('name')
        try:
            img = request.FILES['imag']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = catdb.objects.get(id=dataid).Image
        catdb.objects.filter(id=dataid).update(Catname=cn,Image=file)
        return redirect(catdisplay)

def catdelete(request, dataid):
    dt=catdb.objects.filter(id=dataid)
    dt.delete()
    return redirect(catdisplay)



def bookpage(request):
    dat=catdb.objects.all()
    return render(request,"addbook.html",{'dat':dat})


def booksave(request):
    if request.method == "POST":
        nam = request.POST.get('bname')
        na = request.POST.get('aname')

        my = request.POST.get('date')
        pri = request.POST.get('price')
        ab = request.POST.get('abt')
        img = request.FILES['image']
        ca = request.POST.get('cat')
    obj = bookdb(Bookname=nam,Authname=na,Pdate=my,Price=pri,About=ab,Image = img,Category=ca)
    obj.save()
    return redirect(bookpage)

def bookdisplay(request):
    dat=bookdb.objects.all()
    return render(request,"displaybook.html",{'dat':dat})


def bookedit(request, dataid):
    dat=bookdb.objects.get(id=dataid)
    da=catdb.objects.all()
    print(dat)
    return render(request, "editbook.html", {'dat':dat,'da':da})

def bookupdate(request, dataid):
    if request.method == "POST":
        nam = request.POST.get('bname')
        na= request.POST.get('aname')
        my= request.POST.get('date')
        pri = request.POST.get('price')
        ab = request.POST.get('abt')
        ca = request.POST.get('cat')

        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = bookdb.objects.get(id=dataid).Image
        bookdb.objects.filter(id=dataid).update(Bookname=nam,Authname=na,Pdate=my,Price=pri,About=ab,Image = file,Category=ca)
        return redirect(bookdisplay)

def bookdelete(request, dataid):
    dat=bookdb.objects.filter(id=dataid)
    dat.delete()
    return redirect(bookdisplay)

def contactsave(request):
    data=contactdb.objects.all()
    return render(request,"displaycontact.html",{'data':data})


def adminloginpage(request):
    return render(request,"adminlogin.html")

def adminlog(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(adminloginpage)
        else:
            return redirect(adminloginpage)


