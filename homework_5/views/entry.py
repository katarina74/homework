# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
import json


def entry_page(key):
    from storage import BLOG_ENTRIES
    articles = BLOG_ENTRIES
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
                from storage import BLOG_ENTRIES
                articles = BLOG_ENTRIES
                comment = articles[pos]["comments"]
                comment.append({"name": name, "text": text})
                articles[pos]["comments"] = comment
                with open("storage.py", 'w') as output_file:
                    output_file.write("import datetime\nBLOG_ENTRIES = "+json.dumps(articles))
                return redirect('http://127.0.0.1:5000/entry/{}'.format(key))
    return render_template('entry.html', pos=pos, blog=articles)

