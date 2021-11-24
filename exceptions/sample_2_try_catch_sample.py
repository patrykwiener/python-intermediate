def dummy_func():
    a = 3
    b = [1, 0, 2]
    for elem in b:
        try:
            wynik = a / elem
        except ZeroDivisionError:
            continue
        print(f"Wynik to: {wynik}")


if __name__ == '__main__':
    dummy_func()
