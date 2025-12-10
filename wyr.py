import random, csv
from datetime import date

def main():
    path = new_user()
    answers = quiz_handler(quiz())
    store_answers(path, answers)

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
                print(f"Hello {name} by this {id}.\n")
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
    QH = load_questions("Questions/hard.csv")
    QF = load_questions("Questions/funny.csv")
    QC = load_questions("Questions/couple.csv")
    
    Quiz = []

    Quiz.extend(random.sample(QH, 3))
    Quiz.extend(random.sample(QF, 3))
    Quiz.extend(random.sample(QC, 3))

    return Quiz

def load_questions(file_path):
    lines = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append({"one":row[0], "two":row[1].strip()})
    
    return lines

def quiz_handler(quiz):
    answers = []
    for question in range(9):
        print(f"Would you rather {quiz[question]['one']} or {quiz[question]['two']}?")
        answer = input().strip().lower()
        if answer == 'a':
            answers.append(quiz[question]['one'])
        elif answer == 'b':
            answers.append(quiz[question]['two'])
        else:
            print("You must entered only A or B keys on keyboard.")
            answers.append("Null")
    
    return answers

def store_answers(path, answers):
    today = str(date.today())
    with open(path, 'a') as file:
        file.writelines(f"\n{today}\n")
        for row in answers:
            file.writelines(f"{row}\n")

if __name__ == "__main__":
    main()