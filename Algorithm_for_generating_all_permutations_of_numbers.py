# Генерация всех перестановок n чисел в m позициях

def generate_permutations(n, m = 'default', prefix=None):
    m = n if m == 'default' else m                              # По умолчанию m чисел = n позиций, но можно изменить m на нужное.
    prefix = prefix or []                                       # ( Логично что должно быть n >= m )
    if m == 0:
        print(*prefix)                                          # Вставляет prefix[0], prefix[1], prefix[2] ... prefix[n]
        return
    for number in range(1, n+1):
        if number in prefix:                                    # Чтобы избежать повторов цифр в числе типо 112 222 и тд    
            continue
        prefix.append(number)
        generate_permutations(n, m-1, prefix)
        prefix.pop()

generate_permutations(3)