"""
课程类：
"""


class Course:

    def __init__(self, course_no, course_name):
        """

        :param course_no:     课程号
        :param course_name:   课程名
        """
        self.course_no = course_no
        self.course_name = course_name

    @property
    def course_no(self):
        print("getter")
        return self.course_no_setter

    @course_no.setter
    def course_no(self, course_no: int):
        print(type(course_no) is int)
        if type(course_no) is int:
            self.course_no_setter = course_no
        else:
            raise TypeError("课程号必须是int类型")


if __name__ == "__main__":
    course = Course(117, 'java高级程序设计')
    course.course_name = '123a'
    print(course.course_no)
