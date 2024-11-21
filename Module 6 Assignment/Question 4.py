"""
HTML Tag Generator Module

This module provides functionality to wrap text content with HTML tags.
It demonstrates string formatting and basic HTML generation in Python.

Author: [Your Name]
Date: [Current Date]
"""

def add_html_tags(tag, text):
    """
    Wrap the given text with HTML opening and closing tags.

    Args:
        tag (str): The HTML tag to use (e.g., 'h1', 'p', 'div')
        text (str): The text content to wrap with HTML tags

    Returns:
        str: The text wrapped with the specified HTML tags

    Example:
        >>> add_html_tags('h1', 'Hello')
        '<h1>Hello</h1>'
    """
    return f"<{tag}>{text}</{tag}>"

# Example usage with different HTML tags and content
print(add_html_tags('h1', 'My First Page'))
print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
