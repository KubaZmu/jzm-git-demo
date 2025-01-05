import re

def main():
    print("Witaj w aplikacji QuickMath!")
    menu()

def menu():
    while True:
        print("\nWybierz opcję:")
        print("1. Oblicz średnią.")
        print("2. Potęgowanie liczb.")
        print("3. Sprawdź rodzaj trójkąta.")
        print("4. Porównanie dwóch liczb.")
        print("0 lub quit. Zakończ program.")

        function_selection = input("Wybór: ")
        if function_selection == '1':
            number = input("Podaj liczby oddzielone spacją, przecinkiem, średnikiem lub innym białym znakiem: ")
            result = average(number)
            print(result)
        elif function_selection == '2':
            base = float(input("Podaj podstawę: "))
            power = float(input("Podaj wykładnik: "))
            result = exponentiation(base, power)
            print(f"{base} do potęgi {power} wynosi: {result}")
        elif function_selection == '3':
            side1 = float(input("Podaj długość pierwszego boku: "))
            side2 = float(input("Podaj długość drugiego boku: "))
            side3 = float(input("Podaj długość trzeciego boku: "))
            result = type_of_triangle(side1, side2, side3)
            print(result)
        elif function_selection == '4':
            number1 = float(input("Podaj pierwszą liczbę: "))
            number2 = float(input("Podaj drugą liczbę: "))
            result = comparison_of_numbers(number1, number2)
            print(result)
        elif function_selection == '0' or function_selection.lower() == 'quit':
            print("Zakończono program.")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")


def average(number: str) -> str:
    numbers_without_whitespace = re.split(r"[,\s;:]+", number)
    numbers_list= []
    for numbers in numbers_without_whitespace:
        numbers_list.append(float(numbers))
    average_score= round(float(sum(numbers_list) / len(numbers_list)), 2)
    return f"Średnia wprowadzonych liczb to: {average_score:.2f} (wynik zaokrąglony do dwóch miejsc po przecinku)."


def exponentiation(base: float, power: float) -> float:
    score = base ** power
    return score


def comparison_of_numbers(number1: float, number2: float) -> str:
    if number1 > number2:
        return f"{number1} jest większa od {number2}"
    elif number1 < number2:
        return f"{number1} jest mniejsza od {number2}"
    else:
        return f"{number1} jest równa {number2}"


def type_of_triangle(side1: float, side2: float, side3: float) -> str:
    if side1 == side2 == side3:
        return f"trójkąt o bokach (X: {side1}, Y: {side2}, Z: {side3}) jest równoboczny"
    elif side1 != side2 and side2 != side3 and side1 != side3:
        return f"trójkąt o bokach (X: {side1}, Y: {side2}, Z: {side3}) jest różnoboczny"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return f"trójkąt o bokach (X: {side1}, Y: {side2}, Z: {side3}) jest równoramienny"


if __name__ == "__main__":
    main()