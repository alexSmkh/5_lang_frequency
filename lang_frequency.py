import sys
import os
import re
import collections


def load_data(file_name):
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r"\w+", text.lower())
    return collections.Counter(words).most_common(10)


def get_text_file_name():
    name = sys.argv[1]
    return name


def print_most_frequent_words(list_of_words):
    for word, num in list_of_words:
        print(word, num)


if __name__ == '__main__':
    text_file = get_text_file_name()
    text_from_file = load_data(text_file)
    most_frequent_words = get_most_frequent_words(text_from_file)
    print_most_frequent_words(most_frequent_words)
