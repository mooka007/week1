birthdays = {
    "Albert Einstein": "1879/03/14",
    "Isaac Newton": "1643/01/04",
    "Marie Curie": "1867/11/07",
    "Stephen Hawking": "1942/01/08",
    "Alan Turing": "1912/06/23"
}

print("Welcome! You can look up the birthdays of famous scientists.")
name = input("Enter a scientist's name: ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don't have birthday information for {name}.")