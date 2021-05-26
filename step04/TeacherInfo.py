'''
유재석,3학년담당,수학
백종원,2학년,음악
신동엽,1학년,미술
'''

class Teacher:

    def __init__(self, name, grade, subject):
        self.teacher_name = name
        self.teacher_grade = grade
        self.teacher_subject = subject

    def __str__(self):
        return '선생님 정보 ' + self.teacher_name + ' ' + self.teacher_grade + ' ' +  self.teacher_subject

    def setTeacherGrade(self, new_grade):
        pass