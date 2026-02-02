# Text Analysis Program
A light-weight NLP program to analyze the content of a job description for key words to include on your resume.

## Instructions
1. Input

Enter input text in: 'textAnalysis/textInput.txt'

2. Filter

Pick which 'skippable-words' filter you would like. In 'skippables.py', select which of the filter lists you would like to remove from your results, e.g. 'basicSkippables'. 

In textInputReader.py, navigate to the line that begins with:

```from skippables import ...```

...and substitute '...' with the list name from skippables.py. e.g.:

```from skippables import skippablesPlusCommonResumeWords```

3. (Optional) Search By Target Words

In textInputReady.py, change the targetWords list variabel to include your key words.

At the bottom of the same file, uncomment out the two lines under printing functionality 'OPTION 4' to return frequency of target words in the inputted text.

4. Run

Execute 'textAnalysis/textInputReader.py'

## Additional Usage 
Search description for keywords:

Use the 'targetWords' list that has been commented out in the textInputReader.py file. Enter your target words in 'targetWords' matching the syntax of the 'skippables' list in 'textAnalysis/skippables.py'. 

Ideas:
These target words can be your current job skills (if you're seeking a job tailored to your exact skillset), or you could analyze the frequency with which a certain tool is used to measure its potential industry value if you learned it.