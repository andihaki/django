from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # data dictionary yang akan di-inject ke index.html
    my_dict = {
        "insert_me" : "ini dikirim dari views.py",
    }
    return render(request, 'first_app/index.html', context=my_dict)