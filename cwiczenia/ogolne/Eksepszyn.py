class Eksepszyn:
    def divisor(self, x: float, dzielnik: float):
        try:
            result = x / dzielnik
            print(result)
            return result
        except ZeroDivisionError:
            print("Zero division")
