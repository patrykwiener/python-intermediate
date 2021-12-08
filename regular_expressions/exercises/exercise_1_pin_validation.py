"""
PIN VALIDATION

Naszym zadaniem jest napisanie funkcji korzystajacej z wyrazenia regularnego, ktora podda walidacji
PIN przyjmowany w parametrze.
* pin powinien miec dokladnie 4 znaki
* pin sklada sie tylko z cyfr
* jezeli przychodzacy pin nie jest w oczekiwanym formacie, to rzucamy wlasnorecznie zdefiniowany
  wyjatek InvalidPinFormatError
"""

import re

import pytest


def validate_pin_registration(pin):
    pass


if __name__ == '__main__':
    with pytest.raises(InvalidPinFormatError):
        validate_pin_registration('abcd')

    with pytest.raises(InvalidPinFormatError):
        validate_pin_registration('12345')

    with pytest.raises(InvalidPinFormatError):
        validate_pin_registration('123')

    try:
        validate_pin_registration('1234')
    except InvalidPinFormatError:
        raise AssertionError()
