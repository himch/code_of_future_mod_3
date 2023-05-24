# Текстовый квест, Никольский Денис
import random

lifes = 3
words = ['кот','секрет','пиво','сосиска','пароль',',банан','слово','взлом','жопа','книга','нигер','хрен','бесперспектяковый','облом','атака']
print('Привет, я Денис Никольский и ты попал в мою игру. '
      ' Ты находишся на луне, чтобы найти детали машины теслы, которая упала на планету год назад.'
      ' Но неожиданно ты теряешь сознание и оказываешься в непонятной комнате. У тебя есть три пути: вправо,влево,вперед')
quest = random.randint(2,4)
flag = True
flag1 = True
quest_completed = 0
hp_gg = 10
atk_gg = 6
print(' ')
print('Ты можешь сыграть в небольшую рулетку. Каждый раз, когда ты пишешь "+", ты получаешь случайную прибавку к здоровью от 1 до 5 к начальному здоровье (начальное здоровье равно 10). Если твоё здоровье будет больше 20, то ты начнешь игру с 5 очками здоровья.'
            'Для того, чтобы окончить прибавку к здоровью, напиши "стоп"')
while flag:
      word = input()
      if word == '+':
            hp_gg += random.randint(1,5)
            print('Твое здоровье:', hp_gg)
      if hp_gg > 20:
            print('Ты проиграл, теперь твоё здоровье равно 5')
            hp_gg = 5
            flag = False
      if word == 'стоп':
            print('Переход к следующему этапу...')
            flag = False
print('')
print('Теперь давай опредилимся с твоей силой атаки. Условия те же. Напиши "+" чтобы увеличить атаку от 1 до 3 единиц.'
      'Если же твоя атака будет больше 15, то она опустится до 4. Для перехода к началу игры напиши "стоп"')
while flag1:
      word2 = input()
      if word2 == '+':
            atk_gg += random.randint(1,3)
            print('Твоя атака:', atk_gg)
      if atk_gg > 15:
            print('Ты проиграл, теперь твоя атака равна 4')
            atk_gg = 4
            flag1 = False
      if word2 == 'стоп':
            print('Начало игры...')
            flag1 = False
print('Ты начинаешь с', hp_gg ,'очками здоровья')
print('Значение твоей атаки:', atk_gg)

print('Тебе нужно найти ', quest, 'загадок. Когда ты решишь их ты выберишься из неизвестного места и выиграешь. Местоположение загадок неизввестно.')

rooms = [1,2,3,4,5,6,7,9]
rooms1 = [1,2,3,4,5,6,7,9]

quest_rooms = []

for i in range(quest):
      luck = random.randint(1, len(rooms))
      quest_rooms.append(rooms[luck-1])
      rooms.pop(luck - 1)
print('Комнаты с загадками:', quest_rooms)

count_monsters = random.randint(1,4)
monster_rooms = []

base_room = 8

for q in range(count_monsters):
    luck_monster = random.randint(1, len(rooms1))
    monster_rooms.append(rooms1[luck_monster-1])
    rooms1.pop(luck_monster - 1)
print('Комнаты с монстрами', monster_rooms)

length = len(quest_rooms)

print('Карта:')
print('1  2  3')
print('4  5  6')
print('7  8  9')
print(' ')
print('Ты находишься в комнате 8')

while quest_completed != length:
    if lifes < 1:
        print('К сожалению ты проиграл. Перед смертью ты увидел, как в твою комнату заходит голый шрек....')
        break
    print('Ты можешь пойти вперед, назад, вправо, влево (ты осташься в той же комнате, если действие невозможно)')
    print('')
    action = input('Куда идём?')
    if action == 'влево' and base_room != 1 and base_room != 4 and base_room != 7:
        base_room -= 1
        print('Твоя комната:', base_room)
    elif action == 'вправо' and base_room % 3 != 0:
        base_room += 1
        print('Твоя комната:', base_room)
    elif action == 'назад' and base_room != 7 and base_room != 8 and base_room != 9:
        base_room += 3
        print('Твоя комната:', base_room)
    elif action == 'вперед' and base_room != 1 and base_room != 2 and base_room != 3:
        base_room -= 3
        print('Твоя комната:', base_room)
    else:
        print('Проход невозможен, ты до сих пор в комнате', base_room)

    if base_room in monster_rooms:
        print('Ты попал к монстру, у тебя два пути: либо же ты бьешься ("атака") с ним, ли же убегаешь ("побег"), теряя одну жизнь')
        hp_mon = random.randint(15, 30)
        atk_mon = random.randint(1, 5)
        print('Здоровье монстра:', hp_mon)
        print('Атака монстра:', atk_mon)
        way = input('Что же ты веберешь?')
        if way == 'побег':
            print('Ты теряешь одну жизнь, теперь у тебя их', lifes)
            lifes -= 1
        if way == 'атака':
            print('Ты начал(а) борьбу с монстром...')
            while hp_mon > 0 and hp_gg > 0:
                if hp_mon - atk_gg <= 0:
                    print('Герой наносит удар. Здоровье монстра:', 0)
                    hp_mon -= atk_gg
                    break
                else:
                    print('Герой наносит удар. Здоровье монстра:', hp_mon - atk_gg)
                    hp_mon -= atk_gg
                if hp_gg - atk_mon <= 0:
                    print('Монстр наносит удар. Здоровье героя:', 0)
                    hp_gg -= atk_mon
                    break
                else:
                    print('Монстр наносит удар. Здоровье героя:', hp_gg - atk_mon)
                    hp_gg -= atk_mon
            if hp_mon <= 0:
                monster_rooms.remove(base_room)
                print('Ты победил монстра, и ты можешь продолжить путь, если конечно тут нету загадки)')
            if hp_gg <= 0:
                print('Ты умер, и ты потерял одну жизнь. У тебя их осталось:', lifes - 1)
                lifes -= 1
    if base_room in quest_rooms:
        flag2 = True
        print('Заходя в комнату, ты увидел сундук. Ты попытался его открыть, но он оказался закрыт. Но не ожиданно на сундуке образовалась галограмма:'
              '"Я загадал не которое слово из некоторого количества букв (от 3 до 16 букв). Тебе дано 7 попыток, чтобы отгадать буквы, входящие в это слово. Если ты угадаешь слово, то сундук откроется. Иначе тебе придётся решать загадку заново..."')
        while flag2:
            rand_word = random.randint(0,len(words) - 1)
            for _ in range(1, 8):
                print('Попытка', _, 'из', 7)
                letter = input()
                for i in range(len(list(words[rand_word]))):
                    if letter == list(words[rand_word])[i]:
                        print('Буква нашлась на месте', i + 1)
                        flag2 = True
                if flag2 == False:
                    print('Буква не нашлась')
                flag2 = False
            final_word = input('Твоё слово?')
            if final_word == words[rand_word]:
                print('Пароль подошёл! Сундук открылся и на галограмме появилась надпись:')
                flag2 = False
                quest_completed += 1
                quest_rooms.remove(base_room)
                print('Ты отгадал загадку! Тебе осталось пройти', len(quest_rooms),'загадки')
                print('')
            else:
                print('Пароль не подошёл! Правильное слово:', words[rand_word])
print('Игра окончена! Ты смог выбраться! Когда ты решил последнюю загадку, то всё потменело, и то снова оказался на марсе. Рядом с тобой оказалась записка:'
      'Спасибо за игру!~ (Шрек)')