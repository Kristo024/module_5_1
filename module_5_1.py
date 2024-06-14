class House:

    def __init__(self, name, number):  # конструктор класса (метод)
        self.name = name  # создаём атрибуты и приcваиваем им значения
        self.number_of_floors = number  # характеристика, атрибут
        # print(self.name)
        # print(self.number_of_floors)

    def go_to(self, new_floor):  # (метод)
        # print("new_floor",new_floor)
        # print('этажность', self.number_of_floors)
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 18) # в self попадает h1
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


