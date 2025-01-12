# 1
def change_currency(amount, currency):
    curr_values = {
        "EUR": 4.35,
        "USD": 3.5,
        "GBP": 5.5
    }

    if currency in curr_values.keys():
        return float(amount) / curr_values[currency]
    else:
        return None

# 2
def bmi_calculator(weight, height):
    BMI = weight / height ** 2

    if BMI < 18.5:
        return "Niedowaga"
    elif BMI < 25:
        return "Prawidłowa waga"
    elif BMI < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

# 3
def harmony_sequence(n):
    result = 0
    for i in range(1, n + 1):
        result += 1/i

    return result

# 4
def factorial(n):
    result = 1
    if n not in [0, 1]:
        for i in range(2, n + 1):
            result *= i

    return result

# 5
def only_even(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i)

    return result

if __name__ == '__main__':
    print(change_currency(550.0, "GBP"))
    print(change_currency(1000.0, "EUR"))

    print(bmi_calculator(80, 2.0))
    print(harmony_sequence(2))
    print(factorial(5))
    print(only_even([1, 2, 8, 11, 5, 6]))