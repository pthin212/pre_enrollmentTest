import json
from collections import Counter
from functools import partial

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def count_words(input_string):
    word_counts = Counter(input_string.split())

    start = 1
    end = 100
    filenames = list(map(lambda i: f'result{i}.json', range(start, end)))

    save_functions = list(map(lambda filename: partial(save_json, filename, word_counts), filenames))
    list(map(lambda func: func(), save_functions))

    return dict(word_counts)

if __name__ == "__main__":
    input_string = input("Input: ")
    word_counts = count_words(input_string)
    print(word_counts)