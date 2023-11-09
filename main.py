import matplotlib.pyplot as plt
import calculate

studentName = input("Enter Student Name: ")
subjectNames = []
classScores = []
examScores = []
percentages = []
grades = []
results = []

for i in range(3):  
    subject = input("Enter Subject Name: ")
    classScore = float(input(f"Enter class score for {subject} (out of 200): "))
    examScore = float(input(f"Enter exam score for {subject} (out of 500): "))
    print(classScore, examScore)
    
    subjectNames.append(subject)
    classScores.append(classScore)
    examScores.append(examScore)

for i in range(3):  
    totalScore = calculate.calculateTotalScore(classScores[i], examScores[i])
    percentage = calculate.calculatePercentage(totalScore)
    grade = calculate.calculateGrade(percentage)
    result = calculate.calculateResult(grade)

    oneDp = "{:.1f}".format(percentage)  

    percentages.append(oneDp)
    grades.append(grade)
    results.append(result)

for i in range(3):  
    print(f"Remarks: {studentName} scored {percentages[i]}% in {subjectNames[i]} and had a grade {grades[i]}. Result: {results[i]}")



plt.bar(subjectNames, percentages,width=0.4)
plt.xlabel('Subjects')
plt.ylabel('Percentage')
plt.title(f'Percentage for {studentName}')
plt.show()
