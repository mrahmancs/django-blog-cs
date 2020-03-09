from django.db import models
from django.conf import settings

from django.db.models.signals import pre_save
from djblog.utils import unique_slug_generator
# from django.utils.text import slugify
# Create your models here.
user = settings.AUTH_USER_MODEL


class Post(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    author      = models.ForeignKey('Author', on_delete=models.CASCADE)
    image       = models.ImageField()
    slug        = models.SlugField(max_length=150, unique=True, null=True, blank=True) # try to use unique=True for instant solutions/////null=True, blank=True

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return f"blog/{self.slug}/"


# slug generator

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(slug_generator, sender=Post)





class Author(models.Model):
    user  = models.ForeignKey(user, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()


    def __str__(self):
        # full_name = f"{self.user.first_name} {self.user.last_name}"
        return self.user.first_name
    

    