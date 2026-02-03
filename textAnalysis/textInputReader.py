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
# with open('textAnalysis/testerCorpus.txt','r') as file:
#     for line in file:
#         sentences.append(line)

### OPTION 2: custom corpus
# THIS IS WHERE TEXT TO BE ANALYSED SHOULD BE INPUTTED
with open('textAnalysis/textInput.txt','r') as file:
    for line in file:
        # print('line:', line)
        sentences.append(line)
#################################################################



################## STEP 2: PICK YOUR FILTER ##################
### OPTION 1: import choice of filter(s) from skippables.py
# from skippables import basicSkippables, skippablesPlusCommonResumeWords, skippablesCommonAndTechResumeWords, skippablesTechAndGovtResumeWords
from skippables import skippablesTechAndGovtResumeWords
chosenLibrary = skippablesTechAndGovtResumeWords

### OPTION 2: import from fillerWords.txt
## NOTE: add one blank line at the end of the file to handle my indexing
# skippables = []
# with open('textAnalysis/fillerWords.txt','r') as file:
#     for line in file:
#         skippables.append(line[:-1])
# chosenLibrary = skippables

### OPTION 3: MANUALLY ENTER ALL SKIP-WORDS IN THE LIST BELOW 'skippablesManual'
# skippablesManual = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 'of', 'as', 'with', 'such', 'etc', 'are', 'is', 'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 'we', 'you', 'they', 'and/or']
# chosenLibrary = skippablesManual
#################################################################



################## STEP 3 (Optional): CHOOSE YOUR TARGET SEARCH WORDS ##################
# add words to the str list 'targetWords'
targetWords = ['issue','posting']
#########################################################################################



################## STEP 4: COMPILE ##################
# Stores the total qunatity of unique instances of a word
storeWords(sentences, chosenLibrary, uniqueWordList, punctuation)
#####################################################


################## STEP 5: CONFIGURE A PRINT OPTION ##################

### OPTION 1: ALL UNIQUE KEYS AND THEIR RESPECTIVE FREQUENCIES
# print('##### ALL UNIQUE KEY WORDS / FREQUENCY #####')
# prettySort(dictionaryReverseSort(uniqueWordList))

### OPTION 2: TOP TEN UNIQUE KEYS
# print('##### TOP TEN HIGHEST FREQUENCY MATCHES #####')
# printTopTenSkills(dictionaryReverseSort(uniqueWordList))

### OPTION 3: PRINT JUST THE UNIQUE WORDS IN A LIST  
# print('##### JUST THE UNIQUE TERMS DISPLAY #####')
# plainListDisplay(dictionaryReverseSort(uniqueWordList))

### OPTION 4: REPORT PRESENCE OF TARGET WORDS
# print('##### TARGET WORD DISPLAY #####')
# searchForTargetWords(uniqueWordList, targetWords)

### OPTION 5: TOP 30 UNIQUE KEYS
print('##### TOP THIRTY HIGHEST FREQUENCY MATCHES #####')
print('(Ordered by freq. starting TopLeft, going Up->Down, then Left->Right)')
printTopThirtySkills(uniqueWordList)
########################################################################