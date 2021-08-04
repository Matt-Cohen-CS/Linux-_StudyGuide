'''
    Author: Matthew Cohen
    Date: 2021-06-30
    Name: MakeAnswerKey.py
    Prereq: answers.txt which is the list of review questions with answers

    Resources: https://www.w3schools.com/python/python_regex.asp
                https://www.geeksforgeeks.org/string-comparison-in-python/
                https://flexiple.com/check-if-list-is-empty-python/
                https://careerkarma.com/blog/python-print-without-new-line/
                https://rubular.com/
                https://careerkarma.com/blog/python-string-to-int/
'''

import re


# Purpose: This script will take a txt file of answers from the Linux+ CompTia
# study guide. You can make this txt file by just copying and pasting all the 
# review questions' answers and putting it into a text file. This script will then
# filter out just the answer, the chapter, and the number. Ex. Chapter 2
#                                                              1. A
def makeAnswerKey():
    reviewQuestionDoc = "Answers/answers.txt"
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

#
# Purpose: This script will use the answer key generated from AnswerKey.py and
# will take the answers given from the user in answersToQuestion.txt and compare.
# Once given a chapter the script will let the user know what they got right and
# what they got wrong.
def getScoreFromAnswerKey():
    answersToQuestion = "answersToQuestion.txt"
    answerKey = "answerKey.txt"

    # Get the answers to questions in a list
    answer = open(answersToQuestion, "r")
    answers = answer.readlines()
    answer.close()

    # Get user chapter 
    chapter = input("What chapter did you do?: ")
    chapterInInt = int(chapter)

    # Open answer key for questions in a list
    ansKey = open(answerKey, "r")
    answerKeyList = ansKey.readlines()
    ansKey.close()

    match = False # Will be true when the chapter is correct in for loop
    myList = [] # List of answers from the given chapter
    length = 1 # Length of this list 
    #find the element based on the chapter and add it to the list
    for element in answerKeyList:
        if(chapterInInt<=0 and not match):
            length-=2 # This is for the two extra elements that will always be in length
                    # The chapter and one extra 1.
            break
        # This checks if there is a 1., but since 11. will be true I added a second condition
        if(element.count("1")==1 and element.count("1.")==1):
            chapterInInt-=1
            if(chapterInInt==1):
                chapterInInt-=1
                match = True
                length=0
                myList.clear()
            else:
                match = False
        if(match):
            element = re.sub('[0-9]+[.]','',element) # sub out the numbers with empty space
            myList.append(element.strip())
        length+=1 
    if(len(myList) != 0):
        myList.pop() # This will be like Chapter X so removing this from list

    count=0 # iterator for array
    correctCount = 0.0 # numerator for final grade

    # Comparing answers given to the answer key
    for ans in myList:
        print("\nQuestion "+ str(count+1),end='')
        if(answers[count].strip().upper()==ans.strip().upper()): # Stripping all whitespace and making both uppercase for comparison
            print(" Correct")
            correctCount+=1 
        else:
            print(" Incorrect")
        print("\t  Answer Put: "+answers[count].upper() + "\t  Answer Key: "+ans.upper())
        count+=1

    print("\nTotal Score: " + str((correctCount/length)*100.0)+"%")
    print("Questions Correct: " + str(correctCount) + "\t" + "Total Questions: " + str(length))

def main():
   # makeAnswerKey() # makes a key
    getScoreFromAnswerKey() # uses the key and chapter number to generate a grade

main()
