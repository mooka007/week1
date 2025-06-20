my_name = "Alice"
user_name = ""

while user_name != my_name:
    user_name = input("Enter your name: ").strip()
    if user_name == my_name:
        print("Loop stopped because you entered my name!")