from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'post/index.html', {})

def test(request):
    return render(request, 'post/test.html', {})
