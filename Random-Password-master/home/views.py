from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def home( request):
  return render(request,'home.html')
def back(request):
    return render(request,'home.html')

def password(request):

    characters=list('abcdefghijklmnopqrst')
    length=int(request.GET.get('select number',12))
    global newpassword
    newpassword = ''
    if request.GET.get('specialcharacter'):
        characters.extend(list('@#^&*?/<>+'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('UPPER'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    #else:
        #return HttpResponse("please fill the lenth of the password")
    for i in range(0, length):
        newpassword += random.choice(characters)
    return render(request,'final.html',{'password':newpassword})
def download(request):
    return render(request,'download.html',{'key': newpassword})
def blog(request):
    return render(request,'blog.html')
def privacy(request):
    return render(request,'privacy.html')