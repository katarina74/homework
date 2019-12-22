import sqlite3


def get_dict():
    articles = []
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    comments = {}
    for row in cursor.execute("SELECT * FROM comments"):
        if row[0] in comments:
            comments[row[0]].append({"name": row[1], "text": row[2]})
        else:
            comments[row[0]] = [{"name": row[1], "text": row[2]}]

    for row in cursor.execute("SELECT * FROM articles"):
        if row[0] in comments:
            articles.append({"key": row[0], "title": row[1], "text": row[2], "created_at": row[3],
                             "comments": comments[row[0]]})
        else:
            articles.append({"key": row[0], "title": row[1], "text": row[2], "created_at": row[3],
                             "comments": []})
    return articles

