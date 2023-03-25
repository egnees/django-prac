import django.contrib.auth.models
from django.db import models
import django.utils.timezone


# Create your models here.

class Post(models.Model):

    STATUS_CHOICES = (
        ('published', 'Published'),
        ('draft', 'Draft')
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250, unique_for_date='created_at')

    author = models.ForeignKey(django.contrib.auth.models.User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    body = models.TextField()

    # will be set by user in the moment of publishing (?)
    published_at = models.DateTimeField(default=django.utils.timezone.now)

    # will be set in the moment of creation
    created_at = models.DateTimeField(auto_now_add=True)

    # will be updated each time object gets updated
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-published_at',)

    def __str__(self):
        return self.title
