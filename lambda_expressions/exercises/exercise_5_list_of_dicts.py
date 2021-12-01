"""
LIST OF DICTS

Naszym zadaniem jest przeprowadzenie szeregu dzialań na liście dictow:
* sorted - posortowanie listy dictow rosnaco po atrybucie 'priority'
* min - wyciagniecie obiektu z listy dictow o minimalnej wartosc 'priority'
* max - wyciagniecie obiektu z listy dictow o maksymalnej wartosc 'priority'
"""
if __name__ == '__main__':
    dicts = [
        {
            'id': 3,
            'priority': 4,
        },
        {
            'id': 4,
            'priority': 5,
        },
        {
            'id': 5,
            'priority': 3,
        },
        {
            'id': 6,
            'priority': 1,
        }
    ]

    sorted_dicts = sorted(...)
    print(sorted_dicts)

    minimum = min(...)
    assert minimum == {'id': 6, 'priority': 1}

    minimum = max(...)
    assert minimum == {'id': 4, 'priority': 5}
