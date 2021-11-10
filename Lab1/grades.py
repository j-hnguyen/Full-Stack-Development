grades_dict = {}
with open("grades.txt", "r") as file:
    grades_dict = fiel.readlines()
ans = True
while ans:
    print("What would you like to do?"
          "1. Add student name and grade"
          "2. Look at a student's grade, given the full name"
          "3. Edit a student's grade"
          "4. Delete a student's grade"
          "5. Exit/Quit")
    ans = input()
    if ans == '1':
        print("Enter the student's name: ")
        name = input()
        print("Enter their grade: ")
        grade = input()
        grades_dict[name] = grade
    if ans == '2':
        print("Which student's grad would you like to look at?")