from HW1 import post_collection

def add(title, author, content):
    new_post = {
        "title": title,
        "author": author,
        "content": content,
    }
    post_collection.insert_one(new_post)
    return new_post

add('Pro + Noob = Max', 'Max', 'Love is like a paper')