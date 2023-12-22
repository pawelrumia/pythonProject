class Swicz:
    x: int

    def metodaSwicz(liczba: int):
        x = input("Wez wpisz numer")
        match x:
            case '1':
                print("Jedynka")
            case '2':
                print("Dwojeczka")
            case '_':
                print("Idz gdzie indziej")
