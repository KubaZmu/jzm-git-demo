def exec2(*values, operator = "dodawanie"):
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return values[0]

    result = values[0]
    try:
        if operator == "dodawanie":
            for value in values[1:]:
                result += value
        elif operator == "odejmowanie":
            for value in values[1:]:
                result -= value
        elif operator == "mnozenie":
            for value in values[1:]:
                result *= value
        elif operator == "dzielenie":
            for value in values[1:]:
                try:
                    result /= value
                except ZeroDivisionError:
                    continue
        else:
            return None
    except TypeError:
        exit(1)

    return result

def factorial(n):
    result = 1
    try:
        if n not in [0, 1]:
            for i in range(2, n + 1):
                result *= i
        return result
    except TypeError:
        return factorial(int(n))

if __name__ == '__main__':
    print(factorial("5"))