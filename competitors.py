def mainMenu():
    print("Race Database")
    print("*************")
    print("1 - View All")
    print("2 - Add Record")
    print("3 - Search Record")
    print("4 - Exit")
    option = int(input("Please make your selection"))
    if option == 1: #Optimisation here is grim. I miss switch statements.
        viewAll()
    elif option == 2:
        addRecord()
    elif option == 3:
        searchRecord()
    elif option == 4:
        print("Exiting...")
    else:
        print("Invalid Operation")
        mainMenu() #Fancy self referential function.

def viewAll():
    f = open("competitors.csv", "r")
    comptxt = f.readlines()
    first = 32766
    first_name = ""
    second = 0
    second_name = ""
    third = 0
    third_name = ""
    total = 0
    average = 0
    for line in comptxt:
        name = nameAndScore(line)[0]
        score = nameAndScore(line)[1]
        print("Name: ",name)
        print("Score: ",score)
        total += int(score)
        if int(score) < first:
            third = second
            third_name = second_name
            second = first
            second_name = first_name
            first = int(score)
            first_name = name
    print("First Place: "+first_name+" with a time of "+str(first))
    print("Second Place: "+second_name+" with a time of "+str(second))
    print("Third Place: "+third_name+" with a time of "+str(third))
    print("Average Time: "+str(total/len(comptxt)))
    f.close()
    mainMenu()

def nameAndScore(line):
    name = ""
    score = ""
    word_not_found = True
    for letter in range(0, len(line)):
        if line[letter] != ",":
            name += line[letter]
        else:
            nameEndIndex = letter
            break
    for letter in range(nameEndIndex + 1, len(line)):
        score += line[letter]
    return [name, score]

def addRecord():
    name = input("Please enter the competitor's name")
    score = input("Please enter the competitor's score")
    competitor_to_add = name+","+score
    f = open("Competitors.csv", "a")
    f.write(competitor_to_add)
    f.close()
    mainMenu()

def searchRecord():
    while True:
        query_type = int(input("Please enter 1 to search name, and 2 to search score"))
        if query_type == (1 or 2):
            break
        else:
            print("Invalid input, please try again.")

mainMenu()
