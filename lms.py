class LearningManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name):
        self.students.append(name)