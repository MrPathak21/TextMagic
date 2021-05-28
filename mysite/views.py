# I have created this file - Shikhar
from django.http import HttpResponse
from django.shortcuts import render

'''
def index(request):
    return HttpResponse('<a href = "http://127.0.0.1:8000/navigation"> Click here to go to navigation page</a>')
def about(request):
    return HttpResponse('This is about page')
def navigation(request):
    return HttpResponse('<h1>Navigation</h1><a href = "http://www.google.com"> Google</a> <a href = "http://www.facebook.com"> Facebook</a> <a href = "http://www.twitter.com">Twitter</a>')
'''

def index(request):
    #para = {'name':'Shikhar','place':'Etawah'}
    return render(request, 'index.html')

def analyze(request):
    mytext = request.POST.get('text', 'default')
    punc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('uppercase', 'off')
    lineremove = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    text = mytext
    c = "Option Didn't selected "
    cn = "Option Didn't selected "
    if punc == "on":
        mytext = removepunc(mytext)

    if upper=="on":
        mytext = uppercase(mytext)

    if lineremove == 'on':
        mytext = lineremover(mytext)

    if spaceremover== 'on':
        mytext = spacerem(mytext)

    if charcount == 'on':
        c = charcounter(text)
        cn = charcounter(mytext)

    params = {'purpose': 'Removed Punctuations', 'analyzedtext': mytext, 'charcountold': c, 'charcountnew': cn}

    return render(request, 'analyze.html', params)
    #return HttpResponse('''<h1>  </h1> <a href = 'http://127.0.0.1:8000'>Back</a>''')

def about(request):
    return render(request, 'AboutUs.html')

def contact(request):
    return render(request, 'ContactUs.html')

def removepunc(s):
    result = ''
    p = '''`~!@#$%^&*()[{}]|:;"'<,>.?/'''
    for i in s:
        if i not in p:
            result += i
    return result

def uppercase(s):
    return s.upper()

def lineremover(s):
    result = ''
    for i in s:
        if i != '\n' and i != '\r':
            result += i
    return result

def spacerem(s):
    result = ''
    if s[0] != '':
        result += s[0]
    for i in range(1, len(s)):
        if s[i] == ' ' and s[i-1] == ' ':
            continue
        result += s[i]
    return result

def charcounter(s):
    count = 0
    for i in s:
        count += 1
    return count