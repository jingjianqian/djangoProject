
import json
from http import cookiejar
from lxml import etree

import requests

session = requests.session()
session.cookies = cookiejar.LWPCookieJar(filename='./security.cookie')

BaseUrl = 'https://www.51moot.net'

header = {
    'Referer': BaseUrl + "/main/index",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Chrome/89.0.4389.82',
    'authority': 'www.51moot.net',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}


def login(user, psw):
    try:
        data = {
            'login_name': user,
            'login_pass': psw
        }
        resp = session.post(url=BaseUrl + '/main/login_validate', headers=header, data=data)
        if resp.status_code == requests.codes.ok:
            session.cookies.save(ignore_discard=True, ignore_expires=True)
            print('登录成功')
            print(session.cookies)
            return True
        else:
            print("登录失败！！！")
            return False
    except Exception as ex:
        print(ex)
        print("失败了！！！！！")
        return False


# course_id:课程id  grade:年级 class_id:班级id chapter:章节
def get_course_chapter_complete_count(course_id, grade, class_id, chapter_index):
    course_page_html = get_course_page(course_id)
    course_res_json = get_course_complete_json(class_id, course_id)

    # 课程章节数
    course_chapter = course_page_html.xpath('//body//div[@class="course-details-content-video-view"]/ul/li')
    course_chapter_length = len(course_chapter)

    # 课程章节序号名  -第一章
    course_chapter_index_name = course_page_html.xpath(
        '//body//div[@class="course-details-content-video-view"]/ul/li['+chapter_index+']//h5/span[1]/text()')
    print(course_chapter_index_name)

    # 课程章节名
    course_chapter_name = course_page_html.xpath(
        '//body//div[@class="course-details-content-video-view"]/ul/li['+chapter_index+']//h5/span[2]/text()')
    print(course_chapter_name)

    # 课程章节每节内容  /html/body/div/div[3]/div[2]/ul/li[6]//ul/li/p/span[2]/text()
    course_chapter_dir_name = course_page_html.xpath(
        '/html/body/div/div[3]/div[2]/ul/li['+chapter_index+']//ul/li/p/span[2]/text()')
    print(course_chapter_dir_name)

    # 课程dir_id /html/body/div/div[3]/div[2]/ul/li[6]//ul/li/p/@onclick
    # course_complete_count =
    course_chapter_dir_id = course_page_html.xpath(
        '/html/body/div/div[3]/div[2]/ul/li['+chapter_index+']//ul/li/p/@onclick')
    # print(course_chapter_dir_id)
    course_complete_count = []

    for href_lin in course_chapter_dir_id:
        i = 0
        while i < len(course_res_json):
            if int(course_res_json[i].get('dir_id')) == int(href_lin[-5:-1]):
                course_complete_count.append(course_res_json[i])
            i = i + 1
    print(course_complete_count)


# 获取课程页面元素
def get_course_page(course_id):
    # 返回课程界面html
    print(session.cookies)
    course_html = session.get("https://www.51moot.net/server_hall_2/tea/course_content?course_id=" + str(course_id))
    return etree.HTML(course_html.text)


# 根据班级id以及课程id，返回班级课程阅读完成情况
def get_course_complete_json(class_id, course_id):
    print(session.cookies)
    param = {'class_id': int(class_id), 'course_id': int(course_id)}
    res = session.post("https://www.51moot.net/server_hall_2/tea/get_video_progress_by_class_id", data=param)
    print(res.text)
    return json.loads(res.text)


if __name__ == '__main__':
    if login("18697998680", "q529463245"):
        get_course_chapter_complete_count(1107, '2022', 2100, '6')
