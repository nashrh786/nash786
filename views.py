#thisisfilemadefortesting
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#paras={'name':'nash','place':'pune'}
   #return render(request, 'index.html',paras)
def index(request):
    return render(request, 'index.html')

def analyze( request):
    mytext = request.GET.get('text', 'off')
    mycheckbox = request.GET.get('checkboxxx','default')
    upbox=request.GET.get('upbox', 'off')
    capbox=request.GET.get('capbox', 'off')
    charbox=request.GET.get('charbox', 'off')


    punctuations='''#(){}'\/@$%^*-_<>![]'''
    analyzed=""
    if mycheckbox=="on":
        for char in mytext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'analyzed_text':analyzed}
        return render(request, 'analyze.html',params)
    elif upbox=="on":
        for char in mytext:
            analyzed = analyzed+char.upper()
        params = {'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif capbox=="on":
        for char in mytext:
            analyzed = analyzed+char.capitalize()
        params = {'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    elif charbox=="on":
        for char in mytext:
            analyzed = analyzed + char
            totalcont=len(analyzed)
        params = {'analyzed_text': totalcont}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error no checkbox selected")








