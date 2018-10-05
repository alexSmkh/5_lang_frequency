import sys
import os
import re
import collections


def load_data(file_name):
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, count_of_words):
    words = re.findall(r'\w+', text.lower())
    return collections.Counter(words).most_common(count_of_words)


def get_text_file_name():
    try:
        file_name = sys.argv[1]
        return file_name
    except IndexError:
        return None


def print_most_frequent_words(list_of_words):
    for word, count in list_of_words:
        print(word, '-', count)


if __name__ == '__main__':
    text_file_name = get_text_file_name()
    if text_file_name is not None:
        text_from_file = load_data(text_file_name)
        if text_from_file is not None:
            count_of_popular_words = 10
            most_frequent_words = get_most_frequent_words(
                text_from_file,
                count_of_popular_words
            )
            print_most_frequent_words(most_frequent_words)
