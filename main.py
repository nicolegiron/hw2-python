#Author : Nicole Giron nqg5259@psu.edu
def getGradePoint(course):
  if course == "A":
    return 4.0
  elif course == "A-":
    return 3.67
  elif course == "B+":
    return 3.33
  elif course == "B":
    return 3.0
  elif course == "B-":
    return 2.67
  elif course == "C+":
    return 2.33
  elif course == "C":
    return 2.0
  elif course == "D":
    return 1.0
  else :
    return 0.0

def run():
  grade = getGradePoint(float(input("Enter your course 1 letter grade: ")))
  course1 = input("Enter your course 1 letter grade: ")
  print(f"Grade point for course 1 is: {grade}.")

  grade2 = getGradePoint(float(input("Enter your course 2 letter grade: ")))
  course2 = input("Enter your course 2 letter grade: ")
  print(f"Grade point for course 2 is: {grade2}.")

  grade3 = getGradePoint(float(input("Enter your course 3 letter grade: ")))
  course3 = input("Enter your course 3 letter grade: ")
  print(f"Grade point for course 3 is: {grade3}.")

  GPA = (grade * course1 + grade2 * course2 + grade3 * course3) / (course1 + course2 + course3)
  print("Your GPA is: " + str(GPA))

if __name__ == "__main__":
  run()