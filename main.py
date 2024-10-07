# ***********************************************
# Nazwa klasy: Film
# Pola:
#   _tytul - przechowuje tytuł filmu, ograniczony do 20 znaków
#   _liczba_wypozyczen - przechowuje liczbę wypożyczeń filmu
# Metody:
#   ustaw_tytul(tytul) - ustawia tytul filmu (maks. 20 znaków)
#   pobierz_tytul() - zwraca tytuł filmu
#   pobierz_liczba_wypozyczen() - zwraca liczbę wypożyczeń
#   zwieksz_liczbe_wypozyczen() - zwiększa liczbę wypożyczeń
#   wyswietl_informacje() - wyświetla tytuł oraz liczbę wypożyczalni, przechowując tytuł oraz liczbe wypożyczeń
# Informacje: klasa film reprezentuje film w systemie wypożyczalni, przechowując tytuł oraz liczbę wypożyczeń
# autor: Rafał Lietzau      
# ***********************************************
class film:
    def wyswietl_informacje(self):


if __name__ == "__main__":

    #Inicjalizacja obiektu film z domyślnymi wartościami
    film = film()

    #Wyświetalnie początkowych informacji o filmie
    print("Początkowe dane o filmu:")
    film.wyswietl_informacje()

    #Testowanie metody ustaw_tytul, ustawiając nowy tytuł
    print("\nUstawiamy nowy tytuł filmu 'Incepcja'")
    film.ustaw_tytul("Incepcja")
    print("\nPo ustawieniu tytułu:")
    film.wyswietl_informacje=()

    #Testowanie metody pobierz_tytul, pobierając tytuł filmu
    print("\nAktualny tytuł filmu:", film.pobierz_tytul())

    #Testowanie inkrementacji liczby wypożyczeń
    print("\nZwiększamy liczbę wypożyczeń dwukrotnie...")
    film.zwieksz_liczbe_wypozyczen()
    film.zwieksz_liczbe_wypozyczen()
    film.wyswietl_informacje()

    #Wyświetlanie finalnej liczby wypożyczeń
    print("\nOstateczna liczba wypożyczeń", film.pobierz_liczbe_wypozyczen())