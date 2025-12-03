from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'client/index.html')
def login(request):
    return render(request, 'client/login.html')
def terms(request):
    return render(request, 'client/terms.html')
def privacy_policy(request):
    return render(request, 'client/privacy.html')