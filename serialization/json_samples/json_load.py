import json

from serialization.consts import JSON_FILE

if __name__ == '__main__':
    with open(JSON_FILE) as in_file:
        data = json.load(in_file)

    for obj in data:
        print(obj)
        print(obj['imie'])
