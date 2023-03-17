# class Car:
#     def __init__(self):
#         self.marka = input("Cho za marka?")
#         self.svet = input("Svet kakoi?")
#         self.tipdvigatelya = input("Tip dvijka?")
#
#     def drive(self):
#         print("Yehal ya domoi s raboty")
#
#     def __str__(self):
#         return f"Marka mashini eto {self.marka}\n Svet mashini eto {self.svet}\n Tip dvigatelya eto {self.tipdvigatelya}\n "
#
# jigul = Car()
# print(jigul)
# jigul.drive()

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 50
        self.hunger = 100
        self.reputation = 0
        self.zavisimost = 0
        self.alive = True

    def to_study(self):
        print("Время учебы")
        self.progress += 0.12
        self.gladness -= 5
        self.money -= 5
        self.hunger -= 10
        self.reputation += 0.5

    def to_sleep(self):
        print("Посплю")
        self.gladness += 3
        self.hunger -= 3
        self.progress -= 0.1
        self.reputation -= 0.3
        self.zavisimost += 0.4

    def to_chill(self):
        print("Время отдыха")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5
        self.reputation -= 0.5

    def to_work(self):
        print("Я обязан arbeit")
        self.gladness -= 7
        self.progress += 0.12
        self.money += 40
        self.hunger -=4
        self.zavisimost -= 0.3

    def to_podrabotka(self):
        print("Подзаработал")
        self.gladness -= 3
        self.progress += 0.03
        self.money += 20
        self.hunger -= 1.6
        self.zavisimost -= 0.1

    def to_kafe(self):
        print("Перекусил в кафе")
        self.gladness += 4
        self.progress -= 0.08
        self.money -= 10
        self.hunger += 20
        self.zavisimost -= 0.5

    def podarok_uchitelu(self):
        print("Подорил шоколадку")
        self.gladness += 5
        self.progress += 1
        self.money -= 20
        self.reputation += 1

    def to_bar(self):
        print("Пошел в бар")
        self.gladness += 7
        self.progress -= 0.25
        self.money -= 20
        self.reputation -= 0.6
        self.zavisimost += 1

    def to_sport(self):
        print("Спорт-жизнь, не спорт-не спорт")
        self.gladness += 5
        self.zavisimost -= 0.5
        self.hunger -= 20





    def is_alive(self):
        if self.progress < -0.5:
            print("================Отчисление================")
            self.alive = False
        elif self.gladness <= -10:
            print("================Диприсияя================")
            self.alive = False
        elif self.money <= -20:
            print("================Сбомжился================")
            self.alive = False
        elif self.hunger <= 0:
            print("================Смэрт от голода================")
            self.alive = False
        elif self.hunger >= 250:
            print("================Ожирение 20 степени================")
            self.alive = False
        elif self.reputation >= 10:
            print("================Подмазали================")
            self.alive = False
        elif self.reputation <= -4:
            print("================Выгнали потому-что плохой================")
            self.alive = False
        elif self.zavisimost >= 50:
            print("================Спился================")
            self.alive = False

    def end_of_day(self):
        print(f"Счастье = {self.gladness}")
        print(f"Прогресс учебы = {round(self.progress, 2)}")
        print(f"Репутация = {self.reputation}")
        print(f"Голод = {self.hunger}")
        print(f"Деньги = {self.money}")
        print(f"Зависимость = {self.zavisimost}")


    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 7)
        if self.money <= 5:
            print("Мало денег")
            self.to_podrabotka()
        elif self.gladness <= 0:
            print("Надо расслабиться")
            self.to_bar()
        elif self.progress <= -0.3:
            print("Надо браться за голову!")
            self.to_study()
        elif self.hunger <= 10:
            print("Есть охота")
            self.to_kafe()
        elif self.hunger >= 200:
            print("Так и распухнуть недолго")
            self.to_sport()
        elif self.reputation <= -2:
            print("Что-то все косо на меня смотрят")
            self.podarok_uchitelu()

        elif live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        elif live_cube == 5:
            self.to_kafe()
        elif live_cube == 6:
            self.podarok_uchitelu()
        elif live_cube == 7:
            self.to_bar()
        elif live_cube == 8:
            self.to_sport()

        self.end_of_day()
        self.is_alive()

nick = Student(name="Nickолай")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day+1)



