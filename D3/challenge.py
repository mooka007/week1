class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {} #dictionnary
    

    def add_animal(self, animal, count=1):
        if animal not in self.animals:
            self.animals[animal] = count
        else:
            self.animals[animal] += count
    

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in sorted(self.animals.items()):
            info += f"{animal} : {count}\n"
        info += "\n ---------- \n"
        return info
    
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('cow', 5)
macdonald.add_animal('cow', 5)
macdonald.add_animal('cow', 5)
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat', 12)

print(macdonald.get_info())