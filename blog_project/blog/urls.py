from django.conf.urls import url
from blog import views

urlpatterns = [
    url('', views.PostListView.as_view(), name='post_list'),
    url('about/', views.AboutView.as_view(), name='about'),
    url('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
]