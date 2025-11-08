def main():
    print(user())

def user():
    name = input("What's your name: ")
    birth = input("Enter your birth date: ")
    gen = input("If you're Male enter 'M' or not enter 'F': ")

    return name, birth, gen

if __name__ == "__main__":
    main()