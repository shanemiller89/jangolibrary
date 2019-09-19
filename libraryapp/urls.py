from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', list_libraries, name='libraries'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
]