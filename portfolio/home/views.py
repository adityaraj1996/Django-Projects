from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    context_dic = {'name':'Aditya'}
    return render(request,'index.html',context_dic)
    # return HttpResponse("welcome to index page..!!!")


def about(request):
    return render(request,'about.html')
    # return HttpResponse("welcome to About page..!!!")


def project(request):
    return render(request,'project.html')
    # return HttpResponse("welcome to Projects page..!!!")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("the data has been written to DB")

        print(name,email,phone,desc)
    return render(request,'contact.html')
    # return HttpResponse("welcome to Contact page..!!!")
