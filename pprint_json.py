import json
import sys

from pprint import pprint


def load_data(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("File don`t enter. Please run script with argv.")
        sys.exit()
    data = load_data(sys.argv[1])
    pretty_print_json(data)
