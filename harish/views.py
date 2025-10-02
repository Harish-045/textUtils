from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    return render(request,'harish.html' )
def analyze(request):
    det=request.POST.get('text','default')
    removpunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newliner=request.POST.get('newlineremover','off')
    lowercase=request.POST.get('lowercase','off')



    if removpunc=='on':
        punc=''''''' " ` - – — ( ) [ ] { } < >,. … /:'"? \ @ # % & * + = ^ _ ~ |"""
        analyzed=""
        for char in det:
            if char not in punc:
                analyzed=analyzed+char
        param={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        det=analyzed
    if capitalize=='on':
        analyzed = ""
        for char in det:

            analyzed=analyzed+char.upper()
        param={'purpose':'Capitalization','analyzed_text':analyzed}
        det=analyzed
    if lowercase == "on":

        analyzed = ""
        for index, char in enumerate(det):
            if not (det[index] == " " and det[index + 1] == " "):
                analyzed = analyzed + char

        param = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        det = analyzed
    if newliner=='on':
        analyzed = ""
        for char in det:
            if char!='\n' and char!='\r':
                analyzed=analyzed+char


            print("pre",analyzed)

        param={'purpose':'Newline Remover','analyzed_text':analyzed}

        det=analyzed



    if(removpunc=='off' and capitalize=='off' and newliner=='off' and lowercase=='off' ):
        return HttpResponse("Please Select Any Operation and Try again")
    return render(request, 'analyze.html', param)

      #def navigation(request):
    #