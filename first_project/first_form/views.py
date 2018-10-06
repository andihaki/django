from django.shortcuts import render

from . import forms

# Create your views here.
def index(request):
    data = {
        'form': 'form',
    }

    return render(request, 'first_form/index.html', context=data)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION OK")
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"TEXT: {form.cleaned_data['text']}")
    
    data = {
        'form': form,
    }

    return render(request, 'first_form/form_pages.html', context=data)