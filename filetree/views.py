from django.shortcuts import render
from .models import Files

# Create your views here.
def index(request):
    context = {}
    context['files'] = Files.objects.all()
    return render(request, 'index.html', context)