# Проект Евы Баранюк --- Текстовый Квест


name = input('Введите свой ник')
print('Здравствуй,', name, ', сегодня тебе предстоит взять на себя роль рыцаря и спасти принцессу из замка, наполненного монстрами. На момент начала игры тебе доступно 9 жизней. Тебе придется разгадывать загадки, бороться с жителями старинного дворца и переходить из комнаты в комнату.')
answer = input('Готов услышать правила игры? Ответь "да", если можем приступать')
if answer == 'да' or answer == 'Да':
    print('Отлично! Я рад это слышать. У тебя есть 4 основных варианта хода: перемещение, поиск улик, атака, побег. Ты сможешь воспользоваться последней функцией, если в комнате есть монстры, а ты выбрал действие "перемещение" или "поиск улик". Если действие "перемещение" и монстров нет, то ты можешь выбрать направление для перехода в другую комнату. Если действие "поиск улик" и монстров нет, то тебе предстоит разгадать загадку для ее получения. Если действие "атака" и монстры есть, то тебе предстоит принять участие в битве.')
else:
    print('Ладно, видимо тебя уже не надо инструктировать.')
print('Ты находишься перед воротами древнего замка. Где-то за его стенами скрыввается прекрасная принцесса, которой тебе нужно помочь. Итак, игра начинается.')
step_1 = input('Ты в первой комнате. Тут нет монстров. Что будешь делать? Напоминаю, ты можешь либо перейти в другую комнату (действие "перемещение"), либо обыскать комнату (действие "поиск улик").')
if step_1 == 'перемещение':
    print('Ты не можешь перейти в другую комнату. Дверь закрыта. Вернись назад и выбери действие "поиск улик"')
elif step_1 == 'поиск улик':
    print('Обыскиваю комнату. Найден закрытый на замок сундук. Вы можете отгадать код, решив пример.')
    answer1 = input('Готов? Если да, введи "готов".')
    if answer1 == "готов":
        example = int(input('1400 // 2 + 534'))
        if example == 1234:
            print('Поздравляю! Сундук открыт, ты получаешь ключ и автоматически передвигаешься ближе к принцессе.')
print('Ты в комнате с монстром. Самое время провести битву :) У тебя 9 жизней, у этого монстра всего 2')
health_hero = 9
hero = 1
health_monster = 2
monster = 2
while health_monster > 0 and health_hero > 0:
    health_monster -= hero
    if health_monster < 0:
        health_monster = 0
    print('Герой наносит удар. Здоровье монстра:', health_monster)
    health_hero -= monster
    if health_hero < 0:
        health_hero = 0
    print('Монстр наносит удар. Здоровье героя:', health_hero)
print('Поздравляю! Эту битву ты выиграл! Выбери действие перемещение и ты окажешься в другой комнате.')
if step_1 == 'перемещение':
    print('В этой комнате 5 монстров. Ты можешь выбрать действие "побег" и автоматически перейдешь в башню замка, где и принцессу')
if step_1 == 'побег':
    print('Поздравляю! Квест пройден, ты нашел принцессу и спас ее из замка!')
