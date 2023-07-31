from django.shortcuts import render
from .models import Desc
from django.http import HttpResponse

# Create your views here.
def test(request):
    # return HttpResponse("i am going to make naukri.com clone")
    return render(request,'naukri_nav.html')
def job_desc(request):
    desc = Desc.objects.get(id = 1)
    return render(request,'job_page.html',{'rating':desc.rating,'review':desc.review, 'yrs':desc.yrs,'day':desc.day, 'droll':desc.droll})