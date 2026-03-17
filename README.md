# AI Language Assistant

Finds industry-specific keywords in a document.

Filters can be applied to return highlighted keywords from a specific category, sifting out industry jargon and returning targetted insights on word usage data.


## Usage - Resume / Job Description Matcher
You can check how qualified you are for a job using this tool. 

This was designed as a hiring tool, ingesting a text to return featured topics. This can be applied to job descriptions as well as resumes. 

Using the "Execution Instructions" below, a keyword list can be generated for both the job description and a resume. By cross-referencing the list of keywords in the job description with that of the resume, one can see if the resume experience is a match for the job posting.

This tool can be used by recruiters and applicants alike to match people to their dream jobs!



## Execution Instructions
1. Input

Enter input text in: 'textAnalysis/textInput.txt'

2. Filter

Pick which 'skippable-words' filter you would like. In 'skippables.py', select which of the filter lists you would like to remove from your results, e.g. 'skippablesPlusCommonResumeWords'. 

In textInputReader.py, navigate to the line that begins with:

```from skippables import ...```

...and substitute '...' with the list name from 'skippables.py'. e.g.:

```from skippables import skippablesPlusCommonResumeWords```

3. (Optional) Search By Target Words

In 'textInputReader.py', change the 'targetWords' list to include your key words. e.g.:

```
targetWords = ['software','developer']
```

At the bottom of 'textInputReader.py', uncomment-out the two lines under printing functionality 'OPTION 4: REPORT PRESENCE OF TARGET WORDS' to return frequency of target words in the inputted text.

4. Configure a Print Option
At the bottom of 'textInputReader.py', navigate to where it reads "MAIN PRINTING FUNCTIONALITIES".
Read the available options and uncomment-out those which you wish to see.

For example, OPTION 1 is represented as:

```
### OPTION 1: ALL UNIQUE KEYS AND THEIR RESPECTIVE FREQUENCIES
print('##### ALL UNIQUE KEY WORDS / FREQUENCY #####')
prettySort(dictionaryReverseSort(uniqueWordList))
```


5. Run

```
python3 'textAnalysis/textInputReader.py'
```


### Training Data
The model is made more precise with the filters located in 'skippables.py'. To refine the model for your own use, consider adding a new filter or ammending mine for your needs.