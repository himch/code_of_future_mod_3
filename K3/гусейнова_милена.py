# Гусейнова Милена --- игра Текстовый Квест

end_game = False
while not end_game:  # это игра на удачу,и по поиску сокровищ
    while True:
        print('Привет, ты попал в мой квест.')  # приветствие
        print('Ты очнулся в незнакомом тебе помещении, квест начался!')  # появление в игре
        print('Перед тобой есть 3 двери с номерами: 1, 2 или 3.')  # деревья
        num_1 = input()
        if num_1 == '3':
            print('Когда ты вошёл комнату, ловушка сомкнулась на тебе. Ты проиграл.')  # проигрыш
        elif num_1 == '1':
            print('Ты упал в лаву. Мне очень жаль.')  # проигрыш
        if num_1 == '2':
            print('Ты попал в следующую комнату.')  # проход дальше
            print('Отсюда ты можешь выйти через две двери.')
            print('Дверь справа под номером 1, дверь слева под номером 2.')
            print('В какой двери выход? В правой или левой двери?')  # вопрос
            num_2 = input()
            if num_2 == 'в правой':
                print('Ты открыл правую дверь. Но за ней был большой слизень. Вы проиграли.')  # проигрыш
            elif num_2 == 'в левой':
                print('Ты в следующей комнате.')
                print('Здесь есть три двери. Первая, вторая и третья. Введи номер двери.')
                num_3 = input()
                if num_3 == '2':
                    print('Огромный кол пронзил твою грудь. Игра окончена.')  # проигрыш
                elif num_3 == '1':
                    print('Ты прошёл в комнату, но ты упал в ров с пираньями. Тебя съели.')  # проигрыш
                if num_3 == '3':
                    print('Ты попал в четвёртую комнату.. Увы.. Но ты прошёл дальше.')
                    print('Хочешь секрет. Тут есть подсказка. Введи 321 чтоб найти её.')  # подсказка
                    num_4 = input()
                    if num_4 == '321':
                        print('Правильная дверь находится сбоку.')
                        num_5 = input('А теперь введи число 1, 2 или 3')
                        if num_5 == '3':
                            print('В этой комнате тебя ждёт монстр. Тебя поразил меч гоблина.')  # проигрыш
                        elif num_5 == '2':
                            print('Ты сорвался вниз. Там яма с шипами. Ты не выжил.')  # проигрыш
                        elif num_5 == '1':
                            print('Ты прошёл в последнюю комнату.')
                            print('Вот твои сокровища. Поздравляю, было весело.')  # выигрыш
                        choice = input('Хочешь сыграть ещё раз? Чтоб выйти (Нет).')
                        if choice == 'Нет':
                            end_game = True
                            break
