from slugify import slugify
from transliterate import translit

def generate_slug(title):
    transliterate_title = translit(title, 'ru', reversed=True)
    return slugify(transliterate_title)