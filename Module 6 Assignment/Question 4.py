def add_html_tags(tag, text):
    return f"<{tag}>{text}</{tag}>"

print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
