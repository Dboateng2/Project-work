def calculateTotalScore(class_score, exam_score):
    return class_score + exam_score

def calculatePercentage(total_score):
    return (total_score / 700) * 100

def calculateGrade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"

def calculateResult(grade):
    if grade in ["A", "B", "C"]:
        return "Pass"
    else:
        return "Fail"