from tkinter import Tk     # little bit of GUI code for the file handling
from tkinter.filedialog import askopenfilename

Tk().withdraw()

def mainMenu(): #Main menu of the database that the user is sent to upon load, and after an operation has finised.
    print("Race Database")
    print("*************")
    print("1 - View All")
    print("2 - Add Record")
    print("3 - Search Record")
    print("4 - Create/Change Race File")
    print("5 - Exit")
    option = int(input("Please make your selection"))
    if option == 1: #Optimisation here is grim. I miss switch statements. As far as I know theres no easy way of doing this without going all in tkinter.
        viewAll()
    elif option == 2:
        addRecord()
    elif option == 3:
        searchRecord()
    elif option == 4:
        fileChanger()
    elif option == 5:
        print("Exiting...")
    else:
        print("Invalid Operation")
        mainMenu() #Fancy self referential function.

def viewAll():
    f = open(fileDir, "r") #opens the file
    comptxt = f.readlines()
    bubbleSort(comptxt) #sorts the array containing the file's data
    total = 0 #Initialises total to zero
    for line in comptxt:
        print(nameAndScore(line)[0]+ "with a score of "+str(nameAndScore(line)[1])) #this function pretty much is the entire reason my code works, and at a nice number of lines.
        total += int(nameAndScore(line)[1])
        #Total used to calculate the average time.
    print("First Place: "+nameAndScore(comptxt[0])[0]+" with a score of "+str(nameAndScore(comptxt[0])[1])) #This could probably be less ugly. Making big arrays of strings is agonising though and I don't want to do it.
    print("Second Place: "+nameAndScore(comptxt[1])[0]+" with a score of "+str(nameAndScore(comptxt[1])[1]))
    print("Third Place: "+nameAndScore(comptxt[2])[0]+" with a score of "+str(nameAndScore(comptxt[2])[1]))
    print("Average Time: "+str(total/len(comptxt))) #Average time calc as mentioned earlier.
    f.close() #close the file and return the user to the main menu.
    mainMenu()

def nameAndScore(line): #nameAndScore() <3. I love this function, it makes my life so much easier. It takes a line from the original document in the format of x,y and turns it into an array with the values [str(x), str(y)].
    name = "" #Initialise variables of name and score, as we will be appending to them later.
    score = ""
    for letter in range(0, len(line)):
        if line[letter] != ",": #as long as the letter in the name is not a comma, continue to iterate the appending to the name. The comma will designate the next value and therefore change into the score.
            name += line[letter]
        else: #as we know the comma designates the next value we break the loop
            nameEndIndex = letter
            break
    for letter in range(nameEndIndex + 1, len(line)): #now, for each value towards the end of the array, we add this to the score. Simple, but it saves a lot of headache when in a function.
        score += line[letter]
    return [name, score]

def addRecord():
    name = input("Please enter the competitor's name")
    score = input("Please enter the competitor's score")
    competitor_to_add = name+","+score+"\n" #only really interesting part of this procedure. This statements makes the line readable to a .csv reader.
    f = open(fileDir, "a")
    f.write(competitor_to_add)
    f.close()
    mainMenu() #simple. I like this part because it doesn't make my eyes bleed like the rest of this file.

def searchRecord():
    while True:
        query_type = int(input("Please enter 1 to search name, and 2 to search score")) #I guess I *could* make it recognise that any float must be a score and any string must be a name. Maybe in version 1.1...
        if (query_type == 1) or (query_type == 2):
            break
        else: #Trying my best to make the code idiot proof... We loop until the user gets it right.
            print("Invalid input, please try again.")
    query = input("What is your query?")
    searchWithQuery(query, query_type) #The actual guts of this procedure.

def searchWithQuery(query, query_type): #Now this could be a function, and I could have it return a value to be printed. But then I might as well just split this entire script into a GUI and a library.
    has_found = False #Very important. Used to retry the query process. Once again, making the code idiot proof.
    f = open(fileDir, "r") #opens the file. This is soooooo easy thanks to tkinter's open file window.
    comptxt = f.readlines()
    for line in comptxt: #searches every line, checks if its the same. Because this is unsorted I can't use a Binary search, but the array should be so small that it would only make a significant difference on early 90s hardware.
        if nameAndScore(line)[query_type - 1] == query: #if we found the relevant item in the directory...
            found_item = nameAndScore(line) #prepare to print!
            has_found = True #set to true to display "was true" and end the loop of searching.
            break #break the for loop as there is no need, unless the very rare occassion of individuals having exactly the same name. You can use http://howmanyofme.com/ to find out if anyone shares the same name as you :D
    if has_found: #woo! we found it. Now to print it
        print("Item Found!")
        print("Name: ",found_item[0])
        print("Score: ",found_item[1])
        mainMenu()
    else:
        print("No item found. Try putting in a more precise query.") #failed, so we repeat and tell the user to stop being dumb. I think it would be possible to make it search for similar names, (i.e slowly identify possible candidates by starting letter.
        searchRecord() #back to the start :(
    f.close() #close the file as we don't need it anymore

def bubbleSort(list_to_sort): #Used in my viewAll() procedure. Specialised, as it sorts the list in ascending order so the user can easily see the leaderboard. If only I was actually making a GUI...
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1):
            if int(nameAndScore(list_to_sort[j])[1]) > int(nameAndScore(list_to_sort[j+1])[1]):
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

def fileChanger(): #procedure to change the file. Opens a file browser so the user can select their file. Really satisfying, no more idiot users. Unless they click on the wrong file, in which case, GIGO.
    global fileDir
    fileDir = askopenfilename()
    print("File Directory changed to "+fileDir)
    mainMenu()
fileDir = "Competitors.csv"
mainMenu()
