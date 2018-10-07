from django.conf.urls import url

from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),
    url('', views.index, name='index'),
]