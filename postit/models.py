from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown import *


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_to_location(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post.This method is important because the model is defined below.
    Then a queryset ordered by the "id"s of each object is created, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Post(models.Model):
    """This class represents the postit model."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    slug = models.SlugField(max_length=50, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False, unique=True)
    content = models.TextField(max_length=255, blank=False)
    publish = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=False)
    read_time =  models.IntegerField(default=0)  #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse("posts-api:detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["-timestamp", "-updated"]

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = create_slug(instance)

        if instance.content:
            html_string = instance.get_markdown()
           
pre_save.connect(pre_save_post_receiver, sender=Post)        
        
    




   
