from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete='CASCADE')
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date = timezone.now
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # default
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete='CASCADE')
    author = models.CharField(max_length=125)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    # kembali ke homepage / post list
    def get_absolute_url(self):
        return reverse('post_list')
    
    def __str__(self):
        return self.text

