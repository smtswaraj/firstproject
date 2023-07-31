from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
def display(request):
    # return HttpResponse('<marquee behavior="scroll" direction="up" scrollamount="1"><h1 style="color: rgb(255, 0, 76);">Welcome</h1></marquee><marquee behavior="scroll" direction="right" scrollamount="12"><h1 style="color: red;">Little Fast Scrolling</h1></marquee><marquee behavior="scroll" direction="left" scrollamount="20"><h1 style="color: red;">Fast Scrolling</h1></marquee><marquee behavior="scroll" direction="right" scrollamount="500"><h1 style="color: red;">Very Fast Scrolling</h1></marquee>')
    return render(request,'calculater.html',{'name':'Swaraj'})

def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    op = str(request.POST['opr'])
    if request.method=='POST':
        if op == '+':
            res = n1+n2
        elif op == '-':
            res = n1-n2
        elif op == '*':
            res = n1*n2
        elif op == '/':
            res = n1/n2
        else:
            messages.error(request,'Invalid Operater')
            return render(request,'result.html',{'result':'Enter a valid operator'})
    return render(request,'result.html',{'result':res})