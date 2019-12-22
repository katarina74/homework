# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
import random
import datetime
import json


def create_entry_page():
    if request.method == 'POST':
        title = request.form.get('title')
        text = request.form.get('text')
        if title and text:
            from storage import BLOG_ENTRIES
            articles = BLOG_ENTRIES
            key = random.randint(len(BLOG_ENTRIES), len(BLOG_ENTRIES)+10)
            articles.append({
                'key': key,
                'title': title,
                'text': text,
                'created_at': str(datetime.datetime.now()),
                'comments': []
            })
            with open("storage.py", 'w') as output_file:
                output_file.write("import datetime\nBLOG_ENTRIES = "+json.dumps(articles))
            return redirect('http://127.0.0.1:5000/entry/{}'.format(key))
    return render_template('create_entry.html')

