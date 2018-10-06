from django.conf.urls import url

from first_form import views

urlpatterns = [
    url('', views.form_name_view, name='form')
]