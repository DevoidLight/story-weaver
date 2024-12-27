from django import forms
from .models import Story, Chapter


class CreateStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите название истории',
                'class': 'text_input', 
                'maxlength': '200'
                })
        }

class CreateChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'chapter_number']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите название истории',
                'class': 'text_input', 
                'maxlength': '200'
                }),
            'chapter_number': forms.NumberInput(attrs={
                'placeholder': 'Введите номер главы',
                'class': 'number_input',
                'min': '1'
                })
        }