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
    bubbleSort(comptxt)
    total = 0
    for line in comptxt:
        name = nameAndScore(line)[0]
        score = nameAndScore(line)[1]
        print("Name: ",name)
        print("Score: ",score)
        total += int(score)

    print("First Place: "+nameAndScore(comptxt[0])[0]+" with a score of "+str(nameAndScore(comptxt[0])[1]))
    print("Second Place: "+nameAndScore(comptxt[1])[0]+" with a score of "+str(nameAndScore(comptxt[1])[1]))
    print("Third Place: "+nameAndScore(comptxt[2])[0]+" with a score of "+str(nameAndScore(comptxt[2])[1]))
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
    competitor_to_add = name+","+score+"\n"
    f = open("Competitors.csv", "a")
    f.write(competitor_to_add)
    f.close()
    mainMenu()

def searchRecord():
    while True:
        query_type = int(input("Please enter 1 to search name, and 2 to search score"))
        if (query_type == 1) or (query_type == 2):
            break
        else:
            print("Invalid input, please try again.")
    query = input("What is your query?")
    searchWithQuery(query, query_type)

def searchWithQuery(query, query_type):
    has_found = False
    f = open("Competitors.csv", "r")
    comptxt = f.readlines()
    for line in comptxt:
        if nameAndScore(line)[query_type - 1] == query:
            found_item = nameAndScore(line)
            has_found = True
            break
    if has_found:
        print("Item Found!")
        print("Name: ",found_item[0])
        print("Score: ",found_item[1])
        mainMenu()
    else:
        print("No item found. Try putting in a more precise query.")
        searchRecord()
    f.close()

def bubbleSort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1):
            if int(nameAndScore(list_to_sort[j])[1]) > int(nameAndScore(list_to_sort[j+1])[1]):
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

mainMenu()
