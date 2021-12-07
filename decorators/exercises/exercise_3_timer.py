"""
TIMER

Naszym zadaniem jest napisanie dekoratora zliczającego czas działąnia udekorowanej funkcji.
Dekorator musi byc uniwersalny, aby mozna go bylo uzyc z dowolna funkcja, dlatego powinnismy
pozwolic na dostarczenie do funkcji dowolnych parametrow (*args, **kwargs). Dekorator przed
wykonaniem funkcji zapisuje aktualny czas oraz zaraz po (time.time()). Po czym wyswietla czas jaki
uplynal w czasie wykonania funkcji w następującym formacie:
                    Function <function_name> execution took: <time>
* <function_name> - do nazwy funkcji mozna sie dobrac w nastepujacy sposob: func.__name__
* <time> - czas ktory uplynal

Pamietajmy takze ze udekorowana funkcja nadal musi miec mozliwosc zwracania wartości!
"""
import time


def timer(func):
    pass


@timer
def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(fibonacci(10))
    print(fibonacci(1000000))