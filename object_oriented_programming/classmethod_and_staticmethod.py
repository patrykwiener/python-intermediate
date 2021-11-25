from object_oriented_programming.multiple_inheritance import Osoba


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        if self.czy_imie_poprawne(imie):
            Osoba.__init__(self, imie, wiek)
            # or better super()
            # super().__init__(imie, wiek)
            self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium

    @classmethod
    def stworz_ze_stringa(cls, napis):
        imie, wiek, stypendium = napis.split()
        wiek, stypendium = int(wiek), float(stypendium)
        if cls.czy_imie_poprawne(imie):
            return cls(imie, wiek, stypendium)

    @staticmethod
    def czy_imie_poprawne(imie):
        if imie[0].isupper() and len(imie) > 3:
            return True
        return False


if __name__ == '__main__':
    stud1 = Student("Małgorzata", 32, 0)
    stud2 = Student.stworz_ze_stringa("Maciej 21 600")
    print(stud1)
    print(stud2)
    print(Student.czy_imie_poprawne("ala"))
