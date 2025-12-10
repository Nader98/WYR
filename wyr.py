import random, csv

def main():
    path = new_user()
    answers = quiz_handler(quiz())
    result(path, answers)

def new_user():
    while True:
        try:
            name = input("What's your name? ").strip()
            if not name[0:2].isalpha():
                print("Name should to beginning by character!")
                raise ValueError
                
            if len(name) < 3:
                print(f"{name} is too short! Name should be at least 3 characters")
                raise ValueError
                
            id = find_user(name)
            if id:
                print(f"Hello {name} by this {id}.")
                return f"Users/{id}.csv"
                
            elif id == None:
                age = input("How old are you? ").strip()
                
                if not age.isdigit():
                    print(f"{age} is invalid! You should entered digit.")
                    raise ValueError
                    
                if len(age) != 4:
                    print("Birth date length is 4 digit, and greater '1900'!")
                    raise ValueError
                
                sex = input("Tell me your gender('M' or 'F'). ").strip().upper()
                if sex == 'M' or sex == 'F':
                    id = save_user(name, age, sex)
                    return f"Users/{id}.csv"
                else:
                    print(sex)
                    print("Just enter M as Male or F as Female.")
                    raise ValueError

        except ValueError:
            pass
        

def find_user(name):
    users_list = []
    with open("Users/users.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            users_list.append({'id': row[0], 'name': row[1].strip(), 'birth': row[2].strip(), 'sex': row[3].strip()})
        
    for user in users_list:
        if name == user['name']:
            return user['id']

def save_user(name, age, sex):
    id = random.randint(1000, 2000)
    
    with open("Users/users.csv", 'a') as file:
        file.writelines(f"{id}, {name}, {age}, {sex}\n")
    
    print(f"Welcome dear {name} to our quiz game!\n")
    return id
    
def quiz():
    lines = []
    with open("Questions/question.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append({"one":row[0], "two":row[1].strip()})
    
    return lines

def quiz_handler(lines):
    answers = []
    for line in range(len(lines)):
        print(f"Would you rather {lines[line]['one']} or {lines[line]['two']}?")
        answer = input().strip().lower()
        if answer == 'a':
            answers.append(lines[line]['one'])
        elif answer == 'b':
            answers.append(lines[line]['two'])
        else:
            print("You must entered only A or B keys on keyboard.")
            answers.append("Null")
    
    return answers

def result(path, answers):
    with open(path, 'a') as file:
        for row in answers:
            file.writelines(f"{row}\n")

if __name__ == "__main__":
    main()