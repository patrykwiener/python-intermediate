from object_oriented_programming.multiple_inheritance import Pracownik, Student


def sprawdz_finanse(obj):
    print(obj.pokaz_finanse())


if __name__ == '__main__':
    os1 = Pracownik('Jaroslaw', 50, 40, 168)
    os2 = Student('Adnrzej', 50, 600)

    sprawdz_finanse(os1)  # instancja klasy Pracownik
    sprawdz_finanse(os2)  # instancja klasy Student
