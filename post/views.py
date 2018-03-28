from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    return render(request, 'post/index.html', {})

def test(request):
    posts = models.POST.objects.all()

    context = {
        'post': post,
    }

    return render(request, 'post/test.html', context)
