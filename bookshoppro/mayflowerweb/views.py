from django.shortcuts import render,redirect
from mayflowerweb.models import logindb


# Create your views here.
from mayflower.models import catdb,bookdb,contactdb


def homepage(request):
    data=catdb.objects.all()
    product = bookdb.objects.all()
    context = {
        'product': product,
        'data': data,
    }
    return render(request,"home.html",context)

def aboutpage(request):
    return render(request,"aboutus.html")

def contactpage(request):
    data=catdb.objects.all()
    return render(request,"contactus.html",{'data':data})

def consave(request):
    if request.method == "POST":
        na= request.POST.get('name')
        il = request.POST.get('email')
        ms = request.POST.get('msg')
        obj = contactdb(Name=na,Email=il,Message=ms)
        obj.save()
    return redirect(contactpage)

def discategory(request,itemcatg):
    data=catdb.objects.all()
    print("===itemcatg===",itemcatg)
    catg=itemcatg.upper()
    products=bookdb.objects.filter(Category=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"categorydisplay.html",context)

def disauther(request,itemcat):
    data=catdb.objects.all()
    print("===itemcat===",itemcat)
    cat=itemcat.upper()
    product=bookdb.objects.filter(Authname=itemcat)
    context={
        'product':product,
        'cat':cat,
        'data':data,
    }
    return render(request,"autherdisplay.html",context)


def bookdetails(request,dataid):
    data=bookdb.objects.get(id=dataid)
    return render(request,"bookdetails.html",{'dat':data})

def pagelogin(request):
    return render(request,"login.html")

def logindata(request):
    if request.method == "POST":
        us = request.POST.get('usrname')
        il = request.POST.get('mail')
        pd = request.POST.get('pswrd1')
        cd = request.POST.get('cnfrm1')
        if pd == cd:
           obj = logindb(username=us,email=il, password=pd, confirmpassword=cd)
           obj.save()
           return redirect(pagelogin)
        else:
            return render(request,'login.html')


def registerdata(request):
    if request.method == "POST":
        us = request.POST.get('usrname')
        pd = request.POST.get('pswrd1')
        if logindb.objects.filter(username=us, password=pd).exists():
            # obj = LoginRegister(UserName=un, Password=pd).values('email','id').first()
            request.session['usrname'] = us
            request.session['pswrd1'] = pd
            # request.session['email']=data['email']
            # request.session['userid']=data['id']
            return redirect(homepage)
        else:

            return render(request, 'login.html', {'msg': "Sorry... password not matched."})


def logout(request):
    del request.session['usrname']
    del request.session['pswrd1']
    return redirect(homepage)
