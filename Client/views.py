from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def terms(request):
    return render(request, 'terms.html')
def privacy_policy(request):
    return render(request, 'privacy.html')