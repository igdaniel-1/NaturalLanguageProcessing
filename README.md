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

Enter input text in: 'textAnalysis/corpora/textInput.txt'

2. Filter

What category you are searching for keywords in: DevOps? Financial Technology? Software Engineering? Aerospace?

Determine which 'skippable-words' filter you would like. In the file 'textAnalysis/skippables.py', look at the list of filters to select the category of jargon you would like to remove from your results.

For example:

'skippablesAerospaceWords' for Aerospace,

'skippablesTechAndGovtResumeWords' for tech jobs in the government.

To designate the filter you want to use, navigate to the line in 'textInputReader.py':

```chosenLibrary = basicSkippables```

...and substitute 'basicSkippables' with the chosen filter name from 'textAnalysis/skippables.py'. For example, the structure for govt tech jobs would be:

```chosenLibrary = skippablesTechAndGovtResumeWords```

3. (Optional) Search By Target Words

In addition to filtering out words, we can search for specific target words in a text. This can be useful to see if a candidate has a specific skill required by a job posting.

In 'textInputReader.py', navigate to the 'targetWords' list variable under 'STEP 3 (Optional): CHOOSE YOUR TARGET SEARCH WORDS'.

```targetWords = ['software','developer']```

Modify the list of targetWords to include your search criteria.
You can also select a prebuilt target word list such as 'defaultTargetWords' or 'aerospaceTargetWords'. If you are using 'aerospaceTargetWords', for example, change the targetWords variable to:

```targetWords = aerospaceTargetWords```

The TARGET WORD print option is selected by DEFAULT. This functionality can be customized to provide succinct print options, as laid out below.

4. Configure a Print Option

At the bottom of 'textInputReader.py', navigate to where it reads "CONFIGURE A PRINT OPTION".

Read the available options and uncomment-out those which you wish to see. For example, OPTION 1 is represented as:

```
### OPTION 1: ALL UNIQUE KEYS AND THEIR RESPECTIVE FREQUENCIES
print('##### ALL UNIQUE KEY WORDS / FREQUENCY #####')
prettySort(dictionaryReverseSort(uniqueWordList))
```

This prints all unique keywords in the document, filtered with the optional chosen filter, and sorted by frequency of occurence with the most common on top.

To remove the TARGET WORD data read-out:

At the bottom of 'textInputReader.py', comment-out the two lines under printing functionality 'OPTION 4: REPORT PRESENCE OF TARGET WORDS' to stop returning the frequency of target words in the inputted text.

Have fun experimenting with print styles! There's an elegant multi-column option in there as well!


5. Run

```
python3 'textAnalysis/textInputReader.py'
```


### Training Data
The model is made more precise with the filters located in 'skippables.py'. To refine the model for your own use, consider adding a new filter or ammending mine for your needs.