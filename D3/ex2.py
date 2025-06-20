class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes Woof!")

    
    def jump(self):
        print(f"{self.name} jump {self.height * 2} cm high!")

    
davids_dog = Dog("Buddy", 150)
sarahs_dog = Dog("Luna", 60)


if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}.")
else:
    print(f"The bigger dog is {sarahs_dog.name}.")