# Генерация всех чисел, где n - основание системы счисления, m - длина числа.


def generate_numbers(n, m, prefix=None):
	prefix = prefix or []
	if m == 0:
		print(prefix)
		return
	for digit in range(n):
		prefix.append(digit)
		generate_numbers(n, m-1, prefix)
		prefix.pop()

generate_numbers(4, 3)