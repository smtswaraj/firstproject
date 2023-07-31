from django.shortcuts import render,HttpResponse

# Create your views here.
def display(request):
    # return HttpResponse('<marquee behavior="scroll" direction="up" scrollamount="1"><h1 style="color: rgb(255, 0, 76);">Welcome</h1></marquee><marquee behavior="scroll" direction="right" scrollamount="12"><h1 style="color: red;">Little Fast Scrolling</h1></marquee><marquee behavior="scroll" direction="left" scrollamount="20"><h1 style="color: red;">Fast Scrolling</h1></marquee><marquee behavior="scroll" direction="right" scrollamount="500"><h1 style="color: red;">Very Fast Scrolling</h1></marquee>')
    return render(request,'welcome.html',{'subname':'SQL'})