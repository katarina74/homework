# -*- coding: utf-8 -*-
from flask import render_template, request, redirect
from funcs import get_dict


def sort_by_name(dct):
    return dct["title"]


def sort_by_date(dct):
    return dct["created_at"]


def index_page():
    articles = get_dict()
    lst_num_comm = []
    for blog in articles:
        lst_num_comm.append(len(blog['comments']))

    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            for a in articles:
                if a['title'] == text:
                    key = a['key']
                    return redirect('http://127.0.0.1:5000/entry/{}'.format(key))
            return redirect('http://127.0.0.1:5000/entry/статья не найдена')
        else:
            select1 = request.form.get('sort1')
            select2 = request.form.get('sort2')
            if select1 == "date":
                articles.sort(key=sort_by_date)
            else:
                articles.sort(key=sort_by_name)
            if select2 == "down":
                articles.reverse()
            return render_template('index.html', blog=articles, lst_num_comm=lst_num_comm,
                                   num_of_blog=len(articles))

    return render_template('index.html', blog=articles, lst_num_comm=lst_num_comm, num_of_blog=len(articles))
