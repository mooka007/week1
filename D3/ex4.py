class Zoo:

    def __init__(self, zoo_name):
        self.animals = [] # list of animal objects
        self.zoo_name = zoo_name
    

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print("Animal already exists in the zoo")

    def get_animals(self):
        for animal in self.animals:
            print(f"Animal in The Zoo : {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold")
        else:
            print("Animal not found in the zoo")



    def sort_animals(self):
        sorted_animals = {}
        for animal in self.animals:
            firstLetter = animal[0].upper()
            if firstLetter not in sorted_animals:
                sorted_animals[firstLetter]= []
            sorted_animals[firstLetter].append(animal)
        return sorted_animals
    
    def get_groups(self):
        groups= self.sort_animals()
        print("Animals grouped by first Letter")
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")
    

casaBlanca = Zoo("Casa Zoo")
casaBlanca.add_animal("Lion")
casaBlanca.add_animal("meow")
casaBlanca.add_animal("Tiger")
casaBlanca.get_groups()



