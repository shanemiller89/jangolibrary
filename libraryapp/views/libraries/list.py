import sqlite3
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection

@login_required
def list_libraries(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                li.id,
                li.title,
                li.address
            from libraryapp_library li
            """)

            all_libraries = db_cursor.fetchall()

        template_name = 'libraries/list.html'
        return render(request, template_name, {'all_libraries': all_libraries})


    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
                title, address
            )
            VALUES (?, ?)
            """,
            (form_data['location_name'], form_data['address']))

        return redirect(reverse('libraryapp:libraries'))