from TeacherInfo import Teacher


class Public:

    def public_teach():
        all_T = []

        with open('teachers.csv', 'r', encoding='utf-8') as f:
            data = f.readlines()

            for v in data:
                sv = v.split(',')
                all_T.append(Teacher(sv[0], sv[1], sv[2]))

        return all_T

    def prints(all_T):
        for v in all_T:
            print(v)

    if __name__ == '__main__':

        prints(public_teach())
