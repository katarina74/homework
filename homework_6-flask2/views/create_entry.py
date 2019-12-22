# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
import random
import datetime
from funcs import get_dict
import sqlite3


def create_entry_page():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        if title and text:
            articles = get_dict()
            key = random.randint(len(articles)+1, len(articles)+10)
            conn = sqlite3.connect("mydatabase.db", uri=True)
            cursor = conn.cursor()
            article = [(key, title, text, str(datetime.datetime.now()))]
            cursor.executemany("INSERT INTO articles (key, title, text, created_at) values (?, ?, ?, ?)", article)
            conn.commit()
            return redirect('http://127.0.0.1:5000/entry/{}'.format(key))
    return render_template('create_entry.html')
