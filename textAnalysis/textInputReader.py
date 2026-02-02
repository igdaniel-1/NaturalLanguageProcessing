# open the textInput file and read its contents
sentences = []

# tester corpus
with open('textAnalysis/testerCorpus.txt','r') as file:
    for line in file:
        sentences.append(line)

# active corpus
# THIS IS WHERE INPUT SHOUL BE FED
# with open('textAnalysis/textInput.txt','r') as file:
#     for line in file:
#         sentences.append(line)

###########
# targetWords = []
# these could be words you want to analyze the text for
# they could be tools from your resume you're looking for in a job listing 
# anazlyze the text tfor these words and return their data on top of the other words
# i can also make a 'lite' mode that only anazlyses the frequency of the targetWords and 'ignores' the rest of the text

# I could also make a GUI input for the text/target words

###########




# clean the data
# remove 'filler' words
skippables = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 'of', 'as', 'with', 'such', 'etc', 'are', 'is', 'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 'we', 'you', 'they', 'and/or']
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
        # print('\nempty sentence:::',sentence)
        continue
    # trim the ends
    # print('\nsentence:::',sentence)
    newSentence = trimAndSplitSentence(sentence)
    # remove filler words
    for word in newSentence:
        if word in skippables:
            continue
        elif word in uniqueWordList.keys():
            uniqueWordList[word] += 1
        else:
            # create new entry
            uniqueWordList[word] = 1


######################## NEW CODE BELOW

def dictionarySortingDisplay(dictionary):

    # sort dictionary in descending frequency
    sortedDictionary = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)


    return sortedDictionary

# print(uniqueWordList) 
print('\n\nsorted:',dictionarySortingDisplay(uniqueWordList)) 