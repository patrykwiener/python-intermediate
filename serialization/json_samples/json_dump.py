import json

from serialization.consts import JSON_FILE

kursanci = [
    {
        'imie': "Adam",
        'nazwisko': "Kowalski",
        'liczba punktow': 20
    },
    {
        'imie': "Janusz",
        'nazwisko': "Smuga",
        'liczba punktow': 17
    }
]

if __name__ == '__main__':
    with open(JSON_FILE, 'w') as out_file:
        json.dump(kursanci, out_file, indent=2)
