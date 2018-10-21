from django.shortcuts import render
from blog.models import Post, Comment
from django.views.generic import (TemplateView, ListView
                                    ,DetailView, CreateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # __lte => less than or equal to
        # -published_date => '-' maksudnya urut descending
        return Post.objects.filter(published_date__lte=timezone.now.order_by('-published_date'))

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post