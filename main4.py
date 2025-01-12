def greetings(name):
    print(f"Hi, {name}!")

def fake_shoot(i):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{1} -> PIF PAF")
    elif i % 3 == 0:
        print(f"{i} -> PIF")
    elif i % 10 == 0:
        print(f"{i} -> BOOM")
    elif i % 5 == 0:
        print(f"{i} -> PAF")
    else:
        print(f"{i} -> {i}")

def switch_temp_unit(temp_value, unit):
    result = None
    if unit == "C":
        result = (temp_value - 32) * 5/9
    if unit == "F":
        result = (temp_value * 9/5) + 32
    return result

if __name__ == '__main__':
    greetings("Adam")
    greetings("Piotr")
    fake_shoot(100)
    print (switch_temp_unit(0, "F"))
    print(switch_temp_unit(50, "C"))