from functools import reduce

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]
    squared = [item ** 2 for item in items]

    odds = list(filter(lambda x: x % 2 == 1, items))  # [1, 3, 5]
    odds = [item for item in items if item % 2 == 1]

    print(sum(items))

    my_sum = 0
    for item in items:
        my_sum = my_sum + item


    # items_sum = reduce(lambda total, item: total + item, items)  # 15
    items_sum = reduce(lambda total, item: total + item, items, 0)  # 15

    # co jest pythonowym odpowiednikiem map?
    # co jest pythonowym odpowiednikiem filter?
