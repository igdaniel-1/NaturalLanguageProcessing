basicSkippables = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 
              'of', 'as', 'with', 'such', 'etc', 'are', 'is', 
              'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 
              'we', 'you', 'they', 'and/or',
              'A', 'An', 'The', 'In', 'At', 'On', 'Or', 'And', 
              'Of', 'As', 'With', 'Such', 'Etc', 'Are', 'Is', 
              'Was', 'May', 'Be', 'Maybe', 'To', 'From', 'Along', 
              'We', 'You', 'They', 'AND/OR',
              'least', 'Least', 'what', 'What', 'which','Which',
              'us', 'Us','must','Must', 'only','Only',
              'including','Including', 'addition', 'Addition',
              'similar','Similar','for', 'For','by', 'By', 
              'who', 'Who', 'where','Where','when','When','why','Why',
              'this','This','that','That','low','Low','high','High',
              'lower','Lower','higher','Higher','lowest','highest',
              '1','2','3','4','5','6','7','8','9',
              'our','Our', 'been','Been', 'also','Also'
              ]

skippablesPlusCommonResumeWords = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 
              'of', 'as', 'with', 'such', 'etc', 'are', 'is', 
              'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 
              'we', 'you', 'they', 'and/or',
              'A', 'An', 'The', 'In', 'At', 'On', 'Or', 'And', 
              'Of', 'As', 'With', 'Such', 'Etc', 'Are', 'Is', 
              'Was', 'May', 'Be', 'Maybe', 'To', 'From', 'Along', 
              'We', 'You', 'They', 'AND/OR',
              'least', 'Least', 'what', 'What', 'which','Which',
              'us', 'Us','must','Must', 'only','Only',
              'including','Including','addition', 'Addition',
              'similar','Similar', 'for', 'For', 'by', 'By', 
              'who', 'Who', 'where','Where','when','When','why','Why',
              'this','This','that','That','low','Low','high','High',
              'lower','Lower','higher','Higher','lowest','highest',
              '1','2','3','4','5','6','7','8','9',
              'our','Our', 'been','Been', 'also','Also',
              'make', 'Make',


    'require','Require', 'requirements','Requirements', 
    'requirement','Requirement', 'skills','Skills', 'skill','Skill',
    'related', 'Related','discipline','Discipline', 
    'years', 'Years','proven','Proven', 'experience','Experience',
    'expertise','Expertise', 'current','Current', 'recent','Recent',
    'U.S.', 'level', 'Level', 'models','Models','proficiency','Proficiency',
    'strong','Strong','technologies','Technologies','detail','Detail',
    'best', 'practices','Best', 'Practices','modern','Modern',
    'understanding','Understanding','understand','Understand',
    'accept', 'Accept','conditional','Conditional', 'offer', 'Offer',
    'employment','Employment', 'subject','Subject',
    'interest','Interest', 'position','Position',
    'new','New','emerging','Emerging','existing','Existing'
    'familiarity','Familiarity', 'ability','Ability',
    'trends','Trends','functional','Functional', 'attention','Attention',
    'requires','Requires','require','Require','required','Required',
    'applicants','Applicants','access','Access,'
    'customer','Customer', 'obtain', 'Obtain', 'information','Information',
    'issue','Issue', 'Issues','issues','working','Working', 
    'build','Build', 'builds','Builds', 'meet','Meet',
    'eligibility','Eligibility',
]

