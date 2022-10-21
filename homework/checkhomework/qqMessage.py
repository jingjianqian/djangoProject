import time
import requests

message_id_collect = []  # 放入获取的消息ID以便进行判断是否有人说话
message_id_collect_again = []  # 放入获取的消息ID以便进行判断是否有人说话
message_append = []  # 添加获取的内容


def res_get_error():  # 获取最新的消息数据
    res_get = requests.get(url=url, headers=headers).json()
    mes_get = res_get["data"]["messages"]
    for mes_get_append in mes_get:
        message_append.append(mes_get_append)
        # print(message_append)


def res_separate_mes():
    mes_get_append = message_append[-1]  # 最新的消息记录
    mes_content = mes_get_append["message"]  # 拿取消息内容
    mes_content_sender = mes_get_append["sender"]["nickname"]  # 拿取消息发送者的名字
    print("获取-----：" + mes_content_sender + ':' + mes_content)  # 检查是否正常
    API_get_answer(mes_content)


def API_get_answer(mes_content):  # 聊天API的调用，并获取回答
    urls = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(mes_content)
    answer_get = requests.get(url=urls, headers=headers).json()
    answer_content = answer_get["content"] + " --from robot"  # 获取API回答的内容
    print("回答：" + answer_content)  # 检察是否可以正常运行
    answer_post(answer_content)


def answer_post(answer_content):
    group_id = res_mes_post["group_id"]  # 群号
    msg = answer_content

    urls = "http://127.0.0.1:5700/send_group_msg?group_id=" + group_id + "&message=" + msg
    # print(urls)
    answer_post_use = requests.post(url=urls, headers=headers).json()  # 发送消息
    # print(answer_post_use)
    print("已回答")
    answer_post_again()


def answer_post_again():  # 发消息前的消息ID
    res_get_first = message_append[-1]
    res_mes_id = res_get_first["message_id"]
    message_id_collect.append(res_mes_id)
    nums = message_id_collect[-1]
    # print(nums)
    return nums  # 返回nums以便进行对比


def answer_post_again_check():  # 发消息后的消息ID
    res_get_again = message_append[-2]
    res_mes_id_again = res_get_again["message_id"]
    message_id_collect_again.append(res_mes_id_again)
    numss = message_id_collect_again[-1]
    # print(numss)
    return numss  # 返回nums以便进行对比


if __name__ == '__main__':
    res_mes_post = {"instruction_message": "message_seq", "group_id": "572403914", "message_id": ""}
    message_group_id = res_mes_post["group_id"]
    url = "http://127.0.0.1:5700/get_group_msg_history?group_id=" + message_group_id
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
    res = requests.get(url=url, headers=headers).json()
    # print(res)#检查
    while True:
        res_get_error()
        answer_post_again()
        n = answer_post_again()
        # print(message_id_collect)
        res_separate_mes()
        res_get_error()
        time.sleep(1)
        while True:
            res_get_error()
            answer_post_again_check()
            m = answer_post_again_check()
            time.sleep(1)
            # print(message_id_collect_again)
            if n == m:
                print("无消息")
                time.sleep(3)
                pass
            else:
                print("有消息")
                break