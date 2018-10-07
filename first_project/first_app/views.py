from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    # data dictionary yang akan di-inject ke index.html
    my_dict = {
        'access_record': webpages_list,
    }
    return render(request, 'first_app/index.html', context=my_dict)

def idx(request):
    return render(request, 'default/index.html')

def other(request):
    return render(request, 'default/other.html')

def relative(request):
    return render(request, 'default/relative_url_templates.html')