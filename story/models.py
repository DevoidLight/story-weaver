from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    genre = models.ManyToManyField(Genre, related_name='stories')
    author = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    chapter_number = models.IntegerField()
    story = models.ForeignKey(Story, related_name='chapters', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Version(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='versions', on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commit = models.TextField()


class Collaboration(models.Model):
    story = models.ForeignKey(Story, related_name='authors', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


