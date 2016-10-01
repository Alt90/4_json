import json
import sys


def load_data(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    print(u'%s' % json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("File don`t enter. Please run script with argv.")
        sys.exit()
    data = load_data(sys.argv[1])
    pretty_print_json(data)
