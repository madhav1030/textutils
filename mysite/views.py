# This file is created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('"HELLO" <a href="https://www.youtube.com/results?search_query=code+with+harry">Learn Code</a>')
   # params = {'name': 'Mad', 'place':'Mars'}
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("about madhav")

# def removepunc(request):
#     #get the text
#     djtext= request.GET.get('text', 'default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("removepunc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("removeline")

# def spaceremove(request):
#     return HttpResponse("remove space")

# def charcount(request):
#     return HttpResponse("count char")


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
