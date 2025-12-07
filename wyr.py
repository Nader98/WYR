import random, csv

def main():
    path = user()
    answers = quiz_handler(quiz())
    result(path, answers)

def user():
    name = input("What's your name? ")
    age = input("How old are you? ")
    gen = input("Tell me your gender? ")
    id = random.randint(1000, 2000)

    with open("Users/users.csv", 'a') as file:
        file.writelines(f"{id}, {name}, {age}, {gen}\n")

    return f"Users/{id}.csv"
    
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