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

plt.bar(subjectNames, [float(i) for i in percentages], width=0.4)
plt.xlabel('SUBJECTS')
plt.ylabel('MARKS IN PERCENTAGE')
plt.title(f'Percentages of {studentName} Marks')
plt.show()

raw_totals = [calculate.calculateTotalScore(classScores[i], examScores[i]) for i in range(3)]

fig, ax = plt.subplots()
index = range(len(subjectNames))
bar_width = 0.2

bar1 = plt.bar(index, classScores, bar_width, label='Class Score', color='b')

bar2 = plt.bar([p + bar_width for p in index], examScores, bar_width, label='Exam Score', color='g')
bar3 = plt.bar([p + bar_width*2 for p in index], raw_totals, bar_width, label='Raw Total', color='r')

plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title(f'Scores for {studentName}')
plt.xticks([p + bar_width for p in index], subjectNames)
plt.legend()

plt.show()
