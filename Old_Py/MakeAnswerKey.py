# Author: Matthew Cohen
# Date: 2021-06-30
# Name: MakeAnswerKey.py
# Prereq: answers.txt which consists of the entire review questions from CompTia Linux+
# study guide.
#
# Purpose: This script will take a txt file of answers from the Linux+ CompTia
# study guide. You can make this txt file by just copying and pasting all the 
# review questions' answers and putting it into a text file. This script will then
# filter out just the answer, the chapter, and the number. Ex. Chapter 2
#                                                              1. A
#
# Resources: https://www.w3schools.com/python/python_regex.asp
#            https://www.geeksforgeeks.org/string-comparison-in-python/
#            https://flexiple.com/check-if-list-is-empty-python/
#            https://careerkarma.com/blog/python-print-without-new-line/
#            https://rubular.com/
#            https://careerkarma.com/blog/python-string-to-int/

import re
reviewQuestionDoc = "answers.txt"
writeMatchesDoc = "answerKey.txt"

print("Reading from " +  reviewQuestionDoc +"...")
# Opening the file and reading it into f
txtF = open(reviewQuestionDoc, "r")
f = txtF.read()
#print(f.read())
txtF.close()


#pattern = re.compile("[0-9]+.\s([A-Z])")


print("Finding matches...")
# Getting the matches based on the regex
#old pattern [0-9]+[.]\s([A-Z|,\sA-Z]+)
matches = re.findall("([0-9]+[.]\\s[ABCDEF|,\\sABCDEF]+)",f)
            # This will match every answer based on its number and letter answer
            # example: 1. A, B, C or 1. A

# Writing out to a textfile by iterating over each match
textfile = open(writeMatchesDoc, "w")

chapterCount = 2 # Used to indicate what chapter the answer is in
for element in matches:
    element = re.sub('[\s+]', '', element) #removes whitespace
    # Chapter counter based on every occurence of 1.
    if(element.count("1")==1 and element.count("1.")==1):
        string = str(chapterCount)
        textfile.write("CHAPTER "+ string + ":"+ "\n"+ element + "\n")
        chapterCount+=1
    else:           
        textfile.write(element + "\n")

textfile.close()
print("If matches found, writing to: " + writeMatchesDoc + "...")
