def power_collector(*values: int) -> list[int]:
    result = []
    for value in values:
        result.append(2 ** value)

    return result


def fv_checker(txt: str) -> bool:
    if txt.count("FV") == 0:
        return False
    else:
        return True


def txt_mirror(txt: str) -> str:
    return txt[::-1]


if __name__ == '__main__':
    x: int = 10  # int
    y: float = 12.5  # float
    z: str = "TXT"  # str

    sample = power_collector(1, 5, 8, 10, 2)
    print(sample)