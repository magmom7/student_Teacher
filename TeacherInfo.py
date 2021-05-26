class Teacher:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject

    def __str__(self):
        return self.name+' ' + self.grade+' ' + self.subject
