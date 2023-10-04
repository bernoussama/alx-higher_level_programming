#!/usr/bin/python3

"""
This is the "" module , Example

>>> text_indentation("test?test.test:")
test?
<BLANKLINE>
test.
<BLANKLINE>
test:
<BLANKLINE>
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ["?", ".", ":"]:
            result += "\n\n"
    print(result, end="")
