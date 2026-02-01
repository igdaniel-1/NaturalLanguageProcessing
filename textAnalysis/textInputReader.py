# open the textInput file and read its contents

sentences = []

with open('textAnalysis/textInput.txt','r') as file:
    for line in file:
        sentences.append(line)



# clean the data
# remove 'filler' words
skippables = ['a', 'an', 'the', 'in', 'at', 'on', 'or','and', 'of', 'as', 'with', 'such', 'etc','are','is','was','may','be','maybe','to','from','along', 'we', 'you', 'they','and/or']
punctuation = ['.',',','!']
def trimSentence(sentence):
    newSentence = ''
    # remove the trailing blank spaces at the end of a string
    stripped = sentence.strip()
    # remove punctuation 
    if stripped[-1] in punctuation:
        sentence = stripped[:-1]
        return sentence
    return stripped

sentence = sentences[1]
# for sentence in sentences:
print(sentence)
# print('sentence[-1]:',sentence[:-2])
    # trim the end characters until theres no spaces or punctuation
newSentence = trimSentence(sentence)
print('trimSentence:',newSentence)




# if sentence[:-1] in punctuation:
#     # remove punctuation
#     sentence = sentence[:-1]
#     print('new sentence:', sentence)
