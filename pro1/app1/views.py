from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def add_view(request):
    template_name = 'app1/add.html'
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Data added Successfully......')
    context = {'form':form}
    return render(request, template_name, context)