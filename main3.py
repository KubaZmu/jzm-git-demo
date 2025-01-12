if __name__ == '__main__':

    for i in range(0, 21, 2):
        print(i, end=" ")

    print("\n")

    for i in range(1,26):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{1} -> PIF PAF")
        elif i % 3 == 0:
            print(f"{i} -> PIF")
        elif i % 5 == 0:
            print(f"{i} -> PAF")
        else:
            print(f"{i} -> {i}")