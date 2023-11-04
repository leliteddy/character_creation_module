from random import randint
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80  


class Character:
    # Новая константа.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'
    ...
if char_class == 'warrior':
    print('Воитель — дерзкий воин ближнего боя. '
          'Сильный, выносливый и отважный.')
if char_class == 'mage':
    print('Маг — находчивый воин дальнего боя. '
          'Обладает высоким интеллектом.')
if char_class == 'healer':
    print('Лекарь — могущественный заклинатель. '
          'Черпает силы из природы, веры и духов.')
    
    ...

warrior = Warrior('Кодослав')
print(warrior)
print(warrior.attack())

# Вывод в терминал:
# Warrior — дерзкий воин ближнего боя. Сильный, выносливый и отважный.
# Кодослав нанёс урон противнику, равный 8


...


    def __init__(self, name):
        self.name = name
    
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}.')
    
    def defence(self):
        # Вычисляем значение защиты в переменной value_defence.
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

        if char_class == 'warrior':
            return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
        if char_class == 'mage':
            return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
        if char_class == 'healer':
            return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
        return '{char_name} блокировал 10 урона'


    def special(self):
        # Здесь описано тело метода special().
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.' 

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита' 

    def start_training(self):
        print(f'{self.name}, ты {self.class_type} — мастер своего дела.')
        print('Потренируйся управлять своими навыками.')
        print('Введи одну из команд: attack — чтобы атаковать противника, '
              'defense — чтобы блокировать атаку противника или '
              'special — чтобы использовать свою суперсилу.')
        print('Если не хочешь тренироваться, введи команду skip.')
        cmd = None
        while cmd != 'skip':
            cmd = input('Введи команду: ')
            if cmd == 'attack':
                print(self.attack())
            elif cmd == 'defense':
                print(self.defense())
            elif cmd == 'special':
                print(self.special())
        return 'Тренировка окончена.'

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 'Воитель')

    def attack(self):
        damage = 5 + randint(3, 5)
        return f'{self.name} нанёс противнику урон, равный {damage}'

    def defense(self):
        block = 10 + randint(5, 10)
        return f'{self.name} блокировал {block} ед. урона'

    def special(self):
        return f'{self.name} применил специальное умение «Выносливость {80 + 25}»'

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 'Маг')

    def attack(self):
        damage = 5 + randint(5, 10)
        return f'{self.name} нанёс противнику урон, равный {damage}'

    def defense(self):
        block = 10 + randint(-2, 2)
        return f'{self.name} блокировал {block} ед. урона'

    def special(self):
        return f'{self.name} применил специальное умение «Атака {5 + 40}»'

class Healer(Character):
    def __init__(self, name):
        super().__init__(name, 'Лекарь')

    def attack(self):
        damage = 5 + randint(-3, -1)
        return f'{self.name} нанёс противнику урон, равный {damage}'

    def defense(self):
        block = 10 + randint(2, 5)
        return f'{self.name} блокировал {block} ед. урона'

    def special(self):
        return f'{self.name} применил специальное умение «Защита {10 + 30}»'

def choice_char_class():
    char_class = input('Выбери класс персонажа (Воитель, Маг, Лекарь): ').strip().lower()
    return char_class

def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}!')
    char_class = choice_char_class()
    if char_class == 'воитель':
        character = Warrior(char_name)
    elif char_class == 'маг':
        character = Mage(char_name)
    elif char_class == 'лекарь':
        character = Healer(char_name)
    else:
        print('Неверный класс персонажа. Игра завершена.')
        return
    print(character.start_training())

if __name__ == "__main__":
    main()