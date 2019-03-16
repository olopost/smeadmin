# SME Admin
Wagtail extension for add bunch of tools

## Capture
![capture](doc/django_view.png)

## installation
add the following line to your requirements.txt file :
````
git+https://github.com/olopost/smeadmin.git
````

after that add *smeadmin* to INSTALLED_APPS section of your wagtail settings:
````
INSTALLED_APPS = [
    'home',
    'smeadmin',
    'corbeille',
    'search',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block', # ajout support des tableaux
    'wagtail.core',
    'wagtail.admin',
    'modelcluster',
    'wagtail.contrib.styleguide',
    'taggit',
    'wagtail.contrib.postgres_search',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]
````

## Tools
At this hour, smeadmin provide some tool to create and print physical mail

1. First in the menu is Carnet d'Adresse
This tool manage identity and postal address of sender and recipient
 -![address book](doc/addressbook.png)
 2. Second in the menu is enveloppe tool
 this provide an interface to create pdf for DL format envelop
 ![generate_env](doc/generate_env.png)
 ![enveloppe](doc/enveloppe.png)
 3. Third is letter generation
 That generate letter french format
 ![letter](doc/lettre.png)
 

good usage
