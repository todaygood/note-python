
## issue name 'include' is not defined

<stacktrace>
...
path('apppath/', include('myapp.urls')),
NameError: name 'include' is not defined


### solution:

from django.conf.urls import include


## issue: uwsgi 不支持windows 



## models.ForeignKey(
    'Categorie',
    on_delete=models.CASCADE,
)

https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete

