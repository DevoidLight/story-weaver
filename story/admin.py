from django.contrib import admin
from .models import Story, Chapter, Version, Collaboration, Scene

# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'create']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'chapter_number', 'story']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Version)
admin.site.register(Collaboration)
admin.site.register(Scene)