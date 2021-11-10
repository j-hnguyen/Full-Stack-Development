with open("classesInput.txt", "r") as file:
    fileText = file.readlines()
    coursesNum = int(fileText[0])
    x = 1
    class Courses:
        def __init__(self, x):
            self.cdepartment = fileText[1*x]
            self.cnumber = fileText[2*x]
            self.cname = fileText[3*x]
            self.credits = fileText[4*x]
            self.days = fileText[5*x]
            self.starttime = fileText[6*x]
            self.endtime = fileText[7*x]
            self.avggrade = fileText[8*x]

        def print_schedule(self):
            print("COURSE %d: %s%d: %s" %(x, self.cdepartment, self.cnumber, self.cname))
            print("Number of Credits: %d" % self.credits)
            print("Days of Lectures: %s" % self.days)
            print("Lecture Time: %s - $s" %(self.starttime, self.endtime))
            print("Stat: on average, students get %d% in this course" % self.avggrade)

    schedule = [Courses(x) for x in range(coursesNum)]
    print(schedule)