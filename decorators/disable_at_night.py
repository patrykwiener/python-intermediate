from datetime import datetime


def disable_at_night(func):
    # dekorator, który wywołuje udekorowaną funkcję tylko w ciągu dnia
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

    return wrapper


@disable_at_night
def say_something():
    print("Hello world")


if __name__ == '__main__':
    say_something()
