from django.shortcuts import render, redirect
from .models import Story, Chapter
from .forms import *

# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def story_list(request):
    stories = Story.objects.all()
    if request.method == 'POST':
        form = CreateStoryForm(request.POST)
        if form.is_valid():
            new_story = form.save(commit=False)
            new_story.author = request.user
            new_story.save()
            return redirect('story_list')
    else:
        form = CreateStoryForm()
    return render(request, 'story/story_list.html', {'stories': stories, 'form': form})

def chapter_list(request, title):
    story = Story.objects.get(slug=title)
    chapters = Chapter.objects.filter(story=story)
    if request.method == 'POST':
        form = CreateChapterForm(request.POST)
        if form.is_valid():
            new_chapter = form.save(commit=False)
            new_chapter.story = story
            new_chapter.save()
            return redirect('chapter_list', title)
    else:
        form = CreateChapterForm()
    return render(request, 'story/chapter_list.html', {'chapters': chapters,
                                                       'slug': story.slug,
                                                       'form': form})


def chapter(request, title, chapter_number):
    story = Story.objects.get(slug=title)
    chapters = Chapter.objects.filter(story=story)
    chapter = Chapter.objects.get(story=story, chapter_number=chapter_number)
    chapter_index = next((index for index, chap in enumerate(chapters) if chap.chapter_number == chapter_number), None)    
    previous_chapter = chapters[chapter_index - 1] if chapter_index > 0 else None
    next_chapter = chapters[chapter_index + 1] if chapter_index < len(chapters) - 1 else None
    scene = Scene.objects.filter(chapter=chapter)
    if request.method == 'POST':
        form = CreateSceneForm(request.POST)
        if form.is_valid():
            new_scene = form.save(commit=False)
            new_scene.chapter = chapter
            new_scene.save()
            return redirect('chapter', title, chapter_number)
    else:
        form = CreateSceneForm()
    return render(request, 'story/chapter.html', {'chapter': chapter,
                                                  'chapters': chapters,
                                                  'slug': story.slug,
                                                  'previous_chapter': previous_chapter.chapter_number if previous_chapter else None,
                                                  'next_chapter': next_chapter.chapter_number if next_chapter else None,
                                                  'form': form,
                                                  'scene': scene})
