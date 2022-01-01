from transitions.extensions import GraphMachine
from utils import send_text_message, send_notice_message, send_button_message, send_carousel_message, send_definition_message
#from bs4 import BeautifulSoup
import requests
from linebot.models import CarouselColumn, URITemplateAction, MessageTemplateAction
import pandas as pd
import random
from crawler import crawler


global cate 
cate = 'none'
global db 
db = pd.read_csv('./tarot.csv')
global past 
past = []
global num, direction, left

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lecture(self, event):
        text = event.message.text
        if text == '課業':
            return True
        return False

    def on_enter_lecture(self, event):
        global cate
        cate = 'lecture'
        print(cate)
        title = '現在準備為您進行"課業"占卜'
        text = '請選擇占卜的方式'
        btn = [
            MessageTemplateAction(
                label = '一張牌',
                text ='一張牌'
            ),
            MessageTemplateAction(
                label = '三張牌',
                text = '三張牌'
            ),
        ]
        url = 'https://i.imgur.com/xAn4QKL.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_relation(self, event):
        text = event.message.text
        if text == '人際關係':
            return True
        return False

    def on_enter_relation(self, event):
        global cate
        cate = 'relation'
        title = '現在準備為您進行"人際關係"占卜'
        text = '請選擇占卜的方式'
        btn = [
            MessageTemplateAction(
                label = '一張牌',
                text ='一張牌'
            ),
            MessageTemplateAction(
                label = '三張牌',
                text = '三張牌'
            ),
        ]
        url = 'https://i.imgur.com/2rCbqFV.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
 
    
    def is_going_to_health(self, event):
        text = event.message.text
        if text == '健康':
            return True
        return False
    
    def on_enter_health(self, event):
        global cate
        cate = 'health'
        title = '現在準備為您進行"健康"占卜'
        text = '請選擇占卜的方式'
        btn = [
            MessageTemplateAction(
                label = '一張牌',
                text ='一張牌'
            ),
            MessageTemplateAction(
                label = '三張牌',
                text = '三張牌'
            ),
        ]
        url = 'https://i.imgur.com/25sqgme.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_seven_days(self, event):
        text = event.message.text
        if text == '七天運勢':
            return True
        return False

    def on_enter_seven_days(self, event):
        global cate
        cate = 'seven_days'
        title = '現在準備為您進行"七天運勢"占卜'
        text = '請按下抽取開始占卜'
        btn = [
            MessageTemplateAction(
                label = '抽取',
                text = '抽取'
            ),
        ]
        url = 'https://i.imgur.com/UfvvrcQ.jpg'
        send_button_message(event.reply_token, title, text, btn, url)    
    
    def is_going_to_else(self, event):
        text = event.message.text
        if text == '其他':
            return True
        return False

    def on_enter_else(self, event):
        global cate
        cate = 'else'
        title = '現在準備為您進行占卜'
        text = '請選擇占卜的方式'
        btn = [
            MessageTemplateAction(
                label = '一張牌',
                text = '一張牌'
            ),
            MessageTemplateAction(
                label = '三張牌',
                text = '三張牌'
            ),
        ]
        url = 'https://i.imgur.com/RWZhynA.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_one_1(self, event):
        text = event.message.text
        if text == '一張牌':
            return True
        return False
    
    def on_enter_one_1(self, event):
        global num, direction, left
        num = random.randint(0,21)
        direction = random.randint(1,2)
        print(num, direction, 2 * num + direction - 1)
        left = 0

        url = db['url'][2 * num + direction - 1]
        name = db['name'][2 * num + direction - 1]
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1]
        btn = [
            MessageTemplateAction(
                label = '返回首頁',
                text = '返回首頁',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_three_1(self, event):
        text = event.message.text
        if text == '三張牌':
            return True
        return False
    
    def on_enter_three_1(self, event):
        global num, direction, left
        num = random.randint(0,21)
        direction = random.randint(1,2)
        left = 1

        url = db['url'][2 * num + direction - 1]
        name = db['name'][2 * num + direction - 1]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        
        title = '您抽到的是' + name + direction_w + ' 這張牌是對過去狀況的總結'
        text = db[cate][2 * num + direction - 1 ]

        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_three_2(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_three_2(self, event):
        global num, direction 
        num = random.randint(0,21)
        direction = random.randint(1,2)

        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

       
        title = '您抽到的是' + name + direction_w + ' 這張牌代表您目前身處的情境'
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_three_3(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_three_3(self, event):
        global num, direction, left
        num = random.randint(0,21)
        direction = random.randint(1,2)
        left = 0

        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w + ' 這是塔羅牌所給予你關於未來的建議'
        text = db[cate][2 * num + direction - 1 ]

        btn = [
            MessageTemplateAction(
                label = '返回首頁',
                text = '返回首頁',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_seven_1(self, event):
        text = event.message.text
        if text == '抽取':
            return True
        return False
    
    def on_enter_seven_1(self, event):
        global num, direction, left 
        num = random.randint(0,21)
        direction = random.randint(1,2)
        left = 1
        
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_seven_2(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_2(self, event):
        global num, direction
        num = random.randint(0,21)
        direction = random.randint(1,2)
        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_seven_3(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_3(self, event):
        global num, direction
        num = random.randint(0,21)
        direction = random.randint(1,2)
        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_seven_4(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_4(self, event):
        global num, direction
        num = random.randint(0,21)
        direction = random.randint(1,2)
        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_seven_5(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_5(self, event):
        global num, direction
        num = random.randint(0,21)
        direction = random.randint(1,2)
        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_seven_6(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_6(self, event):
        global num, direction
        num = random.randint(0,21)
        direction = random.randint(1,2)
        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '抽下一張',
                text = '抽下一張',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_seven_7(self, event):
        text = event.message.text
        if text == '抽下一張':
            return True
        return False
    
    def on_enter_seven_7(self, event):
        global num, direction, left
        num = random.randint(0,21)
        direction = random.randint(1,2)
        left = 0

        while (2 * num + direction - 1) in past:
            num = random.randint(0,21)
            direction = random.randint(1,2)
        url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = '您抽到的是' + name + direction_w
        text = db[cate][2 * num + direction - 1 ]
        btn = [
            MessageTemplateAction(
                label = '返回首頁',
                text = '返回首頁',
            ),
            MessageTemplateAction(
                label = '觀看更多牌義',
                text = '觀看更多牌義',
            ),
        ]
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_notice(self, event):
        text = event.message.text
        if text == "閱讀占卜的注意事項":
            return True
        else:
            return False

    def on_enter_notice(self, event):
        send_notice_message(event.reply_token)

    def is_going_to_user(self, event):
        text = event.message.text
        if text == '返回首頁':
            return True
        return False   

    def on_enter_user(self, event):
        past = []
        url = ['https://i.imgur.com/xAn4QKL.jpg', 
            'https://i.imgur.com/2rCbqFV.jpg', 
            'https://i.imgur.com/25sqgme.jpg', 
            'https://i.imgur.com/UfvvrcQ.jpg', 
            'https://i.imgur.com/RWZhynA.jpg']
        choice = ['課業','人際關係','健康','七天運勢', '其他']
        col = []

        c = CarouselColumn(
           thumbnail_image_url = "https://i.imgur.com/s2EDHNX.jpg",
           title =  '歡迎來到班傑明的塔羅占卜',
           text =  '可從此處閱讀占卜的注意事項',
           actions = [
               MessageTemplateAction(
                   label = '閱讀占卜的注意事項',
                   text = '閱讀占卜的注意事項',
               ),
           ]
        )
        col.append(c)
       
        for i in range(5):
            c = CarouselColumn(
                thumbnail_image_url = url[i],
                title =  '歡迎來到班傑明的塔羅占卜',
                text =  '請選擇您要占卜的項目',
                actions = [
                    MessageTemplateAction(
                        label = choice[i],
                        text = choice[i],
                    ),
                ]
            )
            col.append(c)

        send_carousel_message(event.reply_token, col)
    
    def definition(self, event):
        global left
        url = db['definition'][2 * num + direction - 1]
        string = crawler(url, direction)
 
        #url = db['url'][2 * num + direction - 1 ]
        name = db['name'][2 * num + direction - 1 ]
        past.append(2 * num + direction - 1)
        if direction == 1:
            direction_w = '正牌'
        else:
            direction_w = '反牌'

        title = name + direction_w + '的更多牌義解釋'
        text = string
        if left == 0:
            b_text = "返回首頁",
        else:
            b_text = "抽下一張",

        send_definition_message(event.reply_token, text, b_text)