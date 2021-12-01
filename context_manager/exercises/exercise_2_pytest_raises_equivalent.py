"""
PYTEST RAISES EQUIVALENT

Naszym zadaniem jest napisanie context managera imitującego zachowanie funkcji pytest.raises.
* W konstruktorze przyjmowane są 2 parametry: exception_type oraz opcjonalny match domyślnie None
* atrybut _exception_type - przyjmuje w konstruktorze typ wyjątki, który powinien wystąpić
* atrybut _match - oczekiwana wiadomość zawarta w wyjątku, na podstawie tej wartości będziemy
  sprawdzać czy wyjątek mial msg taki jak oczekiwany
* chcemy obsłuzyć przypadek gdy wyjątek nie wystąpi, wtedy AssertionError
* chcemy obsłużyc przypadek gdy wwyjątek który wystąpił nie jest wyjątkiem ktorego oczekiwaliśmy, wtedy AssertionError
* chcemy obsłużyć sytuacje gdy oczekiwana wiadomość nie jest równa rzeczywistej ktora przyszla z wyjatkiem.
  Oczywiscie pamietamy ze match jest opcjonalne, wiec gdy jest rowne None to nie sprawdzamy czy wiadomości się zgadzaja.
  W razie wystapienia niezgodności to AssertionError.

* TIP: aby w __exit__() na koniec wykonania metody nie byl rzucany wyjątek należy na samym końcu
       metody zwrócić True

"""


class PytestRaisesEquivalent:

    def __init__(self, exception_type, match=None):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    with PytestRaisesEquivalent(NotImplementedError, match='test msg'):
        raise NotImplementedError('test msg')

