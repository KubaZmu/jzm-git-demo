def power_printer(*values):
    for value in values:
        print(f"2^{value} = {2**value};", end=" ")
    print()

def exec2(*values, operator = "dodawanie"):
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return values[0]

    print(operator)

    result = values[0]
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
            result /= value
    else:
        return None

    return result

if __name__ == '__main__':
    print(exec2())
    print(exec2(2))
    print(exec2(8, 10))
    print(exec2(10, 2, operator="odejmowanie"))
    print(exec2(10, 2, operator="mnozenie"))
    print(exec2(10, 2, operator="dzielenie"))