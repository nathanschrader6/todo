import os
#Functions
def menu():
    print("1: view tasks")
    print("2: Add task")
    print("3: Remove task")
    print("4: Star/Unstar task")
    print("E: Exit")


def view(names, star):
    print("Tasks: ")
    count = 0
    for i in names:
        print(count, " ", star[count], " ", names[count])
        count = count + 1


def add(names, star):
    print("Add task")
    names.append( input("Task data: "))
    valid = False
    while not valid:
        shouldstar = (input("Star: Y/N"))
        if shouldstar == 'y' or shouldstar == 'Y':
            star.append("*")
            valid = True
        elif shouldstar == 'n' or shouldstar == 'N':
            star.append("-")
            valid = True
        else:
            print("Invalid Selection: ")
        save(names, star)

def remove(names, star):
    view(names, star)
    removeID = int(input("Enter the task number to be deleted: "))
    del names[removeID]
    del star[removeID]
    save(names, star)


def startask(names, star):
    view(names, star)
    starID = input("Enter the task number to change star status: ")
    if star[starID] == '-':
        star[starID] = '*'
    else:
        star[starID] = '-'
    save(names, star)

def getdata(names, star):
    p = open('tasks.txt')
    line = p.readline()
    while line:
        star.append(line.rstrip('\n'))
        line = p.readline()
        names.append(line.rstrip('\n'))
        line = p.readline()


def save(names, star):
    p = open('tasks.txt', 'w')
    counter = 0
    for i in names:
        p.write(star[counter])
        p.write('\n')
        p.write(names[counter])
        p.write('\n')
        counter = counter + 1

names = []
star = []
getdata(names, star)
menu()
choice = input("Enter Selection: ")
while choice != 'E' and choice != 'e':
    os.system('cls')
    if choice == '1':
        view(names, star)
    elif choice == '2':
        add(names, star)
    elif choice == '3':
        remove(names, star)
    elif choice == '4':
        startask(names, star)
    else:
        print("Invalid Selection")
    menu()
    choice = input("Enter Selection: ")

