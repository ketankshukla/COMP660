#### Question 4 - Write a Python function to create the HTML string with tags around the word(s).

```python
def add_html_tags(tag, text):
    return f"<{tag}>{text}</{tag}>"


print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
```

- The function `add_html_tags` takes two arguments: `tag` (the HTML tag) and
  `text` (the content to wrap in the tag).
- It returns a string formatted as an HTML element, using Python's f-string
  to dynamically insert the tag and text.
- The function wraps the text with the specified opening and closing tags.

### Output:

```html
<h1>My First Page</h1>
<p>This is my first page.</p>
<h2>A secondary header.</h2>
<p>Some more text.</p>
```

You can run the above code in Question 4.py file
