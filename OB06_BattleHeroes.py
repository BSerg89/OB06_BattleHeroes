from faker import Faker
import random


# Класс Hero
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанёс {damage} урона!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: Здоровье = {self.health}"


# Класс Game
class Game:
    def __init__(self, player_name):
        fake = Faker()  # Создаём экземпляр Faker для генерации имени
        computer_name = fake.first_name()  # Генерация случайного имени для компьютера
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            # Запрос на продолжение боя или сдачу
            choice = input(
                f"{self.player.name}, хотите продолжить бой или сдаться? (введите 'бой' или 'сдаться'): ").strip().lower()
            if choice == 'сдаться':
                print(f"{self.player.name} сдался! {self.computer.name} победил!")
                break
            elif choice == 'бой':
                # Ход игрока
                self.player.attack(self.computer)
                if not self.computer.is_alive():
                    print(f"{self.computer.name} повержен. {self.player.name} победил!")
                    break
            else:
                print("Некорректный ввод, попробуйте снова.")
                continue

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} повержен. {self.computer.name} победил!")
                break

            # Вывод текущего состояния здоровья
            print(self.player)
            print(self.computer)
            print("-" * 30)

        print("Игра окончена!")


# Основная программа
if __name__ == "__main__":
    player_name = input("Введите имя своего героя: ")
    game = Game(player_name)
    game.start()
