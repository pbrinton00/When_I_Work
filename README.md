When I Work Code Challenge

This repo is broken up into a problem directory and solution directory.

** Problem Directory **
1. This Holds all the given problem documents.

** Solution Directory ***
1. There are 2 solutions presented for this problem.
    -- Python Solution
    -- Java Solution
2. There are readme.md in each solution directory explaining what is and is not in each solution.

** Approach **
I started with a quick language evaluation for this problem.  

** Language evaluation:  
    * Overview:
        I would have liked to use GO for the solution but I do not have enough accumen to complete this solution without utilizing AI to assist in the construction.  I thought about using Java as it is my dominate language choice.  I decied not to use Java to start with because it is not a native part of the "When I Work" stack.  I later concluded that Java is a much better choice than Python.  I started and completed a version of the solution in Python.  I concluded that there are some very powerful advantages to using Python and specificly the Pandas library for this solution.  Unfortuantily I think there are mnore compleling disadvantages to using python that out weight these benifits.  Below is a quick recap of my findings.
    
    * Language Analysis:
        -- GO 
            I feel like there are some native synergies to using GO for this solution.  Unfortuanitly I do not have enough exposure to the language yet to articulate where they are.  Given that I have around 6 hours of experience with GO, I have to leave this as an item that needs further research.
        -- Python
            I chose python because I have been imersed in the language for the last 6 weeks working mainly on Data Science problems.  I chose this problem as an oppertunity to explore limits in the language and test my knowledge.
            ** Advanatages:
                Pandas library:  This library is very powerful and efficient at data manipulation.  For example this library lets the programer maipulate the data in memory as if it where ina  relation DB.  We can skip expensive loops and use advanced data opperations that just are not traditionaly available in other languages.
                Data Tpye Casting:  Python did a great job in letting the data just be data.  I encontered very little issue with data types and the ability to compare and manipulate the data set. 
            ** Disadvantages:
                Deployment:  I mistakenly started working the problem in a Jupitor note book.   while this is great for roughing out the code and working the problem into a final workf flow there is not a clean way to wrap the note book into a deliverable.  
                Testing Framework:  I did not find a good way to incorerate classical unit tests in the code.  The solution feels very incomplete with out having basic tests baked into build/execution time.  Granted you could chose to use 'unittest' or 'pytest' but these would require a setup of CI/CD to be effective and not offer the programer assitance prior to deployment.
        -- Java:
            I felt that I did not accomplish what I realy wanted to for this problem in Python.  I know exactly how I would solve this problem in Java so I decieded to spend some time after the original 3 hour window has eleapse and just stub out the solution.  This was to statisfy my own needs in resolving the problem in a mannor I am comfortable with.
            ** Advantages:
                * Java has excelent run time options that help this problem become a real time solution.  
                * By using the Spring Frame work we get rock solid ties to data stores like kafka and rdms as well as API frameworks.
                * There are well defined hooks in to alerting and performance tracking.
            ** Disadvantages: 
                * Java can be bulky in building out simple solutions.
                * Java can be painful to deploy with out forthought in deployment startegies and infrstructure.

    * Problem Analysis
        -- Overall Thoughts
            * Although this problem is presented in a batching style frame work.  I feel the best solution for this problem would be a realtime processing solution.  Once the data is ingested the first time it should stay in motion and each record should be broken out into individual transations.
            * This problem lends itself to many data looping pitfalls.  For example there are dependent data validation checks that can only be perfomed correctly if you have knopwledge of the complete data set for each transaction.  This leads me to concluding that a robust system of data chaches or data stores should be used to resolve this issue at scale.   
        -- Take Aways
            * Any solution needs take into account the complexity of managing time zones and complex dates.
            * A proper language selection needs to take place so this problem can be split into managaable componets that will work at scale.  
            
            
    * Conclusion:
            * Python is not advisable as a language because of deployment complexities, eventual technical debt for maintanance and availabel project structures for development time testing. 
            * With my expeerience I would use Java to break apart this problem into seperate deployable componets to resolve this issue at scale.  An ingestion soluton, a processing solution, and a data retention solution.  


