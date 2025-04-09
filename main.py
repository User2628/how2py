# how2py 1.1
# Click Run to begin
# Report issues to User2264 on GitHub

print("Welcome to how2py 1.1!")
input("Press Enter to continue...")
name = input("Before we start, please enter your name: ")
print(f"Hello, {name}!")
input("Press Enter to get started...")

while True:
    print("\n" + "-" * 61)
    print("                   Welcome to how2py 1.1")
    print("-" * 61)
    print(" Choose from the options below (type the word):")
    print("  [LESSONS]   Learn Python step-by-step")
    print("  [ABOUT]     What is how2py?")
    print("  [CREDITS]   Who made this?")
    print("  [GITHUB]    View project on GitHub")
    print("  [CODER]     Info about the developer")
    print("  [QUIT]      Exit the program")
    print("-" * 61)

    choice = input("Your choice: ").strip().upper()

    if choice == "QUIT":
        print("Thanks for using how2py! Goodbye.")
        break

    elif choice == "LESSONS":
        lesson_choice = input("Select a lesson (1–9): ").strip()
        print()

        if lesson_choice == "1":
            print("Lesson 1: Introduction to Python")
            print("Learn about variables, data types, and basic operations.")
            x = 10
            print("Example: x =", x)
        
        elif lesson_choice == "2":
            print("Lesson 2: Control Flow")
            print("Explore if/else conditions and loops.")
            try:
                age = int(input("Enter your age: "))
                print("You are an adult." if age >= 18 else "You are a minor.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif lesson_choice == "3":
            print("Lesson 3: Functions")
            def greet(name):
                return f"Hello, {name}!"
            print(greet("User2264"))
        
        elif lesson_choice == "4":
            print("Lesson 4: Lists and Tuples")
            my_list = [1, 2, 3, 4, 5]
            print("List:", my_list)
            print("First item:", my_list[0])
        
        elif lesson_choice == "5":
            print("Lesson 5: Dictionaries and Sets")
            my_dict = {"name": "Alice", "age": 25}
            print("Dictionary:", my_dict)
            print("Name:", my_dict["name"])
        
        elif lesson_choice == "6":
            print("Lesson 6: File Handling")
            with open("example.txt", "w") as file:
                file.write("Hello, this is how2py lesson 6!")
            print("File 'example.txt' written successfully!")
        
        elif lesson_choice == "7":
            print("Lesson 7: Error Handling")
            try:
                number = int(input("Enter a number: "))
                print("You entered:", number)
            except ValueError:
                print("That's not a valid number!")
        
        elif lesson_choice == "8":
            print("Lesson 8: Object-Oriented Programming")
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age
                def greet(self):
                    return f"Hello, my name is {self.name} and I am {self.age} years old."
            person1 = Person("Bob", 30)
            print(person1.greet())
        
        elif lesson_choice == "9":
            print("Lesson 9: Advanced Topics")
            def count_up_to(max):
                count = 1
                while count <= max:
                    yield count
                    count += 1
            print("Counting up to 5:")
            for number in count_up_to(5):
                print(number)
        
        else:
            print("Invalid lesson number. Please choose 1–9.")
        
        input("\nPress Enter to return to the main menu...")

    elif choice == "ABOUT":
        print("how2py is an interactive Python learning tool designed to teach")
        print("new programmers the basics of Python in a simple and fun way.")
        input("\nPress Enter to return to the main menu...")

    elif choice == "CREDITS":
        print("Developed with 💡 by User2264.")
        input("\nPress Enter to return to the main menu...")

    elif choice == "GITHUB":
        print("Check out the project on GitHub:")
        print("https://github.com/User2264/how2py")
        input("\nPress Enter to return to the main menu...")

    elif choice == "CODER":
        print("Main Coder: User2264")
        print("Follow for more educational projects!")
        input("\nPress Enter to return to the main menu...")

    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to return to the main menu...")
