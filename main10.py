from __future__ import annotations

def multiply_divider(x: int, y: int, z: int) -> float | None:
    try:
        return x / y / z
    except ZeroDivisionError:
        return None
    except TypeError:
        return -1

def multiply_divider2(x: int, y: int, z: int) -> float | None:
    try:
        return x / y / z
    except (ZeroDivisionError, TypeError):
        return None

def power_collector(*values: int) -> list[int]:
    result = []
    for value in values:
        try:
            result.append(2**value)
            print(f"Value: {value} passed.")
        except (ValueError, TypeError):
            print(f"Value: {value} created error.")
            break


    return result

if __name__ == '__main__':
    print(multiply_divider(1, 3, 4))
    print(multiply_divider(1, 3, 0))
    print(multiply_divider2(1, "12", 1))

    print(power_collector(1,2,3))
    print(power_collector(1))
    print(power_collector(1,2, "4", 5))