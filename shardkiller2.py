import re
from spellchecker import SpellChecker
import time
import os

spell = SpellChecker()
#opens the txt and stores all of the lines
def openShard(fileName):
    lines=""
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


def openMenu():
    print("\n\n\n============ SHARDKILLER v2.0 ============\n")
    categories = []

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
            categories.append(indexOfCategory)
            indexOfCategory+=1

    #user makes choice of which cateogry to path into
    catChoice = input("\nchoose a category: ")
    catName = ''

    for x in categories:
        match str(catChoice):
            case "1":
                catName = "literature"
            case "2":
                catName = "technology"
            case "3":
                catName = "people_of_NC"
            case "4":
                catName = "Poetry"
            case "5":
                catName = "encrypted"
            case "6":
                catName = "religion_and_philosophy"
            case "7":
                catName = "leaflets"
            case other:
                time.sleep(1)
                print('not recognized')
                time.sleep(1)
                openMenu()
                
        
    currentPath = catName

    #print all shards in the folder
    indexOfShard = 1
    for x in os.listdir(currentPath):
        if ".txt" in x:
            print(str(indexOfShard) + ". " + str(x))
        indexOfShard+=1




    try:
        shardCoice = input("choose a shard: ")
        print()
        fileName = currentPath + "/" + str(os.listdir(currentPath)[(int(shardCoice)-1)])
    except:
        print("-_- ... error occured")
        time.sleep(1)
        print("back to main menu")
        time.sleep(1)


    #now the file gets opened, then ask what command you want to run
    #store the lines, title, and words as seperate variables
    lines = openShard(fileName)
    title = getTitle(lines)
    words = getWords(lines)


    shardText = ""
    for word in words:
        # test the function
        shardText += word + " "

    print(shardText)

    shardTextArray = shardText.split(' ')

    commandChoice = input("\n\nwhat do you want to do? " + "\n \t 1. misspelled words \n \t 2. first letters \n \t 3. b@d finder \n \t 4. sic finder\n")

        

    match commandChoice:
        case "1":
            misspelled = getMisspelledWords(shardTextArray)
            print(misspelled)
            for spelledWord in misspelled:
                try:
                    if len(spelledWord) < 8:
                        print("correction for: " + spelledWord + "\t\t-> " + spell.correction(spelledWord))
                    else:
                        print("correction for: " + spelledWord + "\t-> " + spell.correction(spelledWord))
                except:
                    if "-" in spelledWord:
                        spelledWordArray = spelledWord.split('-')
                        try:
                            for newWord in spelledWordArray:
                                if len(newWord) < 8:
                                    print("correction for: " + newWord + "\t\t-> " + spell.correction(newWord))
                                else:
                                    print("correction for: " + newWord + "\t-> " + spell.correction(newWord))
                        except:
                            print("something went wrong with this word: " + spelledWord)
                            continue
                    continue
        case "2":
            print(getFirstLetters(words))
        case "3":
            print(badFinder(words))
        case "4":
            print(sicFinder(words))
        case _:
            time.sleep(1)
            print('\n\n not recognized')
            time.sleep(1)

    print("\n\ngoing back to menu")
    time.sleep(1)
    openMenu()

openMenu()