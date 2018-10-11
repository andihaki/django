from django.conf.urls import url, include
from django.urls import path

from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

school_patterns = ([
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
], 'first_app')

urlpatterns = [
    url('relative/', views.relative, name='relative'),
    url('other/', views.other, name='other'),
    url('register/', views.register, name='register'),
    url('login/', views.user_login, name='user_login'),
    # path('<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),
    # url('', views.SchoolListView.as_view(), name='list'),
    path('', include(school_patterns))
    # url('', views.IndexView.as_view(), name='index'),
]