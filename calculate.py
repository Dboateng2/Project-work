def calculateTotalScore(classScore, examScore):
    return classScore + examScore

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
    if grade in ["A"]:
        return "Excellent"
    elif grade in ["B"]:
        return "Very Good"
    elif grade in ["C"]:
        return "Good"
    elif grade in ["D"]:
        return "Fair"
    elif grade in ["E"]:
        return "Poor"
    else:
        return "Very Poor"
