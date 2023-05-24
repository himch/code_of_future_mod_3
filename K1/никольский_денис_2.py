# Быки и коровы, Никольский Денис
import random

def game():
    count_b = 0
    count_k = 0
    list_win = []
    secret_num = ''
    for _ in range(4):
        secret_num += random.choice("0123456789")
    print(list(secret_num))
    print('Тебе загадана последовательность из 4 цифр. Ты пытаешься отгадать эти цифры. Если ты угадал цифру и она на своем месте, то это бык. Но если ты угадал цифру, но не её место, то это корова. Ну что ж, сыграемс?')
    while list_win != list(secret_num):
        print('Твои буквы:')
        for i in range(4):
            num = input()
            list_win.append(num)
        for q in range(4):
            for h in range(4):
                if list_win[q] == list(secret_num)[h]:
                    if q == h:
                        count_b += 1
                    else:
                        count_k += 1
        if list_win == list(secret_num):
            print('Ты выиграл! Ты угадал последовательность:', list_win)
            break
        else:
            print('Пока не отгадал. Поробуй ещё раз!')
            print('Твоя последовательность:', list_win)
            print('Количество быков:', count_b)
            print('Количество коров:', count_k)
            list_win.clear()
            count_b = 0
            count_k = 0
game()