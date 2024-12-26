from django.shortcuts import render
from .models import Story, Chapter

# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def story_list(request):
    story = Story.objects.all()
    return render(request, 'story/story_list.html', {'stories': story})

def chapter_list(request, story_id):
    story = Story.objects.get(id=story_id)
    chapters = Chapter.objects.filter(story=story)
    return render(request, 'story/chapter_list.html', {'chapters': chapters,
                                                       'slug': story.slug})


def chapter(request, title, chapter_number):
    story = Story.objects.get(slug=title)
    chapters = Chapter.objects.filter(story=story)
    chapter = Chapter.objects.get(story=story, chapter_number=chapter_number)
    chapter_index = next((index for index, chap in enumerate(chapters) if chap.chapter_number == chapter_number), None)    
    previous_chapter = chapters[chapter_index - 1] if chapter_index > 0 else None
    next_chapter = chapters[chapter_index + 1] if chapter_index < len(chapters) - 1 else None
    return render(request, 'story/chapter.html', {'chapter': chapter,
                                                  'chapters': chapters,
                                                  'slug': story.slug,
                                                  'previous_chapter': previous_chapter.chapter_number if previous_chapter else chapter_number,
                                                  'next_chapter': next_chapter.chapter_number if next_chapter else chapter_number,})
