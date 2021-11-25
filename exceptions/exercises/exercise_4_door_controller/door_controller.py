"""
DOOR CONTROLLER - cz. 1

Wyobraźmy sobie, że piszemy sterownik do kontroli drzwi. Drzwi mogą się otwierać, zamykać.

Specyfikacja:
*   Tworząc obiekt domyślnie stan drzwi (atrybut prywatny '_is_opened') oraz stan rygla ('_is_locked') są równy False
*   W konstruktorze podajemy takze kod otwierający/odryglowujący nasze drzwi. Jest on zapisywany do atrybutu self._unlock_code
*   Metoda 'is_door_opened' pozwalającą sprawdzić aktualny stan drzwi (czy są otwarte czy zamknięte). Zwraca wartość
    boolowską (True lub False)
*   Metoda 'open' otwiera drzwi poprzez odpowiednie ustawienie atrybutu '_is_opened'.
    Drzwi mogą się otworzyć tylko wtedy gdy nie są zaryglowane. Jezeli drzwi zaryglowane rzucany jest wyjątek DoorLockedError.
*   Metoda 'close' zamyka drzwi analogicznie poprzez odpowiednie ustawienie atrybutu '_is_opened'
*   Metoda 'is_door_locked' pozwala sprawdzic czy drzwi są zaryglowane
*   Metoda 'lock' rygluje nam drzwi
*   Metoda 'unlock' odryglowuje nam drzwi, ale tylko w przypadku gdy podamy odpowiedni kod otwarcia.
    W momencie gdy kod jest niepoprawny rzucany jest wyjątek UnlockCodeError, ktory nalezy samemu stworzyć
"""
DoorLockedError
UnlockCodeError

class DoorController:

    def __init__(self, unlock_code):
        pass

    def is_door_open(self):
        pass

    def is_door_locked(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def lock(self):
        pass

    def unlock(self, code):
        pass
