# Author: Matthew Cohen
# Date: 2021-06-30
# Name: Score.py
# Prereq: answerKey.txt from AnswerKey.py & answersToQuestion.txt
#
# Purpose: This script will use the answer key generated from AnswerKey.py and
# will take the answers given from the user in answersToQuestion.txt and compare.
# Once given a chapter the script will let the user know what they got right and
# what they got wrong.
#
# Resources: https://www.w3schools.com/python/python_regex.asp
#            https://www.geeksforgeeks.org/string-comparison-in-python/
#            https://flexiple.com/check-if-list-is-empty-python/
#            https://careerkarma.com/blog/python-print-without-new-line/
#            https://rubular.com/
#            https://careerkarma.com/blog/python-string-to-int/


import re
answersToQuestion = "answersToQuestion.txt"
answerKey = "answerKey2.txt"

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
    print("\t  Answer Key: "+answers[count].upper() + "\t  Answer Put: "+ans.upper())
    count+=1

print("\nTotal Score: " + str((correctCount/length)*100.0)+"%")
print("Questions Correct: " + str(correctCount) + "\t" + "Total Questions: " + str(length))
