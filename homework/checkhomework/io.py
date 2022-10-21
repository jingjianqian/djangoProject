import pathlib
import xlwings as excle


# 获取学生作业清单
def get_homework_list(target_path):
    print(target_path)
    if pathlib.Path(target_path).exists():
        if pathlib.Path(target_path).is_dir():
            print("开始进入" + target_path + "获取作业清单")
            homeworks = pathlib.Path(target_path).glob("*")
            homeworks_array = []
            for homework in homeworks:
                homeworks_array.append(homework.name)
            return homeworks_array
        else:
            print(target_path + "不是目录")

    else:
        print(" 路径不存在")


# 获取学生清单 返回数据
def get_students(xml_path):
    visible = False
    add_book = False
    start_row = 2
    end_row = 1000
    students_array = []
    sheet1 = excle.App(visible, add_book).books.open(xml_path).sheets[0]
    for row in range(start_row, end_row):
        row_str = str(row)
        name = sheet1.range('A' + row_str).value
        # no = sheet1.range('B' + row_str).value
        if name is not None:
            students_array.append(name)
        else:
            print("读取结束！")
            break
    return students_array


# 检查学生作业
def check_homework(homework_dir, xml_path):
    _homeworks = get_homework_list(homework_dir)  # 作业数组
    _students = get_students(xml_path)  # 学生数组
    print(_homeworks)
    print(_students)
    finished = []
    not_finished = []
    for homework_student in _homeworks:
        for student_name in _students:  # 逐个查看学生名在不在完成的作业清单内
            if student_name in homework_student:
                finished.append(student_name)
    # print(finished)

    for student_name in _students:
        if student_name not in finished:
            not_finished.append(student_name)
    return finished, not_finished


if __name__ == '__main__':
    finished_name, not_finished_name = check_homework("E:\\data\\20220823\\上课\\作业\\7班\\01.作业归档\\9月20日作业",
                                                      "E:\\data\\20220823\\班级\\7班\\学生清单.xlsx")
    print(finished_name)
    print(not_finished_name)
