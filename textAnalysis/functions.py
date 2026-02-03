from columnPrint import col_print

def storeWords(sentences, chosenLibrary, uniqueWordList, punctuation):
    for sentence in sentences:
        # this is to resolve an error when a line from the input is blank 
        if sentence == '\n':
            continue
        # trim the ends
        newSentence = trimAndSplitSentence(sentence, punctuation)
        # remove filler words
        for word in newSentence:
            # remove any punctuation at the end of the word
            if word[-1] in punctuation:
                word = word[:-1]

            # NOTE: TO CHANGE FILTER USED FROM 'skippables.py', CHANGE 'skippables' TO 'library name, e.g.skippablesPlusCommonResumeWords'
            # if word in skippables:
            if word in chosenLibrary:
                continue
            elif word in uniqueWordList.keys():
                uniqueWordList[word] += 1
            else:
                # create new entry
                uniqueWordList[word] = 1

def trimAndSplitSentence(sentence, punctuation):
    newSentence = ''
    # remove the trailing blank spaces at the end of a string
    stripped = sentence.strip()
    # remove punctuation 
    if stripped[-1] in punctuation:
        sentence = stripped[:-1]
        return sentence.split()
    return stripped.split()

def dictionaryReverseSort(dictionary):
    # sort dictionary in descending frequency
    sortedDictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sortedDictionary

def plainListDisplay(sortedDict):
    plainList = []
    for key,value in sortedDict:
        plainList.append(key)
    # choose column count for display
    lengthList = len(plainList)
    if lengthList < 30:
        columnNumber = 4
    elif lengthList< 140:
        columnNumber = 5
    elif lengthList< 180:
        columnNumber = 6
    elif lengthList< 220:
        columnNumber = 7
    elif lengthList< 240:
        columnNumber = 8
    else:
        columnNumber = 9
    col_print(plainList, columnCount=columnNumber)

    

def prettySort(sortedDict):
    # pretty print the dictionary with row numbers and frequencies
    row_number = 1
    for key,value in sortedDict:
        if len(key) < 4:
            print(row_number,key, '\t\t\t------', value)
        elif len(key) > 11:
            print(row_number,key, '\t------', value)
        else:
            print(row_number,key, '\t\t------', value)
        row_number+=1

def printTopTenSkills(sortedDict):
    count = 0
    for key,value in sortedDict:
        if count > 9: break
        print(key)
        count+=1

def printTopThirtySkills(sortedDict):
    reversedDict30 = dictionaryReverseSort(sortedDict)[:30]
    plainListDisplay(reversedDict30)
# def printTopThirtySkills(sortedDict):
#     reversedDict30 = dictionaryReverseSort(uniqueWordList)[:30]
#     plainListDisplay(reversedDict30)

def searchForTargetWords(dictionary, targetWords):
    print('WORD','\t','FREQUENCY')
    for word in targetWords:
        if word in dictionary:
            if len(word) >7:
                print(word, '\t',dictionary[word])
            else:
                print(word, '\t\t',dictionary[word])