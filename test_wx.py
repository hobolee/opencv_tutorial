from wxpy import *
import time

bot = Bot()

def send_news(c):
    contents = 'This is a message from python.'
    my_friend = bot.friends().search(u'李昊波')[0]
    my_friend.send(c)

# if __name__ == '__main__':
    # c = input()
while True:
    # time.sleep(1)
    c = input("发送什么消息：")
    send_news(c)
