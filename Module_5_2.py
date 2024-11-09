class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Такого этажа не существует')
        else:
            floor = 0
            while new_floor:
                if floor < new_floor:
                    floor = floor + 1
                    print(floor)
                    continue
                else:
                    break
