class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


C1 = Cat("Tom", 5)
C2 = Cat("Jerry", 3)
C3 = Cat("Whiskers", 10)

cats = [C1, C2, C3]

def find_oldest_cat(cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(cats)


print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

