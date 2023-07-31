from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def january(request):
#     return HttpResponse('First month of the year')
# def february(request):
#     return HttpResponse('Shortest month of the year')
# def march(request):
#     return HttpResponse('Exam month of the year')
# -----------------------------------------------------
d = {
    'january': 'First month of the year',
    'february': 'Shortest month of the year',
    'march': 'month of the Exam',
    'april': 'Month of Fools',
    'may': 'Month of vaccation',
    'june':'Month of Admission',
    'july':'longest month',
    'august':'No Non-veg Month',
    'september':'Ganpati bappa moreya',
    'october':"i don't know about october",
    'november':'Month of light',
    # 'december':'Chilling winter Month',
    'december':None,
}
def index(request):
    l = list(d)
    # out = ''
    # for i in l:
        # out+=f'''<li><a style="text-decoration: none;" href="{reverse('dis',args=[i])}">{i}</a></li>'''
        # out+=f'''<li><a href={'/mon/'+ i}>{i}</a></li>'''
    # res = f'<ul style="list-style-type: none;">{out}</ul>'
    # return HttpResponse(res)
    return render(request,"index.html",{"data":l})

def month_with_num(request, month):
    l = list(d)
    data = l[month-1]
    red_path = reverse('dis',args=[data])
    return HttpResponseRedirect(red_path)
    # return HttpResponseRedirect('/mon/'+data)
def monthes(request, month):
    # if month == 'january':
    #     msg = 'First month of the year'
    # elif month == 'february':
    #     msg = 'Shortest month of the year'
    # elif month == 'march':
    #     msg = 'month of the Exam'
    # else:
    #     return HttpResponseNotFound('Invalide month')
    # return HttpResponse(msg)
    try :
        # return HttpResponse(d[month])
        return render(request,'month.html',{'message':d[month],'m':month})
    except:
        return HttpResponseNotFound('<h1>Invalid Month name</h1>')