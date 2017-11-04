#Accounts.py, outlines the different kinds of accounts that can be created
#and stores various relevant fields

class Grader(object):
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.average = 0

    def add_grade(self, grade):
        self.grades.append(grade)
        self.average = (sum(self.grades))/(len(self.grades))

class Student(object):
    def __init__(self, name):
        self.status = "Incomplete"
        self.name = name

    def complete(self):
        self.status = "Under Review"

    def result(self, decision):
        if decision:
            self.status = "Accepted"
        else:
            self.status = "Rejected"

class Nominator(object):
    def __init__(self, name):
        self.name = name
        self.submissions = 0
        self.names = []

    def nominate(self, student):
        self.submissions += 1
        self.names.append(student)
