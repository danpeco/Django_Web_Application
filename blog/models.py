from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    # when create a post it doesn't know were to redirect
    # this will tell it were to find the url of the model object
    # of a especific instance
    # reverse: will return full url to the rout as a string
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

