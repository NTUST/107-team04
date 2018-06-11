
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
class Category(models.Model):
    c_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

class Post(models.Model):
    p_id = models.AutoField(primary_key = True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    image_width=models.IntegerField(default=0)
    image_height=models.IntegerField(default=0)
    image = models.ImageField(null = True, blank=True, width_field="image_width", height_field="image_height",upload_to='static/images/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return  str(self.p_id) + "." + self.title

class Comment(models.Model):
    title = models.CharField(max_length =200)
    user_name = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.IntegerField(default=0)

    def __str__(self):
        return self.title




