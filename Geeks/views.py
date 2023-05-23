from django.shortcuts import render
from Geeks.forms import GeeksForms

from django.forms import formset_factory

# Create your views here.

def home(request):
    context = {}
    GeeksFormSet = formset_factory(GeeksForms, extra=2)
    formset = GeeksFormSet(request.POST or None)
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
    
    # add formset to context dixnary_
    context['formset']=formset
    return render(request,'home.html',context)