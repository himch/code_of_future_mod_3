# Этот код я создал для того чтобы люди которые проверяют этот код смогли пройти эту игру что я сам создал.
# СЮЖЕТ: В начале игры вы залезаете в дом хотя его ограбить,далее в игре.
# СОЗДАТЕЛЬ: Граудиньш Илья

end_gema_flag = False
while not end_gema_flag:
    while True:
        print('Вы забрались в дом,рештв его ограбить.Вдруг разбитое вами окно закрывается железной оградой.Вы слышите '
              'голос доносящийся из глубин дома.')
        # Эта команда отвечает за ввод
        print(
            'Здравствуй,воришка ты наверное удивлен что я запер тебя в этом доме.Я хочук сыграть с тобой в игру если '
            'ты выберешся из дома.Молодец.Если нет то ты умреш. ')
        print('Итак начнем же представление.')
        print(
            'Перед собой ты видишь дверь,но ты можешь осмотреть эту комнату учти после выхода из этой комнаты в нее '
            'больше невернутся.')
        action = int(input('Введите 1 если хотите обыскать комнату.Введите 2 если хотите войти в дверь.'))
        # эта команда отвечает за работу кода т.е переменная
        if action == 1:
            print('ВЫ ОБЫСКАЛИ КОМНАТУ.Вы нашли кинжал.Он поможет вам уничтожить монстров.')
        elif action == 2:
            print(
                'Вы вошли в комнату увидели там монстров и погибли.Открыв глаза вы поняли что вам это '
                'приснилось.ПОПРОБУЙТЕ обыскать комнату.')
            print(
                'У вас есть выбор или обыскать комнату или пойти в одну из двух дверей.Напиши 1 если обыскать или '
                'комната 2 или 3.')
            choice = int(
                input('Вы вошли в комнату взяв кинжал войдя в комнату.Вы уничтожили всех монстров и сели отдохнуть.'))
            if choice == 1:
                print('Вы обыскали комнату и нашли бумажку с цифорками.Цифры:7009.Вы заходите в 3-ую комнату.')
            elif choice == 2:
                print('Вы встретили гоблина который вас убил.Начните сначало')
            elif choice == 3:
                print('Вы несмогли зайти в комнату ведь там пароль.')
            print('Вы зашли в комнату и увидели там огромного слизня который сразу побежал на вас.')
            choice2 = int(input('У вас есть варианты либо 1 бегать уклонятся или 2 пойти в атаку'))
            if choice2 == 1:
                print('Вы очень долго бегали cпоткнулись,упали и погибли от атаки слизня')
            elif choice2 == 2:
                print(
                    'Вы пошли в атаку,оказалось что слизень просто защищал своих детей.Вы оставили его и он решил вам '
                    'дать сундук в котором лежал лук с веревкой.')
                choice3 = int(input('Введите 1 чтобы войти в комнату.Введите 2 чтобы покушать пиццу из слизи.'))
                if choice3 == 1:
                    print(
                        'Вы вошли в комнату и упали в яму.Зацепившись за ветку вы решили воспользоватся веревкой и '
                        'луком что вам подарил слизень.')
                elif choice3 == 2:
                    print('Вы съели пиццу из слизи и погибли.')
                    choice4 = int(input(
                        'Вы решили зайти в комнату и увидели там сундук.Введите 1 чтобы открвть сундук.Или Введите 2 '
                        'чтобы обыскать комнату.'))
                    if choice4 == 1:
                        print('Вы открыли сундук и погибли от шипов что вонзились в спину.')
                    elif choice4 == 2:
                        print(
                            'Вы нашли проход в стене на улицу войдя туда вас встречает полиция.Они говорят вам '
                            'поднять руки за то что вы вломились в дом.')
                        print('Вы решили сдатся. Оказалось что если бы вы попытались убежать то погибли бы.КОНЕЦ.')
                        break
    choice = input('хотите повторить? (Д) или любое значение для выхода')
    if choice != 'Д':
        end_gema_flag = True
