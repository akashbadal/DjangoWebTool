#This is user created file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'bootstrap.html')


def about(request):
    return HttpResponse("About this website:")


def textfile(request):
    with open("fun.txt", 'r+') as file:
        return HttpResponse(file.read())


def navigate(request):
    return HttpResponse('''<h1>Akash</h1><a href="https://www.facebook.com">Go to Facebook</a>''')


def removepun(request):
    return render(request,'removepun_1.html')


def capitalizefirst(request):

    return HttpResponse('Capitalizing the first letter <a href="/">Back to home</a>')


def spaceremove(request):
   # spaceremove = request.GET.get( )
    return HttpResponse('Removing the space<a href="/">Back to home</a>')


def charcount(request):
    return HttpResponse('Counting the character<a href="/">Back to home</a>')


def newlineremove(request):
    return HttpResponse('removing the new line<a href="/">Back to home</a>')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepun1 = request.POST.get('removepun', 'off')
    uppercase = request.POST.get('UpperCase','off')
    spaceremove = request.POST.get('Spaceremove','off')
    purpose = ""

    if removepun1 == 'on':
        punctuations = ''':,.-;"'()[]/!@*?_~`<>#&%$^'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose = "Punctuations Removed"

        #params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #return render(request, 'removepun_result.html',params)

    if uppercase == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose += " Upper Case"

        #params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        #return render( request, 'removepun_result.html',params)

    if spaceremove == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if (char ==" " and djtext[index-1]==" "):
                continue
            else : analyzed = analyzed + char
        djtext = analyzed
        purpose += " Space removed"

       # params = {'purpose': 'Space remover', 'analyzed_text': analyzed}
        #return render( request, 'removepun_result.html',params)

    if (removepun1 == "on" or spaceremove == "on" or uppercase== "on"):
        params = {'purpose': purpose, 'analyzed_text': djtext}
        return render(request , 'bootstrap_result.html', params)

    else: return HttpResponse( '''ERROR!!!!  <br>   <a href=/bootstrap>Back to Previous Page</a>''')

#def template_test(request):
#    return render(request, 'removepun_1.html')

def bootstrap(request):
    return render (request,'bootstrap.html')