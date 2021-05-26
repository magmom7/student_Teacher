# 학생과 선생님 정보를 file 로 부터 read해서 , 를 기준으로 데이터를 나눠서 Student와 Teacher 객체 생성 및 제공

from StudentInfo import Student
from TeacherInfo import Teacher


class DataPublic:
    def teacher_public():
        all_teacher = []

        with open('teachers.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

            for v in data:
                sv = v.split(',')
                all_teacher.append(Teacher(sv[0], sv[1], sv[2]))

        return all_teacher

    def stu_public():
        all_stu = []

        with open('students.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

            for v in data:
                sv = v.split(',')
                all_stu.append(Student(sv[0], sv[1], sv[2], sv[3]))

        return all_stu

    def teacher_all_print(all_teacher):
        for v in all_teacher:
            print(v)
        print("")

    def stu_all_print(all_stu):
        for v in all_stu:
            print(v)
        print("")

    if __name__ == '__main__':
        teacher_all_print(teacher_public())
        stu_all_print(stu_public())
