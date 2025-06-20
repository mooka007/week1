names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ").strip()

if user_name in names:
    print(f"First occurrence of {user_name} is at index {names.index(user_name)}")
else:
    print("Name not found in the list.")