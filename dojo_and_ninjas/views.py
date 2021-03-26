from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.

def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all()
    }
    return render(request, 'dojo_and_ninjas.html', context)

def add_dojo(request):
    Dojo.objects.create(name=(request.POST['dojo_name']),city=(request.POST['dojo_city']), state=(request.POST['dojo_state']))
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(
        name=(request.POST['ninja_name']),
        dojo=Dojo.objects.get(id=(request.POST['dojo']))
        )
    return redirect('/')