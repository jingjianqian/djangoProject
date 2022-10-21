if __name__ == '__main__':
    # python 判断数组中是否包含某个字符串
    # 成员运算符
    sheet1 = ['张三', '李四', '王五']
    sheet2 = ['学号-张三', '学号-李四', '学号-王sdf五']
    finished = []
    not_finished = []
    for s2 in sheet2:
        for s1 in sheet1:
            if s1 in s2:
                finished.append(s1)
    print(finished)

    for s1_name in sheet1:
        if s1_name not in finished:
            not_finished.append(s1_name)

    print(not_finished)
