from django.shortcuts import render
#login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# class base view
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from first_app.models import AccessRecord, Topic, Webpage
from first_app.models import UserProfileInfo

from first_app.forms import UserForm, UserProfileInfoForm

# untuk delete halaman 
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    # data dictionary yang akan di-inject ke index.html
    my_dict = {
        'access_record': webpages_list,
    }
    return render(request, 'first_app/index.html', context=my_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def idx(request):
    return render(request, 'default/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    data = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'first_app/registration.html', context=data)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Akun disable")
        else:
            print('wrong username / password')
            print(f"Username: {username}, Password: {password}")
    else:
        return render(request, 'first_app/login.html', {})

def other(request):
    return render(request, 'default/other.html')

def relative(request):
    return render(request, 'default/relative_url_templates.html')

# class base view
from . import models

class IndexView(TemplateView):
    template_name = 'first_app/index.html'

class SchoolListView(ListView):
    # jika tidak di define context_object_name
    # maka, context yang diinject ke html = school_list
    context_object_name = 'schools'

    model = models.School    

class SchoolDetailView(DetailView):
    # jika tidak di define context_object_name
    # maka, context yang diinject ke html = school
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'first_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("first_app:index")