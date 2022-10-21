"""
成绩类
"""


class Score:
    # course_no = None
    # stu_no = None
    # written_score = None
    # machine_score = None

    def __init__(self, course_no, stu_no, written_score, machine_score):
        """
        :param course_no:         关联的课程好
        :param stu_no:            学生学号
        :param written_score:     笔试成绩
        :param machine_score:     机考成绩
        """
        self._course_no = course_no
        self._stu_no = stu_no
        self._written_score = written_score
        self._machine_score = machine_score

    @property
    def course_no(self):
        print('course_no getter')
        return self._course_no

    @course_no.setter
    def course_no(self, value):
        print('course_no setter')
        self._course_no = value

    @property
    def stu_no(self):
        print('stu_no getter')
        return self._stu_no

    @stu_no.setter
    def stu_no(self, value):
        print('stu_no setter')
        self._stu_no = value

    @property
    def written_score(self):
        print('written_score getter')
        return self._written_score

    @written_score.setter
    def written_score(self, value):
        print('written_score setter')
        self._written_score = value

    @property
    def machine_score(self):
        print('machine_score getter')
        return self._machine_score

    @machine_score.setter
    def machine_score(self, value):
        print('machine_score setter')
        self._machine_score = value


if __name__ == "__main__":
    score = Score(1, 2, 3, 4)
    score.course_no = 117
    score.stu_no = 1115080111
    score.written_score = 80
    score.machine_score = 100
    print(score.machine_score)
    print(score.written_score)
    print(score.stu_no)
    print(score.course_no)
