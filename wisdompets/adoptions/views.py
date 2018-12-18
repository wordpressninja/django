from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet

# Home view
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

# Pet_Detail view
def pet_detail(request, id):
    try:
        pet = Pet.objects.get(id=id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(request, 'pet_detail.html', {'pet': pet})
