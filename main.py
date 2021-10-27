import math


# '''
# Problema 14 :  Calculează CMMMC al `n` numere date
# '''
def get_cmmmc(numbers):
     x = numbers[0]
     i = 1
     while i < len(numbers):
         y = numbers[i]
         a = x
         b = y
         while x != y:
             if x > y:
                 x -= y
             else:
                 y -= x
         m = a * b / x
         x = m
         i += 1
     return m


def test_get_cmmmc():
     n = [28, 147, 63, 7]
     assert (get_cmmmc(n) == 1766) is False
     m = [4, 6, 3, 9]
     assert (get_cmmmc(m) == 36) is True

# '''
# Problema 13 :  Transformă o temperatură dată într-o scară dată (`K`, `F` sau `C`) într-o altă scară dată. De exemplu: `300 K C` -> `26.85`.
# '''

def get_temp(temp: float, actual: str, to: str):
     if actual == "C" and to == "K" :
         return temp + 273.15
     elif actual == "K" and to == "C":
         return temp - 273.15
     elif actual == "C" and to == "F":
         return temp * 1.8 + 32
     elif actual == "F" and to == "C":
         return (temp - 32) / 1.8
     elif actual == "F" and to == "K":
         return 5/9 * ( temp + 459.67 )
     elif actual == "K" and to == "F":
         return (temp - 273.15) * 9/5 + 32
     else:
         return temp


def test_get_temp():
      assert(get_temp(30,"C", "K") == 303.15) is True
      assert(get_temp(30, "K", "C") == 20.15) is False


# '''
# Problema 10 :Calculează combinări de `n` luate câte `k` (`n` și `k` date)
# '''
def get_n_choose_k(n: int, k: int):
    x = math.comb(n, k)
    return x


def test_get_n_choose_k():
    assert(get_n_choose_k(10, 5) == 252) is True
    assert(get_n_choose_k(11, 6) == 134) is False
    assert(get_n_choose_k(4,2) == 6) is True


def printMenu():
    print("1.Calculează CMMMC al `n` numere date")
    print("2.Transformă o temperatură dată într-o scară dată (`K`, `F` sau `C`) într-o altă scară dată.")
    print("3. Calculează combinări de `n` luate câte `k` ( 'n' > 'k')")
    print("4.Inchide program")


def main():
     test_get_cmmmc()
     test_get_temp()
     test_get_n_choose_k()
     while True:
        printMenu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
             numbers = []
             s = int(input("Introdu lungimea sirului: "))
             for i in range(0, s):
                 x = int(input("Introduce-ti una dintre valori: "))
                 numbers.append(x)
             print(get_cmmmc(numbers))
        if optiune == "2":
             m = input("Introduce-ti scara actuala(K , C , F): ")
             n = input("Introduce-ti scara in care vreti sa transformati(K, C, F): ")
             p = int(float(input("Introduce-ti temperatura pe care doriti sa o transformati: ")))
             print(get_temp(p, m, n))
        if optiune == "3":
            n = int(input("Dati-l pe n: "))
            k = int(input("Dati-l pe k: "))
            print(get_n_choose_k(n ,k))

        elif optiune == "4":
             break


if __name__ == '__main__':
    main()