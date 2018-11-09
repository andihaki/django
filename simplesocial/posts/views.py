from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequireMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import models
from . import forms

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model() # ambil session dari user yang login

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group') # mixin dari tuple

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            # user dari post yang sedang di-open
            # ambil semua post dari user tsb
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        # __ = object relation model
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequireMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequireMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)
    
    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post dihapus')
        return super().delete(*args, **kwargs)
    