skippablesCommonAndTechResumeWords = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 
              'of', 'as', 'with', 'such', 'etc', 'are', 'is', 
              'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 
              'we', 'you', 'they', 'and/or',
              'A', 'An', 'The', 'In', 'At', 'On', 'Or', 'And', 
              'Of', 'As', 'With', 'Such', 'Etc', 'Are', 'Is', 
              'Was', 'May', 'Be', 'Maybe', 'To', 'From', 'Along', 
              'We', 'You', 'They', 'AND/OR',
              'least', 'Least', 'what', 'What', 'which','Which',
              'us', 'Us','must','Must', 'only','Only',
              'including','Including','addition', 'Addition',
              'similar','Similar', 'for', 'For', 'by', 'By', 
              'who', 'Who', 'where','Where','when','When','why','Why',
              'this','This','that','That','low','Low','high','High',
              'lower','Lower','higher','Higher','lowest','highest',
              '1','2','3','4','5','6','7','8','9',
              'our','Our', 'been','Been', 'also','Also'
              'make', 'Make',


    'require','Require', 'requirements','Requirements', 
    'requirement','Requirement', 'skills','Skills', 'skill','Skill',
    'related', 'Related','discipline','Discipline', 
    'years', 'Years','proven','Proven', 'experience','Experience',
    'expertise','Expertise', 'current','Current', 'recent','Recent',
    'U.S.', 'level', 'Level', 'models','Models','proficiency','Proficiency',
    'strong','Strong','technologies','Technologies','detail','Detail',
    'best', 'practices','Best', 'Practices','modern','Modern',
    'understanding','Understanding','understand','Understand',
    'accept', 'Accept','conditional','Conditional', 'offer', 'Offer',
    'employment','Employment', 'subject','Subject',
    'interest','Interest', 'position','Position',
    'new','New','emerging','Emerging','existing','Existing'
    'familiarity','Familiarity', 'ability','Ability',
    'trends','Trends','functional','Functional', 'attention','Attention',
    'requires','Requires','require','Require','required','Required',
    'applicants','Applicants','access','Access,'
    'customer','Customer', 'obtain', 'Obtain', 'information','Information',
    'issue','Issue', 'Issues','issues','working','Working', 
    'build','Build', 'builds','Builds','meet','Meet',
    'eligibility','Eligibility',


    'analyze','Analyze','analyse','Analyse','develop', 'Develop',
    'development','Development','programming','Programming',
    'technical','Technical','innovation','Innovation',
    'application','Application','applications','Applications',
    'design','Design','engineer','Engineer', 'Computer','computer',
    'programming','Programming', 'BS', 'B.S.', 'software', 'Software',
    'engineer', 'Engineer', 'engineering', 'Engineering',
    'science', 'Science', 'customer','Customer', 'Value','value',





]


skippablesTechAndGovtResumeWords = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', 
              'of', 'as', 'with', 'such', 'etc', 'are', 'is', 
              'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 
              'we', 'you', 'they', 'and/or',
              'A', 'An', 'The', 'In', 'At', 'On', 'Or', 'And', 
              'Of', 'As', 'With', 'Such', 'Etc', 'Are', 'Is', 
              'Was', 'May', 'Be', 'Maybe', 'To', 'From', 'Along', 
              'We', 'You', 'They', 'AND/OR',
              'least', 'Least', 'what', 'What', 'which','Which',
              'us', 'Us','must','Must', 'only','Only',
              'including','Including','addition', 'Addition',
              'similar','Similar', 'for', 'For', 'by', 'By', 
              'who', 'Who', 'where','Where','when','When','why','Why',
              'this','This','that','That','low','Low','high','High',
              'lower','Lower','higher','Higher','lowest','highest',
              '1','2','3','4','5','6','7','8','9',
              'our','Our', 'been','Been', 'also','Also'
              'make', 'Make',


    'require','Require', 'requirements','Requirements', 
    'requirement','Requirement', 'skills','Skills', 'skill','Skill',
    'related', 'Related','discipline','Discipline', 
    'years', 'Years','proven','Proven', 'experience','Experience',
    'expertise','Expertise', 'current','Current', 'recent','Recent',
    'U.S.','U.S', 'level', 'Level', 'models','Models','proficiency','Proficiency',
    'strong','Strong','technologies','Technologies','detail','Detail',
    'best', 'practices','Best', 'Practices','modern','Modern',
    'understanding','Understanding','understand','Understand',
    'accept', 'Accept','conditional','Conditional', 'offer', 'Offer',
    'employment','Employment', 'subject','Subject',
    'interest','Interest', 'position','Position',
    'new','New','emerging','Emerging','existing','Existing'
    'familiarity','Familiarity', 'ability','Ability',
    'trends','Trends','functional','Functional', 'attention','Attention',
    'requires','Requires','require','Require','required','Required',
    'applicants','Applicants','access','Access,'
    'customer','Customer', 'obtain', 'Obtain', 'information','Information',
    'issue','Issue', 'Issues','issues','working','Working', 
    'build','Build', 'builds','Builds','meet','Meet',
    'eligibility','Eligibility',


    'analyze','Analyze','analyse','Analyse','develop', 'Develop',
    'development','Development','programming','Programming',
    'technical','Technical','innovation','Innovation',
    'application','Application','applications','Applications',
    'design','Design','engineer','Engineer', 'Computer','computer',
    'programming','Programming', 'BS', 'B.S.', 'software', 'Software',
    'engineer', 'Engineer', 'engineering', 'Engineering',
    'science', 'Science', 'customer','Customer', 'Value','value',


    'Secret','secret', 'Government','government', 'citizens','Citizens',
    'granted','Granted','grant','Grant','classified','Classified',
    'investigation','Investigation','investigations','Investigations',
    'clearance','clearances','Clearances','Clearance'



]