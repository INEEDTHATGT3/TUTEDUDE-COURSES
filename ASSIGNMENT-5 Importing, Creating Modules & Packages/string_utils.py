def capitalize_words(text):
    # i used .title() because it iterates through the string and capitalizes the first character of every word detected.
    return text.title()

def reverse_string(text):
    # i used slicing [::-1] because it is the most efficient, Python way to step through a string backwards.
    return text[::-1]

def word_count(text):
    # i used .split() because it automatically handles multiple spaces and returns a list of individual words.
    words = text.split()
    return len(words)