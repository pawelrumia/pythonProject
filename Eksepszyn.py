class Eksepszyn:
    def podzielacz(self, x: float, dzielnik: float):
        try:
            result = x / dzielnik
            print(result)
            return result
        except ZeroDivisionError:
            print("Jestes pierdolonym debilem!")
