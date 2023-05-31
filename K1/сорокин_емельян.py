import datetime

# список доступных команд
commands = ['привет', 'как дела', 'список фильмов', 'вычисли', 'дата']

# список фильмов
movies = ['Зеленая миля', 'Форрест Гамп', 'Начало', '1+1', 'Жизнь прекрасна']


# функция, выполняющая команду
def run_command(command):
    if command == 'привет':
        print('Привет!')
    elif command == 'как дела':
        print('Хорошо, спасибо!')
    elif command == 'список фильмов':
        print('Список фильмов:')
        for movie in movies:
            print('- ' + movie)
    elif command.startswith('вычисли'):
        expression = command.split(' ')[-1]
        try:
            result = eval(expression)
            print('Результат: ' + str(result))
        except (SyntaxError, NameError, TypeError, ZeroDivisionError, ValueError):
            print('Ошибка')
    elif command == 'дата':
        today = datetime.date.today()
        print('Сегодняшняя дата: ' + str(today))


# приветствие и описание возможных команд
print('Привет! Я твой персональный помощник. Я могу ответить на следующие команды:')
for command in commands:
    print('- ' + command)

# ввод и выполнение команд
while True:
    user_input = input().lower()
    if user_input == 'закрыть':
        break
    elif user_input not in commands:
        print('Команда не распознана. Попробуйте еще раз.')
    else:
        run_command(user_input)
