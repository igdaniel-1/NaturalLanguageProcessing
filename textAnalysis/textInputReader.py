# text reader handler 
# import text to be analysed in textInput.py or use existing testerCorpus.py
# filter out skippable words using either of 2 filters. 
# Either fillerWords.txt or skippables.py depending on how you prefer to enter input.
# Configure which files 


###### STEP 1: INPUT YOUR TEXT
# open the textInput file and read its contents
sentences = []

### OPTION 1: tester corpus
with open('textAnalysis/testerCorpus.txt','r') as file:
    for line in file:
        sentences.append(line)

### OPTION 2: custom corpus
# THIS IS WHERE TEXT TO BE ANALYSED SHOULD BE INPUTTED
# with open('textAnalysis/textInput.txt','r') as file:
#     for line in file:
#         sentences.append(line)




###### STEP 2: PICK YOUR FILTER
### OPTION 1: import choice of filter(s) from skippables.py
# from skippables import basicSkippables, skippablesPlusCommonResumeWords, skippablesCommonAndTechResumeWords, skippablesTechAndGovtResumeWords
from skippables import skippablesTechAndGovtResumeWords
# print('commonResumeWords:',skippablesPlusCommonResumeWords)
chosenLibrary = skippablesTechAndGovtResumeWords

### OPTION 2: import from fillerWords.txt
## NOTE: add one blank line at the end of the file to handle my indexing
# skippables = []
# with open('textAnalysis/fillerWords.txt','r') as file:
#     for line in file:
#         skippables.append(line[:-1])
# chosenLibrary = skippables







###########
# targetWords = []
# these could be words you want to analyse the text for
# they could be tools from your resume you're looking for in a job listing 
# anazlyze the text tfor these words and return their data on top of the other words
# i can also make a 'lite' mode that only anazlyses the frequency of the targetWords and 'ignores' the rest of the text

# I could also make a GUI input for the text/target words

###########




# clean the data
# remove 'filler' words
# skippables = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 'of', 'as', 'with', 'such', 'etc', 'are', 'is', 'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 'we', 'you', 'they', 'and/or']
punctuation = ['.',',','!','?',':', '-']
def trimAndSplitSentence(sentence):
    newSentence = ''
    # remove the trailing blank spaces at the end of a string
    stripped = sentence.strip()
    # remove punctuation 
    if stripped[-1] in punctuation:
        sentence = stripped[:-1]
        return sentence.split()
    return stripped.split()


uniqueWordList = {}

# Store all words in a dictionary 
# count unique instances of words and note the total qunatity of each
for sentence in sentences:
    # this is to resolve an error when a line from the input is blank 
    if sentence == '\n':
        continue
    # trim the ends
    newSentence = trimAndSplitSentence(sentence)
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


######################## NEW CODE BELOW

def dictionaryReverseSort(dictionary):
    # sort dictionary in descending frequency
    sortedDictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sortedDictionary

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
    print('\n### TOP TEN HIGHEST FREQUENCY MATCHES: ')
    count = 0
    for key,value in sortedDict:
        if count > 9: break
        print(key)
        count+=1


###### THESE ARE THE MAIN 3 PRINTING FUNCTIONALITIES
### OPTION 1: ALL UNIQUE KEYS AND THEIR RESPECTIVE FREQUENCIES
prettySort(dictionaryReverseSort(uniqueWordList))

### OPTION 2: TOP TEN UNIQUE KEYS
# printTopTenSkills(dictionaryReverseSort(uniqueWordList))

## OPTION 3: PRINT JUST THE UNIQUE WORDS IN A LIST  
# justKeys = uniqueWordList.keys()
# print('\nJust the keys:', justKeys)