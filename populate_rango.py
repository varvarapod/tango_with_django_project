import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # First,we willcreatelists of dictionariescontainingthepages
    # we wanttoaddintoeach category.
    # Then wewill createadictionaryof dictionariesforourcategories.
    # This mightseem alittle bitconfusing,butitallowsustoiterate
    # througheach datastructure,andaddthedatatoourmodels.

    python_pages = [
        {'title': 'OfficialPython Tutorial',
         'url': 'http://docs.python.org/3/tutorial/'},
        {'title': 'HowtoThinklike aComputerScientist',
         'url': 'http://www.greenteapress.com/thinkpython/'},
        {'title': 'LearnPythonin10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/'}]

    django_pages = [
        {'title': 'OfficialDjangoTutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title': 'DjangoRocks',
         'url': 'http://www.djangorocks.com/'},
        {'title': 'HowtoTangowith Django',
         'url': 'http://www.tangowithdjango.com/'}]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/'},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org'}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'OtherFrameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}

    # If youwanttoaddmorecategories orpages,
    # addthem tothe dictionariesabove.

    # Thecode belowgoesthrough the catsdictionary,thenaddseachcategory,
    # andthen adds alltheassociatedpagesforthatcategory.
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # Print out the categories we haveadded.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}:{p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
