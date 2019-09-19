from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^librarians$', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    url(r'^libraries$', list_libraries, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
]