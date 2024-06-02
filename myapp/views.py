from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.

def one(request):
    return render(request, 'form.html', {'form': ExampleForm})
