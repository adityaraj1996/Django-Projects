from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post



# Create your views here.

def home(request):
    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query) > 70:
        allposts = Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allposts = allpostsTitle.union(allpostsContent)
    if allposts.count() == 0:
        messages.warning(request, "Please refine your query")

    context = {'allposts' : allposts, 'query': query}
    return render(request,'home/search.html',context)


def signup(request):
    if request.method == 'POST':
        # get post parameters
        username = request.POST['uname']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        # check for erroneous input
        if len(username) < 13:
            messages.error(request, "username can not be less than 13 characters")
            return redirect('home')

        elif not username.isalnum():
           messages.error(request, "username needs to be alphanumeric ")
           return redirect('home')

        elif not password1 == password2:
           messages.error(request, "password does not match ")
           return redirect('home')





        # create user
        myuser = User.objects.create_user(username, email, password1)
        myuser.save()
        messages.success(request, "Your Icoder Account has been successfully created..!!!")
        return redirect('home')



    else:
        return HttpResponse("404-Not found")


def signin(request):
    if request.method == 'POST':
        # get post parameters
        username = request.POST['loginusername']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "loggged in successfully")
            return redirect('home')
        else:
            messages.error(request, "invalid login credentials")
            return redirect('home')


    else:
        return HttpResponse("404-Not found")


def signout(request):
    logout(request)
    messages.success(request, "loggged out successfully")
    return redirect('home')











def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if len(name) < 2 or len(email) < 2 or len(phone) < 10 or len(desc) < 10:
            messages.error(request, "Please fill the form correctly..")
        else:
                ins = Contact(name=name, email=email, phone=phone, desc=desc)
                ins.save()
                messages.success(request, "you message has been sent successfully..!!!")



    return render(request,'home/contact.html')
