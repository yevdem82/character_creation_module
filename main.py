"""Модуль character_creation_module отвечает за создание персонажа
в RPG-игре «Питонические Воины: Тёмная Сторона Кода»"""

from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Возвращает строковое сообщение о проведённой атаке.

    Генерирует количество очков атаки в зависимости от выбранного
    типа персонажа и возвращает строковое сообщение о проведённой атаке.

    :param char_name: имя персонажа
    :param char_class: тип персонажа
    :return: сообщение о проведённой атаке
    """
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}'
    if char_class == 'mage':
        return f'{char_name} нанёс урон противнику равный {5 + randint(5, 10)}'
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')
    return f'{char_name} не нанёс урон противнику'


def defence(char_name: str, char_class: str) -> str:
    """Возвращает строковое сообщение о выполненном блокировании атаки.

    Генерирует количество очков защиты в зависимости от выбранного типа
    персонажа и возвращает строковое сообщение о выполненном
    блокировании атаки.

    :param char_name: имя персонажа
    :param char_class: тип персонажа
    :return: сообщение о блокировании атаки
    """
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'
    return f'{char_name} не блокировал урона'


def special(char_name: str, char_class: str) -> str:
    """Возвращает сообщение о применении специального умения.

    Возвращает сообщение о применении специального умения в зависимости
    от выбранного типа персонажа.

    :param char_name: имя персонажа
    :param char_class: тип персонажа
    :return: сообщение о применении специального умения
    """
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость '
                f'{80 + 25}»')
    if char_class == 'mage':
        return f'{char_name} применил специальное умение «Атака {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} применил специальное умение «Защита {10 + 30}»'
    return f'{char_name} не применил никакое специальное умение'


def start_training(char_name: str, char_class: str) -> str:
    """Запускает цикл тренировки навыков персонажа.

    В качестве параметров она получает введённое игроком имя персонажа
    и выбранный тип персонажа.

    :param char_name: имя персонажа
    :param char_class: тип персонажа
    :return: сообщение о тренировке навыков персонажа
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или special — '
          'чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Позволяет игроку выбрать тип игрового персонажа.

     Возвращает выбранный вариант игрового персонажа.

    :return: сообщение о выбранном варианте типа игрового персонажа
    """
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь '
                           'играть: Воитель — warrior, Маг — mage, Лекарь — '
                           'healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый '
                  'и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким '
                  'интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из '
                  'природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или любую '
                               'другую кнопку, чтобы выбрать другого '
                               'персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
