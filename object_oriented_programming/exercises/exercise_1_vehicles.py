"""
VEHICLES

1. Abstract classes
Naszym zadaniem przy uzyciu odpowiedniej abstracji napisanie kilku klas. Będziemy budować
hierarchię zależności kilku wybranych środków transportów, zarówno lądowych jak i wodnych.
1.1. class Vehicle:
    * klasa ABSTRAKCYJNA
    * posiada tylko jedną metodę abstrakcyjną get_current_speed
1.2 klasa LandVehicle:
    * dziedziczy po klasie Vehicle
    * jest również klasą abstrakcyjną
    * w konstruktorze przyjmuje parametr wheels_number, który zapisywany do ochronionego atrybutu
      _wheels_number
    * klasa posiada także abstrakcyjną metodę drive
1.3 klasa WaterVehicle:
    * dziedziczy po klasie Vehicle
    * jest również klasą abstrakcyjną
    * w konstruktorze przyjmuje parametry name oraz propulsion_type; zapisywane są one do
      chronionych atrybutów
    * posiada abstrakcyjną metodę swim
1.4 klasa Car:
    * dziedziczy po klasie LandVehicle;
    * NIE jest klasą abstrakcyjną!
    * implementuje odziedziczone metod; każda z metod powinna wyświetlać jakąś wiadomość;
      można sobie wybrać treść (nie jest to istotne)
1.5 klasa Ship:
    * dziedziczy po klasie WaterVehicle;
    * NIE jest klasą abstrakcyjną!
    * implementuje odziedziczone metod; każda z metod powinna wyświetlać jakąś wiadomość;
      można sobie wybrać treść (nie jest to istotne)

2. Multiple inheritence
Wyobraźmy sobie taką sytuację, że chcemy dodać amfibię. W jaki sposób rozwiążemy dziedziczenie?
Należy napisać klasę AmphibiousVehicle w taki sposób, aby ten pojazd mógł zarówno poruszać się po
lądzie jak i po wodzie. Zaimplementuj wszystkie odziedziczone metody. W konstruktorze wskaż w
jakiej kolejności powinny się wykonać konstruktory klas, po których dziedziczy.

"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_current_speed(self):
        pass


class LandVehicle(Vehicle, ABC):
    def __init__(self, wheels_number: int):
        super().__init__()
        self._wheels_number = wheels_number

    @abstractmethod
    def drive(self):
        pass


class WaterVehicle(Vehicle, ABC):
    def __init__(self, name: str, propulsion_type: str):
        super().__init__()
        self._name = name
        self._propulsion_type = propulsion_type

    @abstractmethod
    def swim(self):
        pass


class Car(LandVehicle):
    def drive(self):
        print('Driving...')

    def get_current_speed(self):
        print('50km/h')


class Ship(WaterVehicle):
    def swim(self):
        print('Swimming...')

    def get_current_speed(self):
        print('10mil/h')


if __name__ == '__main__':
    car = Car(wheels_number=4)
    ship = Ship(name='Nugat', propulsion_type='asd')
    car.get_current_speed()
    car.drive()
