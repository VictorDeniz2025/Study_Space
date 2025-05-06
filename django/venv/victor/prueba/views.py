from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def show_tables(request):
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    tables_list = "<br>".join([table[0] for table in tables])
    return HttpResponse(f"<h1>Tablas en la base de datos:</h1><p>{tables_list}</p>")
