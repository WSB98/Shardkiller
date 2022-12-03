#SHARD_KILLERv1


from spellchecker import SpellChecker
import time
import os

spell = SpellChecker()
#opens the txt and stores all of the lines
def openShard(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines()
    return lines

#extracts title from the txt
def getTitle(lines):
    title = lines[0]
    return title

#extracts all words from the txt and appends them in an array, splitting each sentence by spaces
def getWords(lines):
    lineNumber = 0
    wordArray = []
    for x in lines:
        if lineNumber == 0:
            title = str(x)
        else:
            words = x.split(' ')
            
            tempArray = []
            for x in words:

                #more splits for punctuation that shows up as misspellings per pyspellchecker
                
                if "\"" in x:
                    splitWord = x.split("\"")
                    for j in splitWord:
                        tempArray.append(j)
                elif "." in x:
                    splitWord = x.split(".")
                    for j in splitWord:
                        tempArray.append(j)
                elif "," in x:
                    splitWord = x.split(",")
                    for j in splitWord:
                        tempArray.append(j)
                elif "!" in x:
                    splitWord = x.split("!")
                    for j in splitWord:
                        tempArray.append(j)
                elif "?" in x:
                    splitWord = x.split("?")
                    for j in splitWord:
                        tempArray.append(j)
                elif ":" in x:
                    splitWord = x.split(":")
                    for j in splitWord:
                        tempArray.append(j)
                elif "(" in x:
                    splitWord = x.split("(")
                    for j in splitWord:
                        tempArray.append(j)
                elif ")" in x:
                    splitWord = x.split(")")
                    for j in splitWord:
                        tempArray.append(j)
                elif "\n" in x:
                    splitWord = x.split("\n")
                    for j in splitWord:
                        tempArray.append(j)
                elif ";" in x:
                    splitWord = x.split(";")
                    for j in splitWord:
                        tempArray.append(j)
                elif "[" in x:
                    splitWord = x.split("[")
                    for j in splitWord:
                        tempArray.append(j)
                elif "]" in x:
                    splitWord = x.split("]")
                    for j in splitWord:
                        tempArray.append(j)
                else:
                    tempArray.append(x)
                
            for w in tempArray:
                if "." == w:
                    continue
                elif "," == w:
                    continue
                elif "?" == w:
                    continue
                elif "!" == w:
                    continue
                elif "\"" == w:
                    continue
                elif '' == w:
                    continue
                elif ":" == w:
                    continue
                elif "(" == w:
                    continue
                elif ")" == w:
                    continue
                elif "\n" == w:
                    continue
                elif ";" == w:
                    continue
                elif "[" == w:
                    continue
                elif "]" == w:
                    continue
                else:
                    wordArray.append(w)

                
        lineNumber += 1
    return wordArray

#gets the first letters from every word in wordArray. stores them in their own array
def getFirstLetters(words):
    firstLetterList = []
    for x in words:
        firstLetter = x[0]
        firstLetterList.append(firstLetter)

    return firstLetterList

#gets the last letters from every word in wordArray. stores them in their own array
def getLastLetters(words):
    lastLetterList = []
    for x in words:
        wordLength = len(x)
        lastLetter = x[wordLength-1]
        lastLetterList.append(lastLetter)

    return lastLetterList

#get misspelled words
def getMisspelledWords(words):
    wrongWords = spell.unknown(words)

    return wrongWords

#[sic] finder -- just finding prompted misspellings
def sicFinder(lines):
    sics = []

    for x in lines:
        tempArray = x.split(' ')
        for j in tempArray:
            if "[sic]" in j:
                sics.append(j)

    return sics

#B@D finder
def badFinder(words):
    #set variable for b@d's found
    bads = []
    tracker = 0
    #look through words to find when an @ symbol is mentioned
    for x in words:
        if "@" in x:
            #if the @ symbol is the first word, get the 3 words after it, and store in array
            if tracker == 0:
                word1 = x
                word2 = words[tracker+1]
                word3 = words[tracker+2]
                word4 = words[tracker+3]
                appendState = str(word1+' '+word2+' '+word3+' '+word4+'...')
                bads.append(appendState)
            #if the @ symbol is mentioned anywhere else, get the word before and fter and store in the array
            else:
                word1 = words[tracker-1]
                word2 = str(x)
                word3 = words[tracker+1]
                word4 = words[tracker+2]
                appendState = str(word1+' '+word2+' '+word3+' '+word4+'...')
                bads.append(appendState)
        #iterate the tracker each time through the if loop
        tracker+=1
    return bads

#mainloop menu for the user to select shards and command
def openMenu():
    print("\n\n\n============ SHARDKILLER v1.0 ============\n")

    #print all of the categories in the shards folder
    indexOfCategory = 1
    for j in os.listdir(os.curdir):
        if ".py" in j:
            continue
        elif ".DS" in j:
            continue
        elif ".git" in j:
            continue
        elif ".md" in j:
            continue
        else:
            print(str(indexOfCategory) + ". " + str(j))
            indexOfCategory+=1

    #user makes choice of which cateogry to path into
    catChoice = input("\nchoose a category: ")

    #religion and philosophy
    if(catChoice == "6"):
        print()
        currentPath = "religion_and_philosophy"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        
        print()
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()


        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "4":
        print()
        currentPath = "Poetry"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()

        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "5":
        print()
        currentPath = "encrypted"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()
        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "7":
        print()
        currentPath = "leaflets"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()

        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "3":
        print()
        currentPath = "people_of_NC"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()

        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "2":
        print()
        currentPath = "technology"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()

        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
    elif catChoice == "1":
        print()
        currentPath = "literature"

        #print all shards in the folder
        indexOfShard = 1
        for x in os.listdir(currentPath):
            if ".txt" in x:
                print(str(indexOfShard) + ". " + str(x))
            indexOfShard+=1
        print()


        #gather the choice and create filename based on choice
        try:
            relAndPhilChoice = input("choose a shard: ")
            print()
            fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(relAndPhilChoice)-1)])
        except:
            print("-_- ... error occured")
            time.sleep(1)
            print("back to main menu")
            time.sleep(1)
            openMenu()

        #now the file gets opened, then ask what command you want to run
        #store the lines, title, and words as seperate variables
        lines = openShard(fileName)
        title = getTitle(lines)
        words = getWords(lines)


        #show commands, and run command
        print("0. RAW PRINT")
        print("1. get FIRST letter of each word")
        print("2. get LAST letter of each word")
        print("3. get MISSPELLED words")
        print("4. get ALL [SIC]s")
        print("5. get ALL B@Ds")
        
        print()

        relAndPhilCommand = input("choose a command: ")
        print()

        if relAndPhilCommand == "1":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getFirstLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "2":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print(getLastLetters(words))
            print()
            openMenu()
        elif relAndPhilCommand == "3":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            wrongWords = getMisspelledWords(words)
            for i in wrongWords:
                print(str(i) + " -- possible correction: " + str(spell.correction(i)))
            print()
            openMenu()
        elif relAndPhilCommand == "4":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allSics = sicFinder(lines)
            for i in allSics:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "5":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            allBads = badFinder(words)
            for i in allBads:
                print(i)
            print()
            openMenu()
        elif relAndPhilCommand == "0":
            print("working...")
            time.sleep(1)
            print(title)
            time.sleep(1)
            print()
            for x in lines:
                print(x)
            openMenu()
        else:
            print("error -_- ...")
            time.sleep(1)
            print("going back to start, please enter a listed command")
            time.sleep(1)
            openMenu()
        
    else:
        print("error -_- ...")
        time.sleep(1)
        print("back to main menu")
        time.sleep(1)

        openMenu()
    

        


openMenu()



    



