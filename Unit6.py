from pprint import pprint


class animal:
    status_feed = 'Hungry'
    common_name = []
    common_weight = []
    def __init__(self, name = 'animal', weight = 0, vote = 'not'):
        self.name = name
        self.weight = weight
        self.vote = vote
        self.common_weight.append(self.weight)
        self.common_name.append(self.name)


    def feed(self):
        self.status_feed = 'fed'

class animal_dird(animal):
    eggs = 0
    def pick_eggs(self, sum):
        self.eggs += sum
        print("Собрано яиц", self.eggs)

class milk_animal(animal):
    milk_stat = "Not"
    def milk(self):
        self.milk_stat = "Yes"
        print(self.name, "подоен")

class trimmed_animal(animal):
    cut_status = "Not"
    def cut(self):
        self.cut_status = "Yes"
        print(self.name, " подстрижена")


goose1 = animal_dird("Серый", 5, "Ga Ga Ga")
print(goose1.name)
goose1.feed()
print(goose1.status_feed)
goose1.pick_eggs(2)
print(goose1.__dict__)

goose2 = animal_dird("Белый", 4, "Ga Ga Ga")
print(goose2.name)
goose2.feed()
print(goose2.status_feed)
goose2.pick_eggs(1)
print(goose2.__dict__)

chicken1 = animal_dird("Ко Ко", 3, "Ko Ko Ko")
print(chicken1.name)
chicken1.feed()
print(chicken1.status_feed)
chicken1.pick_eggs(4)
print(chicken1.__dict__)

chicken2 = animal_dird("Кукареку", 3, "Ko Ko Ko")
print(chicken2.name)
chicken2.feed()
print(chicken2.status_feed)
chicken2.pick_eggs(5)
print(chicken2.__dict__)

duck = animal_dird("Кряква", 8, "Gaaaaaaa")
print(duck.name)
duck.feed()
print(duck.status_feed)
duck.pick_eggs(5)
print(duck.__dict__)

cow = milk_animal("Манька", 90, "Mu Mu Mu Mu Mu")
print(cow.name)
cow.feed()
print(cow.status_feed)
cow.milk()
print(cow.__dict__)

goat1 = milk_animal("Рога", 60, "Me Me Me Me")
print(goat1.name)
goat1.feed()
print(goat1.status_feed)
goat1.milk()
print(goat1.__dict__)

goat2 = milk_animal("Копыта", 58, "Me Me Me Me")
print(goat2.name)
goat2.feed()
print(goat2.status_feed)
goat2.milk()
print(goat2.__dict__)

sheep1 = trimmed_animal("Барашек", 80, "Be Be Be Be")
print(sheep1.name)
sheep1.feed()
print(sheep1.status_feed)
sheep1.cut()
print(sheep1.__dict__)


sheep2 = trimmed_animal("Кудрявый", 90, "Be Be Be Be")
print(sheep2.name)
sheep2.feed()
print(sheep2.status_feed)
sheep2.cut()
print(sheep2.__dict__)


#pprint(animal.__dict__)
#print(animal.common_weight)
#print(animal.common_name)

sum = dict(zip(animal.common_name,animal.common_weight))
#print(sum)
sum_weight = 0
max_weight = 0
neme_max = 0


for i, j in sum.items():
    sum_weight += j
    if j > max_weight:
        max_weight = j
        neme_max = i

print("Суммарный вес ", sum_weight)

print("Самое тяжелое животное ", neme_max, " с весом ", max_weight)

