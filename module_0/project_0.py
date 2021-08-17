import numpy as np


def game_core_v3(number):
    count = 1
    if 0 < number <= 10:
        predict = 5
    elif 10 < number <= 20:
        predict = 15
    elif 20 < number <= 30:
        predict = 25
    elif 30 < number <= 40:
        predict = 35
    elif 40 < number <= 50:
        predict = 45
    elif 50 < number <= 60:
        predict = 55
    elif 60 < number <= 70:
        predict = 65
    elif 70 < number <= 80:
        predict = 75
    elif 80 < number <= 90:
        predict = 85
    elif 90 < number <= 100:
        predict = 95

    while number != predict:
        count += 1
        if number > predict:
            if number % 2 == 0:
                if predict % 2 == 0:
                    predict += 2
                else:
                    predict += 1
            else:
                predict += 3
        elif number < predict:
            if number % 2 == 0:
                if predict % 2 == 0:
                    predict -= 2
                else:
                    predict -= 1
            else:
                predict -= 1
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