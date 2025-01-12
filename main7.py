# *args - krotka
def number_printer(*numbers):
    print(numbers)

def sumator(*numbers):
    result = 0
    for n in numbers:
        result += n

    return result

# **kwargs - slownik
def config_parser(**config):
    for key, value in config.items():
        print(key, value)

if __name__ == '__main__':
    number_printer(1, 2, 3)
    number_printer(1, 2, 3, 4)
    number_printer(2)
    print(sumator(1, 2, 3))
    print(sumator(1, 2, 3, 4))
    print(sumator(100))
    config_parser()
    config_parser(version=1.0, channel="stable", released=True, author="piotr")