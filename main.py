from random import randint

class Character:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.stamina = 80
        self.attack = 5
        self.defense = 10

    def attack(self):
        pass

    def defense(self):
        pass

    def special(self):
        pass

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
