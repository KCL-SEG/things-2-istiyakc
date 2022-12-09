from django.shortcuts import render
from .froms import ThingForm

def home(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
