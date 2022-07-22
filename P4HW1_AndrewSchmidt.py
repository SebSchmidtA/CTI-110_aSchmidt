# CTI-110
# P4HW1 - Score List
# Andrew Schmidt 
# 7/8/2022
#

def main():
    #defining basic variables
    grade = 0
    totalGrade = 0
    gradeList = []
    numScores = int(input("How many scores do you want?: "))
    count = 0
    print() #for spacing

    #
    for x in range(numScores):
        count += 1 #tracks how many times loop has been executed
        print(f"Enter score #{count}: ", end='')
        #i can't figure out how to nest extra variables into inputs, so i used end= as a workaround
        scoreEntry = int(input())
        totalGrade += scoreEntry
        gradeList.append(scoreEntry)
        while scoreEntry < 0 or scoreEntry > 100:
            print("\nINVALID. Please enter a number between 0 and 100")
            scoreEntry = input(f"Please Enter score #{count} again: ")
    #loop breaks and continues on to this code once it has executed enough times (as defined by numScores)
    gradeAvg = sum(gradeList)/len(gradeList)
    if gradeAvg > 90:
        gradeLetter = "A"
    elif gradeAvg > 80:
        gradeLetter = "B"
    elif gradeAvg > 70:
        gradeLetter = "C"
    elif gradeAvg > 60:
        gradeLetter = "D"
    else:
        gradeLetter = "F"
    
    print("\n----------Results----------") 
    print("Lowest Score  : ", min(gradeList))
    print("Modified List : ", gradeList)
    print("Scores Average: ", gradeAvg)
    print("Grade         : ", gradeLetter)
    print("----------------------------")




            

        

main()
