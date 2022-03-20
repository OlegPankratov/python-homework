from pprint import pprint
from random import randint
#  НАСЛЕДОВАНИЕ строка 67
#  ИНКАПСУЛЯЦИЯ _check_fuel_level _check_status
#  ПОЛИМОРФИЗМ изменения методов NewMechanism


class MechanismOptions:
    def bepp(self):
        print('Звуковой сигнал - ААААА')

class Mechanism:
    mass = 0
    status_work = 'WORK'
    status_stop = 'STOP'
    current_status = status_stop
    # work_type = ''  # fuel_type = 'бензин'# # объем бака # fuel_tank = 100 эти три строки из общих перематров задали ниже для конкретного механизма деф__инитом
    # литры
    fuel_level = 0

    def __init__(self, work_type, fuel_type, fuel_tank):
        self.work_type = work_type
        self.fuel_type = fuel_type
        self.fuel_tank = fuel_tank
        self.data = []

    def start(self):
        # если уровень топлива больше 0
        if self.fuel_level > 0:
            # дай текущий статус
            if self._check_status():
                print('не могу завести машину, она уже работает')
            # если не работаешь тогда запуск
            else:
                self.current_status = self.status_work
                self.fuel_level = self.fuel_level - 5
                print('машина заведена')
                return
        else:
            print('нет топлива, используйте команду add_fuel')
            return

    def stop(self):
        if self._check_status():
            self.current_status = self.status_stop
            print(f'Машина остановлена, топливо - {self.fuel_level}')
            return
        else:
            print('Машина уже остановлена')
            return

    def _check_fuel_level(self, fuel_guantity):
        return self.fuel_level + fuel_guantity <= self.fuel_tank

    def add_fuel(self, fuel_type, fuel_guantity):
        if fuel_type != self.fuel_type:
            print('этот тип топлива не подходит')
            return

        if not self._check_fuel_level(fuel_guantity):
            print(f"много топлива. Текущий уровень - {self.fuel_level}. Максимальный - {self.fuel_tank}")
            return

        self.fuel_level = self.fuel_level + fuel_guantity
        print(f'Бак {self.work_type} заправлен, есть {self.fuel_level}')
        return

    def _check_status(self):
        return self.current_status == self.status_work

    def get_status(self):
        print(f"Машина {self.work_type} сейчас - {self.current_status}. уровень топлива - {self.fuel_level}")
        return

class NewMechanism(Mechanism, MechanismOptions):
    def start(self):
        super().start()
        self.bepp()
        # if self.fuel_level > 0:
        #     if self.check_status():
        #         print('не могу завести машину, она уже работает')
        #     else:
        #         self.current_status = self.status_work
        #         self.fuel_level = self.fuel_level - 5
        #         print('машина заведена')
        #         self.bepp()
        #         return
        # else:
        #     print('нет топлива, используйте команду add_fuel')
        #     return

    def get_status(self):
        print(f"НЕТ ДАННЫХ")
        return

    def __str__(self):
        return f'{self.work_type}'


fixture = [
    {
        'name': 'сеялка',
        'fuel': 'бензин',
        'fuel_tank': 50
    },
    {
        'name': 'генератор',
        'fuel': 'газ',
        'fuel_tank': 100
    }
]

class Repository:
    items: list = []

    def add(self, instance):
        if isinstance(instance, NewMechanism):
            self.items.append(instance)

    def get(self, index):
        return item[index]

    def get_items(self):
        return self.items

    @property
    def guantity(self):
        return len(self.items)

repo = Repository()

for item in fixture:
    name, fuel, fuel_tank = item.values()
    repo.add(NewMechanism(name, fuel, fuel_tank))

for i in repo.items:
    # print(i)
    i.add_fuel(i.fuel_type, randint(1, 10))

# for i in repo.get_items():
#     print(i)

# for i in data:
#     print(i.fuel_level)

def calc(repo_obj: Repository):
    if not repo_obj.get_items():
        return 0

    fuel = 0
    for i in repo_obj.get_items():
        fuel += i.fuel_level

    result = fuel / repo_obj.guantity
    return result

print(calc(repo))



print('---------')
# for i in data:
#     i.add_fuel(i.fuel_type, 10)
# print('---------')
# for i in data:
#     i.start()
# print('---------')
# for i in data:
#     print(i)
#
# #     i.bepp()
# print(NewMechanism.mro())
# print('---------')



