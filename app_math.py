def menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Oblicz średnią")
        print("2. Potęgowanie liczb")
        print("3. Sprawdź rodzaj trójkąta")
        print("4. Porównanie dwóch liczb")
        print("0 lub quit. Zakończ program")

        wybor = input("Wybór: ")

        if wybor == '1':
            wylicz_srednia()
        elif wybor == '2':
            potegowanie()
        elif wybor == '3':
            rodzaj_trojkata()
        elif wybor == '4':
            porownanie_licz()
        elif wybor == '0':
            print("Zakończono program.")
            break
        elif wybor == 'quit':
            print("Zakończono program.")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


def wylicz_srednia():
    import re
    liczby = input("Podaj liczby oddzielone spacją lub przecinkiem lub średnikiem lubinnym białym znakiem: ")
    liczby_bez_bialych_znakow = re.split(r'[,\s;:]+', liczby)
    liczby_calkowite = []
    for liczba in liczby_bez_bialych_znakow:
        liczby_calkowite.append(float(liczba))
    srednia = round(float(sum(liczby_calkowite) / len(liczby_calkowite)), 2)
    print(f"Średnia wprowadzonych liczb to: {srednia:.2f} (wynik zaokrąglony do dwóch miejsc po przecinku)")


def potegowanie():
    podstawa = float(input("Podaj podstawę: "))
    potega = float(input("Podaj wykładnik: "))
    wynik = podstawa ** potega
    print(f"{podstawa} do potęgi {potega} wynosi: {wynik}")


def porownanie_licz():
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    if liczba1 > liczba2:
        print(f"{liczba1} jest większa od {liczba2}")
    elif liczba1 < liczba2:
        print(f"{liczba1} jest mniejsza od {liczba2}")
    else:
        print(f"{liczba1} jest równa {liczba2}")


def rodzaj_trojkata():
    bok1 = int(input("Podaj długość pierwszego boku: "))
    bok2 = int(input("Podaj długość drugiego boku: "))
    bok3 = int(input("Podaj gługość trzeciego boku: "))
    if bok1 == bok2 == bok3:
        print(f"trójkąt o bokach (X: {bok1}, Y: {bok2}, Z: {bok3}) jest równoboczny")
    elif bok1 != bok2 != bok3:
        print(f"trójkąt o bokach (X: {bok1}, Y: {bok2}, Z: {bok3}) jest różnoboczny")
    elif bok1 == bok2 or bok2 == bok3:
        print(f"trójkąt o bokach (X: {bok1}, Y: {bok2}, Z: {bok3}) jest równoramienny")


def main():
    print("Witaj w aplikacji matematycznej!")
    menu()


if __name__ == "__main__":
    main()