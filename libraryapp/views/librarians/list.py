import sqlite3
from django.shortcuts import render
from libraryapp.models import Librarian
from ..connection import Connection


def librarian_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                a.first_name,
                a.last_name      
            from libraryapp_librarian l
            join auth_user a on a.id = l.user_id
            """)

            all_librarians = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                librarian = Librarian()
                librarian.id = row['id']
                librarian.first_name = row['first_name']
                librarian.last_name = row['last_name']

                all_librarians.append(librarian)

        template = 'librarians/list.html'
        context = {
            'all_librarians': all_librarians
        }

        return render(request, template, context)