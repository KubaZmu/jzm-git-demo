def add_two_numbers(num1, num2 = 9):
    return num1 + num2

# Na początku definiujemy argumenty wymagane (bez wartości domyślnej),
# a następnie argumenty z wartością domyślną.

def multiply_three_numbers(num1 = 10, num2 = 2, num3 = 5):
    return num1 * num2 * num3

def calculator(num1, num2, num3 = 0, num4 = 0):
    return num1 + num2 + num3 + num4

if __name__ == '__main__':
    # print(f"Bez argumentu num2: {add_two_numbers(11)}")
    # print(f"Z argumentem num2: {add_two_numbers(15, 75)}")
    print(f"Bez argumentów: {multiply_three_numbers()}")

    # Podaje jeden argument
    # Zapis pozycyjny: podajemy argumenty w kolejnosci
    # w jakiej sa podane w definicji
    print(f"1 argument: {multiply_three_numbers(3)}")
    print(f"2 argumenty: {multiply_three_numbers(2, 7)}")

    # Zapis z przypisaniem
    print(f"1 argument/przypisanie: {multiply_three_numbers(num3=100)}")
    print(f"2 argumenty/przypisania: {multiply_three_numbers(num3=15, num1=1)}")

    # Dobra praktyka
    # Najpierw argumenty wymagane (zapis pozycyjny), a nastepnie argumenty
    # z wartosciami domyslnymi (zapis z przypisaniem)
    print(
        calculator(1, 99, num4=-20)
    )