def main():
    print(user())

def user():
    name = input("What's your name? ")
    age = input("How old are you? ")
    gen = input("Tell me your gender? ")

    with open("Users/users.csv", 'a') as file:
        file.writelines(f"{name}, {age}, {gen}\n")

    return name, age, gen

if __name__ == "__main__":
    main()