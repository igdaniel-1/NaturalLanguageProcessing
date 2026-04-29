# Text Analysis Program
# A light-weight NLP program to analyze the content of a job description for key words to include on your resume.
# Import text, filter out skippable words, and return word usage data.

from columnPrint import col_print
from functions import storeWords,trimAndSplitSentence,dictionaryReverseSort,plainListDisplay,prettySort,printTopTenSkills,printTopThirtySkills,searchForTargetWords

sentences = []
punctuation = ['.',',','!','?',':', '-','"']
uniqueWordList = {}

################## STEP 1: INPUT YOUR TEXT ##################
### OPTION 1: tester corpus
# with open('textAnalysis/corpora/testerCorpus.txt','r') as file:
#     for line in file:
#         sentences.append(line)

### OPTION 2: custom corpus
# THIS IS WHERE TEXT TO BE ANALYSED SHOULD BE INPUTTED
with open('textAnalysis/corpora/textInput.txt','r') as file:
    for line in file:
        sentences.append(line)
#################################################################



################## STEP 2: PICK YOUR FILTER ##################
### OPTION 1: import choice of filter(s) from corpora/skippables.py
# options include: basicSkippables, skippablesPlusCommonResumeWords, skippablesCommonAndTechResumeWords, skippablesTechAndGovtResumeWords, skippablesAerospaceWords
from corpora.skippables import *

# text input header
print("\n\n\n\n\n#################################################################")
print("\nJob Application Filter \n")
print("#################################################################")
print("\nFIRST TIME USERS: \n Before beginning, " \
"locate the file corpora/textInput.txt." \
"\n Paste text of the document in this file.\n")
print("#################################################################\n \n")



print("Which Filter would you like to apply to your document:")
print(" basic \n resume \n tech \n govt \n aerospace")
filterChoice = input("Selection:")
if filterChoice == 'basic':
    chosenLibrary = basicSkippables
if filterChoice == 'resume':
    chosenLibrary = skippablesPlusCommonResumeWords
if filterChoice == 'tech':
    chosenLibrary = skippablesCommonAndTechResumeWords
if filterChoice == 'govt':
    chosenLibrary = skippablesTechAndGovtResumeWords
if filterChoice == 'aerospace':
    chosenLibrary = skippablesAerospaceWords
else:
    # default is basic
    chosenLibrary = basicSkippables

### OPTION 2: import from fillerWords.txt
## NOTE: add one blank line at the end of the file to handle my indexing
# skippables = []
# with open('textAnalysis/corpora/fillerWords.txt','r') as file:
#     for line in file:
#         skippables.append(line[:-1])
# chosenLibrary = skippables

### OPTION 3: MANUALLY ENTER ALL SKIP-WORDS IN THE LIST BELOW 'skippablesManual'
# skippablesManual = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 'of', 'as', 'with', 'such', 'etc', 'are', 'is', 'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 'we', 'you', 'they', 'and/or']
# chosenLibrary = skippablesManual
#################################################################



################## STEP 3 (Optional): CHOOSE YOUR TARGET SEARCH WORDS ##################
# ADDITIONAL TARGET WORD FILTER OPTIONS
# You can add more target word lists in this section, mirroring the list format for 'aerospaceTargetWords'
aerospaceTargetWords = ['simulation','simulator', 'simulators', 'modeling','Python','C','training','train','team']
defaultTargetWords = ['issue','posting']

# Add to the list of targetWords or choose a prebuilt list above
targetWords = []
# targetWords = ['software','developer']
# targetWords = defaultTargetWords

# input version
filterYesNo = input("\n(Optional) Would you like to select specific target words to filter for? (Y/N)")
if filterYesNo == 'Y':
    filterWordsInput = input("Enter the target words seperated by spaces: ")
    print("Is this list correct? \n", filterWordsInput)
    continueTargetYesNo = input("(Y/N): ")
    if continueTargetYesNo == "N":
        print("Restart and try again. Remember to seperate with spaces like the following example:")
        print("Example: software developer Python JavaScript")
    elif continueTargetYesNo == "Y":
        targetWords = filterWordsInput.split()
        
#########################################################################################



################## STEP 4: COMPILE ##################
# Stores the total qunatity of unique instances of a word
storeWords(sentences, chosenLibrary, uniqueWordList, punctuation)
#####################################################


################## STEP 5: CONFIGURE A PRINT OPTION ##################
print("\nSelect one of the following output print options:")
print("OPTION 1: ALL UNIQUE KEYS AND THEIR RESPECTIVE FREQUENCIES")
print("OPTION 2: TOP TEN UNIQUE KEYS")
print("OPTION 3: PRINT JUST THE UNIQUE WORDS IN A LIST")
print("OPTION 4: REPORT PRESENCE OF TARGET WORDS")
print("OPTION 5: TOP 30 UNIQUE KEYS")
printSelection = input("Selection (#):")

if printSelection == "1":
    print('\n##### ALL UNIQUE KEY WORDS / FREQUENCY #####')
    prettySort(dictionaryReverseSort(uniqueWordList))
elif printSelection == "2":
    print('\n##### TOP TEN HIGHEST FREQUENCY MATCHES #####')
    printTopTenSkills(dictionaryReverseSort(uniqueWordList))
elif printSelection == "3":
    print('\n##### JUST THE UNIQUE TERMS DISPLAY #####')
    plainListDisplay(dictionaryReverseSort(uniqueWordList))
elif printSelection == "4":
    print('\n##### TARGET WORD DISPLAY #####')
    searchForTargetWords(uniqueWordList, targetWords)
elif printSelection == "5":
    print('\n##### TOP THIRTY HIGHEST FREQUENCY MATCHES #####')
    print('(Ordered by freq. starting TopLeft, going Up->Down, then Left->Right)')
    printTopThirtySkills(uniqueWordList)
else:
    print("Please input a number between 1 and 5.")
########################################################################