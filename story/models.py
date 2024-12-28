from django.db import models
from django.contrib.auth.models import User
from .utils import generate_slug


class Story(models.Model):
    class Status(models.TextChoices):
        PRIVATE = 'PR', 'Private'
        PUBLIC = 'PU', 'Public'

    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True, unique=True)
    desctiption = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PUBLIC)
    author = models.ForeignKey(User, related_name='stories', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    chapter_number = models.IntegerField(unique=True)
    story = models.ForeignKey(Story, related_name='chapters', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

class Scene(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    scene_number = models.IntegerField(unique=True)
    chapter = models.ForeignKey(Chapter, related_name='scenes', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

class Version(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='versions', on_delete=models.CASCADE)
    text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commit = models.TextField()


class Collaboration(models.Model):
    story = models.ForeignKey(Story, related_name='authors', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


