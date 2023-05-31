print('Программа Матвея Лукьянова 3 группа яндекс программирование')

print('Капитан Тит на планете Кузница-Грайя')
print('Капитан Тит приземлилися на планету под названием Кузница-Грайя, её захватили орки и Титу придётся сразится с'
      ' орками в замке состоящем из 6 комнат который называется Мануфакторий. '
      'Титу придётся отыскать специальные реликвии'
      ' чтобы он смог вернуться домой. У капитана Тита есть оружие - цепной мечь которым он может драться с врагами')
number = 1
while number < 6:

    print('число орков в текущей комнате')
    import random

    y = random.randint(0, 10)
    print(y)
    health_hero = 25
    print('здоровье Тита:', health_hero)
    strenght_hero = 5
    print('сила удара Тита:', strenght_hero)
    if y > 1:
        print('советуем выбрать действие побег, иначе вы можете проиграть')
        print('комнота в которой вы находитесь:', number)
    if y == 1:
        print('советуем выбрать действие атака')

    name = input('введите действие которые хотите выполнить'
                 'на выбор: перемещение, поиск улик, атака, побег')
    if name == 'перемещение':
        print('номер комнаты в которой вы находитесь:', number)
        if number == 1:
            print('вы можете перейти "вправо" или "вниз"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 2
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 4
            else:
                print('вы оказались в комнате номер', number)
        elif number == 2:
            print('вы можете перейти "вправо" или "вниз" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 3
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 5
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 1
            else:
                print('вы оказались в комнате номер', number)
        elif number == 3:
            print('вы можете перейти "влево" или "вниз"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 2
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 6
            else:
                print('вы оказались в комнате номер', number)
        elif number == 4:
            print('вы можете перейти "вправо" или "вверх"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 5
            elif movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 1
            else:
                print('вы оказались в комнате номер', number)
        elif number == 5:
            print('вы можете перейти "вправо" или "вверх" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 6
            elif movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 2
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 4
            else:
                print('вы оказались в комнате номер', number)
        elif number == 6:
            print('вы можете перейти "вверх" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 3
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 5
            else:
                print(number)
        if y == 0:
            print('хожу')
        else:
            print('убегаю')
    elif name == 'атака':
        print('здоровье Тита:', health_hero)
        print('сила удара Тита:', strenght_hero)
        health_monster = random.randint(1, 20)
        strenght_monster = random.randint(1, 5)
        while health_monster > 0 and health_hero > 0:
            health_monster -= strenght_hero
            health_hero -= strenght_monster
            if health_monster <= 0:
                health_monster = 0
                print('Тит наносит удар. Здоровье орка:', health_monster)
                break
            elif health_hero <= 0:
                health_hero = 0
                print('Тит наносит удар. Здоровье орка:', health_monster)
                print('орк наносит удар. Здоровье Тита:', health_hero)
                break
            else:
                print('Тит наносит удар. Здоровье орка:', health_monster)
                print('орк наносит удар. Здоровье Тита:', health_hero)
        if y == 0:
            print('Атаковать некого. Комната пуста.')
        else:
            print('бьюсь с орками')
    elif name == 'побег':
        print('убегаю')
        print('номер комнаты в которой вы находитесь:', number)
        if number == 1:
            print('вы можете перейти "вправо" или "вниз"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 2
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 4
            else:
                print('вы оказались в комнате номер', number)
        elif number == 2:
            print('вы можете перейти "вправо" или "вниз" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 3
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 5
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 1
            else:
                print('вы оказались в комнате номер', number)
        elif number == 3:
            print('вы можете перейти "влево" или "вниз"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 2
            elif movement == 'вниз':
                print('вы оказались в комнате номер', number + 3)
                number = 6
            else:
                print('вы оказались в комнате номер', number)
        elif number == 4:
            print('вы можете перейти "вправо" или "вверх"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 5
            elif movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 1
            else:
                print('вы оказались в комнате номер', number)
        elif number == 5:
            print('вы можете перейти "вправо" или "вверх" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вправо':
                print('вы оказались в комнате номер', number + 1)
                number = 6
            elif movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 2
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 4
            else:
                print('вы оказались в комнате номер', number)
        elif number == 6:
            print('вы можете перейти "вверх" или "влево"')
            print('перемещение которое вы хотите выбрать: вправо, влево, вниз, вверх')
            movement = input()
            if movement == 'вверх':
                print('вы оказались в комнате номер', number - 3)
                number = 3
            elif movement == 'влево':
                print('вы оказались в комнате номер', number - 1)
                number = 5
            else:
                print(number)
    elif name == 'поиск улик':
        if y == 0:
            print('обыскиваю комнату')
            n = ["песок", "земля", "воздух", "битва"]
            print('список слов которые будут за секречены:n')
            word = random.choice(n)
            success = True
            for x in range(5):
                letter = input()
                print('Попытка', x + 1, 'из 5')
                not_found = True
                for i, char in enumerate(word):
                    if char == letter:
                        not_found = False
                        print('Буква нашлась на месте', i + 1)
                if not_found:
                    success = False
                    print('Буква не нашлась')
            word2 = input()
            if word2 == word:
                print('Пароль подошёл!')
            else:
                print('Пароль не подошёл')
        else:
            print('убегаю')
    else:
        print('не правильно введено действие!')
