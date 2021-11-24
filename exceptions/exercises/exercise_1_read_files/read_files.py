"""
READ FILES

Naszym zadaniem jest napisanie dwóch funkcji.
1. read_file(file_path) - odczytyje zawartość wskazanego pliku
2. read_files(file_paths) - odczytuje zawartość wielu plików i zwraca je w postaci listy list

Pliki znajdują się w folderze <project-root>/exceptions/exercises/assets.

-- budowa ścieżek ---
Do budowy ścieżek posłużyć się funkcjami z modułu 'os', który należy zaimportować.
* os.path.dirname(sciezka_do_pliku) - zwraca ścieżkę do folderu w którym znajduje się wskazany plik
* os.path.dirname(__file__) - zwraca ścieżkę do folderu, w którym znajduje się plik, w którym
  jest użyta funkcja
* os.path.join(*paths) - zwraca złączoną ścieżke w danym systemie operacyjnym

--- read_file ---
* jako parametr przyjmuje ścieżke do pliku, którego ma odczytać w trybie odczyty ('r')
* plik należy otworzyć i następnie użyć na pliku metody readlines(), która pobiera wszystkie linie z pliku
* odczytaną wartość należy zwrócić
** waszym obowiązkiem jest przedebugować wywołanie, aby upenić się w jaki formacie są zwracane dane
** należy pamiętać, aby zamknąć plik ZAWSZE!


--- read_files ---
* korzysta z wcześniej napisanej funkcji read_file
* jako parametr przyjmuje listę ścieżek wskazujących na pliki, które należy odczytać
* zwraca listę list zawierającą dane z plików
** obsłużyć przypadek gdy dany plik nie istnieje (FileNotFoundError zostanie rzucony przed read_file).
   Należy wtedy uznać, że zawawrtość nieistniejącego pliku jest równa pustej liście.
"""


def read_file(file_path):
    pass


def read_files(file_paths):
    pass
