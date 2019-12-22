# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from funcs import get_dict
import sqlite3


def entry_page(key):
    articles = get_dict()
    pos = "none"
    if key in [str(a['key']) for a in articles]:
        for i in range(len(articles)):
            if str(articles[i]['key']) == key:
                pos = i
                articles = articles[pos]
                break
        if request.method == 'POST':
            name = request.form.get('name')
            text = request.form.get('comment')
            if name and text:
                articles = get_dict()
                comment = articles[pos]["comments"]
                comment.append({"name": name, "text": text})
                articles[pos]["comments"] = comment
                conn = sqlite3.connect("mydatabase.db", uri=True)
                cursor = conn.cursor()
                comm = [(key, name, text)]
                cursor.executemany("INSERT INTO comments (key, name, text) values (?, ?, ?)", comm)
                conn.commit()
                return redirect('http://127.0.0.1:5000/entry/{}'.format(key))
    return render_template('entry.html', pos=pos, blog=articles)
