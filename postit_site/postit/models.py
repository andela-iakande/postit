from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
#from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.

class Post(models.Model):
    """This class represents the meetup model."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=255, blank=False, unique=True)
    text = models.TextField(max_length=255, blank=False)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)
        return "{}".format(self.text)  

   
