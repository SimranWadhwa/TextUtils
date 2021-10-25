#Simran created this file
from django.http import HttpResponse, request
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>Hello</h1> \n <a href='https://github.com/SimranWadhwa/TrainingPython-FIL/tree/main/db'>MongoDB</a> \n <a href='https://github.com/SimranWadhwa/TrainingPython-FIL/tree/main/postgres'>SQL</a>") #Can write HTML tags as well

# def about(request):
#     return HttpResponse("About Simran Wadhwa")

# def program(request):
#     a=''
#     with open("../try.txt","r") as file:
#         for line in file:
#             a=a+line.rstrip()+" "
#     return HttpResponse(a)

def index(request):
    params={'name':'Simran', 'purpose':'practice'}
    return render(request,'index2.html', params)
    # return HttpResponse("<h1>HOME</h1><a href='http://127.0.0.1:8000/removepunc'><h2>1\n</h2></a><a href='http://127.0.0.1:8000/capitalizefirst'><h2>2\n</h2></a><a href='http://127.0.0.1:8000/newlineremove'><h2>3\n</h2></a><a href='http://127.0.0.1:8000/spaceremove'><h2>4\n</h2></a><a href='http://127.0.0.1:8000/charcount'><h2>5\n</h2></a>")

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    charcount=request.POST.get('charcount', 'off')
    # print(removepunc)
    # print(djtext)
    if removepunc=='on':
        analyzedtext=''
        for i in djtext:
            if i not in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
                analyzedtext+=i
        # print(analyzedtext)
        params1={'answer':analyzedtext,'purpose':'Remove Punctuations'}
        return render(request,'analyze2.html', params1)
    elif charcount=='on':
        params1={'answer':len(djtext),'purpose':'Character Count'}
        return render(request,'analyze2.html', params1)
        

    else:
        return HttpResponse("Error")
    # return HttpResponse("<h2>remove punctuation</h2><a href='http://127.0.0.1:8000/'>Back to home</a>")

def about(request):
    return render(request, 'about.html')
# def capfirst(request):
#     return HttpResponse("<h2>capitalize first</h2><a href='http://127.0.0.1:8000/'>Back to home</a>")

# def newlineremove(request):
#     return HttpResponse("<h2>new line remove</h2><a href='http://127.0.0.1:8000/'>Back to home</a>")

# def spaceremove(request):
#     return HttpResponse("<h2>space remove</h2><a href='http://127.0.0.1:8000/'>Back to home</a>")

# def charcount(request):
#     return HttpResponse("<h2>character count</h2><a href='http://127.0.0.1:8000/'>Back to home</a>")
