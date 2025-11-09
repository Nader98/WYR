import random
from datetime import date

def main():
    file, gender = user()

def user():
    today = str(date.today())
    
    try:
        name = input("What's your name: ")
        if len(name) < 3:
            print("Invalid name input")
            raise ValueError
        
        if not name[0:2].isalpha():
            print("Your name can not begin with a number")
            raise ValueError

        birth = input("Enter your birth date: ")
        if not birth.isnumeric():
            print("Your birth date must be a number")
            raise ValueError
        
        if len(birth) != 4:
            print("You must enter a 4-digit birth date")
            raise ValueError

        gen = input("If you're Male enter 'M' or not enter 'F': ").strip().upper()
        id = random.randrange(1000, 2000)

        # Append user's informations to users.csv
        with open("Users/users.csv", 'a') as file:
            file.writelines(f"{name}, {birth}, {gen}, {id}\n")

        user_file = "Users/" + str(id).strip() + ".csv"

        # Create a file to store user answers
        with open(user_file, 'w') as file:
            file.writelines(f'{today}\n')

        return user_file, gen

    except ValueError:
        pass


if __name__ == "__main__":
    main()