import numpy as np


def game_core_v3(number):
    count = 1
    predict = np.random.randint(1, 101)
    if number // predict >= 2:
        predict *= 2
    elif number / predict < 1:
        predict //= 2

    while number != predict:
        count += 1
        if number > predict:
            if number % 2 == 0:
                if predict % 2 == 0:
                    predict += 6
                else:
                    predict += 1
            else:
                predict += 7
        elif number < predict:
            if number % 2 == 0:
                if predict % 2 == 0:
                    predict -= 4
                else:
                    predict -= 1
            else:
                predict -= 5
    return count  # выход из цикла, если угадали


def score_game(game_core):
    count_ls = []
    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

score_game(game_core_v3)
