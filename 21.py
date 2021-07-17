M = ['-' for i in range(1, 10)]  # Создаем поле для игры


def playing_field():   # Функция для красивого поля
    print('   ', 'x', 'y', 'z')
    print('    -----')
    print('x', '|', *M[6:9])
    print('y', '|', *M[3:6])
    print('z', '|', *M[0:3])

playing_field()

while True:  # Цикл для игры
    print('ходит игрок 1')
    a = input('Введите число от 1 до 9 : ')
    if a not in [str(i) for i in range(1, 10)]:  # Проверка, что ввели цифру от 1 до 9
        while a not in [str(i) for i in range(1, 10)]:
            print('Вы ввели не то')
            a = input('Введите число от 1 до 9 : ')

    if 'x' not in M[int(a) - 1] and '0' not in M[int(a) - 1]:  # Проверка, что поле не занято
        M[int(a) - 1] = 'x'
    else:
        while True:
            print('занято')
            a = input('Введите число от 1 до 9 : ')
            if a not in [str(i) for i in range(1, 10)]:
                print('Вы ввели не то')
                continue
            if 'x' not in M[int(a) - 1] and '0' not in M[int(a) - 1]:
                M[int(a) - 1] = 'x'
                break
    # Проверка выигрышных комбинаций
    if ('x' in M[0] and 'x' in M[1] and 'x' in M[2]) or ('x' in M[3] and 'x' in M[4] and 'x' in M[5]) or (
            'x' in M[6] and 'x' in M[7] and 'x' in M[8]) or ('x' in M[0] and 'x' in M[3] and 'x' in M[6]) or (
            'x' in M[1] and 'x' in M[4] and 'x' in M[7]) or ('x' in M[2] and 'x' in M[5] and 'x' in M[8]) or (
            'x' in M[0] and 'x' in M[4] and 'x' in M[8]) or ('x' in M[2] and 'x' in M[4] and 'x' in M[6]):
        playing_field()
        print('Победил игрок 1!')
        break
    playing_field()

    if '-' not in M:    # Проверка варианта 'Ничья'
        print('Ничья')
        break

    print('ходит игрок 2')
    b = input('Введите число от 1 до 9 : ')
    if b not in [str(i) for i in range(1, 10)]:  # Проверка, что ввели цифру от 1 до 9
        while b not in [str(i) for i in range(1, 10)]:
            print('Вы ввели не то')
            b = input('Введите число от 1 до 9 : ')
    if 'x' not in M[int(b) - 1] and '0' not in M[int(b) - 1]:  # Проверка, что поле не занято
        M[int(b) - 1] = '0'

    else:
        while True:
            print('занято')
            b = input('Введите число от 1 до 9 : ')
            if b not in [str(i) for i in range(1, 10)]:
                print('Вы ввели не то')
                continue
            if 'x' not in M[int(b) - 1] and '0' not in M[int(b) - 1]:
                M[int(b) - 1] = '0'
                break
    # Проверка выигрышных комбинаций
    if ('0' in M[0] and '0' in M[1] and '0' in M[2]) or ('0' in M[3] and '0' in M[4] and '0' in M[5]) or (
            '0' in M[6] and '0' in M[7] and '0' in M[8]) or ('0' in M[0] and '0' in M[3] and '0' in M[6]) or (
            '0' in M[1] and '0' in M[4] and '0' in M[7]) or ('0' in M[2] and '0' in M[5] and '0' in M[8]) or (
            '0' in M[0] and '0' in M[4] and '0' in M[8]) or ('0' in M[2] and '0' in M[4] and '0' in M[6]):
        playing_field()
        print('Победил игрок 2!')
        break
    playing_field()
