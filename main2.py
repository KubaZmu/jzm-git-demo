if __name__ == '__main__':

    address_book = {
        "user1": "11111111",
        "user2": "22222222",
        "user3": "33333333",
        "user4": "44444444"
    }
    print(address_book)

    address_book["user5"] = "55555555"
    print(address_book)

    address_book["user2"] = "2222"
    print(address_book)

    address_book.pop("user3")
    print(address_book)


    key = "user2"
    if key in address_book.keys():
        print(f"Klucz {key} istnieje w słowniku.")
    else:
        print(f"Klucz {key} nie istnieje w słowniku.")


    check_value = "44444444"
    for keys, values in address_book.items():
        if values == check_value:
            print(keys)