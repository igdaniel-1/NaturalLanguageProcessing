# open the textInput file and read its contents
sentences = []

with open('textAnalysis/textInput.txt','r') as file:
    for line in file:
        sentences.append(line)

###########
# targetWords = []
# these could be words you want to analyze the text for
# they could be tools from your resume you're looking for in a job listing 
# anazlyze the text tfor these words and return their data on top of the other words
# i can also make a 'lite' mode that only anazlyses the frequency of the targetWords and 'ignores' the rest of the text
###########




# clean the data
# remove 'filler' words
skippables = []
with open('textAnalysis/fillerWords.txt','r') as file:
    for line in file:
        skippables.append(line)

punctuation = ['.',',','!','?',':']
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
    # trim the ends
    newSentence = trimAndSplitSentence(sentence)
    print('newSentence',newSentence)
    # remove filler words
    for word in newSentence:
        if word in skippables:
            continue
            # print('testing filler:', word)
        elif word in uniqueWordList.keys():
            uniqueWordList[word] += 1
            # print('testing match:', word)
        else:
            # create new entry
            uniqueWordList[word] = 1
            # print('testing unique:', word)


print(uniqueWordList)

