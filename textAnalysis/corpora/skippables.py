# These are filter options 
# Each option builds upon the basic filtr to provide more narrow results when searcing for keywords in a particular field
# For example, when searching for keywords for avaition roles,
# ... one could filter out 'skippablesAviationWords' to remove tose terms from the top results
# ... and instead focus on role-specific skills that differ from the industry stanard

basicSkippables = ['a', 'an', 'the', 'in', 'at', 'on', 'or', 'and', '&',
              'of', 'as', 'with', 'such', 'etc', 'are', 'is', 
              'was', 'may', 'be', 'maybe', 'to', 'from', 'along', 
              'we', 'you', 'they', 'and/or','I','it','It','its','Its',
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
              'our','Our', 'been','Been', 'also','Also',
              'make', 'Make','while', 'While','all', 'All',
              'not', 'Not', 'any', 'Any', 'other', 'Other',
              'will','Will','using','Using','use','Use','uses','Uses', 
              'used', 'Used','through', 'Through','though','Though','during','During'
              ]

skippablesPlusCommonResumeWords = basicSkippables + ['require','Require', 'requirements','Requirements', 
    'requirement','Requirement', 'skills','Skills', 'skill','Skill','paid','Paid',
    'need','Need','needs','Needs','apply','Apply','know','Know','well','Well',
    'related', 'Related','discipline','Discipline', 'range','Range',
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
    'function','Function','functions','Functions',
    'requires','Requires','require','Require','required','Required',
    'applicants','ApplicSants','access','Access,'
    'customer','Customer', 'customers','Customers','obtain', 'Obtain', 'information','Information',
    'issue','Issue', 'Issues','issues','working','Working', 
    'build','Build', 'builds','Builds', 'meet','Meet',
    'eligibility','Eligibility','solution','Solution','solutions','Solutions',
    'individual', 'individuals','Individual', 'Individuals',
    'Requirements','Requirement', 'requirements','requirements',
    'having','Having', 'has','had', 'have','shall','Shall','should','Should','company', 'Company', 'enterprise','Enterprise',
    'employees','Employees','employee','Employee','employer','Employer',
    'succeed','Succeed','success','Success',
    'helping','Helping','help','Help','helps','Helps',
    'focus','Focus','focuses','Focuses','focusing','Focusing',
    'eligible','Eligible','eligibility','Eligibility',
    'able','Able','ability','Ability',
    'choice','Choice','choices','Choices',
    'join','Join','providing','Providing',
    'add','Add','adds','Adds','techniques','Techniques',
    'tool','Tool','tools','Tools',
    'location','Location','locations','Locations',
    'capability','Capability','capabilities','Capabilities',
    'improve','Improve','improves','Improves','improvement','Improvement',
    'enhance', 'Enhance','enhances', 'Enhances','enhancement','Enhancement',
    'looking','Looking','look','Look','looks''Looks',
    'provide','Provide','provides','Provides',
    'enable','Enable','enables','Enables','role','roles','Role','Roles','based',
    'strategy','Strategy','over','Over','under','Under',
    

]

skippablesCommonAndTechResumeWords = skippablesPlusCommonResumeWords + ['analyze','Analyze',
    'analyse','Analyse','develop', 'Develop',
    'development','Development','programming','Programming',
    'technical','Technical','innovation','Innovation',
    'application','Application','applications','Applications',
    'design','Design','engineer','Engineer', 'Computer','computer','computers','Computers',
    'program','Program', 'BS', 'B.S.', 'software', 'Software',
    'engineer', 'Engineer', 'engineering', 'Engineering',
    'science', 'Science', 'customer','Customer', 'Value','value','Values','values',
    'code','Code','codes','Codes', 'work', 'Work', 
    'functionality','Functionality','enhancements','enhancement', 'feature', 'features',
    'Enhancements','Enhancement', 'Feature', 'Features',
    'performance','Performance','digitally','Digitally',
    'efficiency','Efficiency','advanced','Advanced','data','Data',
    'technology','Technology','dynamic','Dynamic',
    'computing','Computing','execution','Execution',
]


skippablesTechAndGovtResumeWords = skippablesCommonAndTechResumeWords + ['Secret','secret', 
    'Government','government', 'citizens','Citizens',
    'granted','Granted','grant','Grant','classified','Classified',
    'investigation','Investigation','investigations','Investigations',
    'clearance','clearances','Clearances','Clearance', 'Security', 'security',
    'defense', 'Defense', 'mission', 'Mission', 'critical', 'Critical', 
    'safe', 'Safe', 'professional', 'Professional','DoD', 
    'divulge', 'Divulge','divulges', 'Divulges','divulged', 'Divulged',
    'systems','system','Systems','System','maintaining','Maintaining',
    'maintainance','Maintainance','maintain','Maintain',
    'legacy','Legacy','readiness','Readiness', 'reliability','Reliability',
    'safety','Safety','safe','Safe',
    'ensuring','Ensuring','ensure','Ensure','civil','Civil','United','States'
]


skippablesAviationWords = skippablesTechAndGovtResumeWords + ['aviation', 'Aviation', 
    'military', 'Military', 'flight','Flight','flights','Flights',
    'pilot','pilots','Pilot','Pilots','piloting','Piloting',
    'mission','Mission','missions','Missions',
    
    ]
