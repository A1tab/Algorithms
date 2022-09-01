# Алгоритм перевода числа из 10чной системы счисления в любую от 2 до 9

def transfer(x, base):
    num = ''
    while x > 0:
        num += str(x % base)  # строка num + инт x % base -> строка + str(x % base)
        x //= base
    print(num[::-1])          # строку нужно перевернуть

a = 1182

transfer(a, 9)
