from django.shortcuts import render
from .models import Operation
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, "add/home.html",{'name' : "adi"})


def operation(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    op = request.POST['operation']
    if op == 'add':
        res = val1 + val2
    elif op == 'subtract':
        res = val1 - val2
    ins = Operation(operation=op, num1=val1, num2=val2, result=res)
    ins.save()
    messages.success(request, "you result has been saved successfully..!!!")
    return render(request, 'add/result.html', {'result': res})





