import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage, CarouselColumn, CarouselTemplate, URITemplateAction, ButtonsTemplate, MessageTemplateAction, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
import message_template


def send_text_message_AI(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token,TextSendMessage(text=Olami().nli(text)))

    return "OK"

def send_carousel_message(reply_token, col):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text = 'Carousel template',
        template = CarouselTemplate(columns = col, image_size = "contain")
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"



def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url = url,
        preview_image_url = url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"



channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    if url == "none":
        message = TemplateSendMessage(
            alt_text='button template',
            template = ButtonsTemplate(
                text = text,
                actions = btn,
            )
        )
    else:
        message = TemplateSendMessage(
            alt_text='button template',
            template = ButtonsTemplate(
                title = title,
                text = text,
                thumbnail_image_url = url,
                actions = btn,
                image_size = "contain"
            )
        )
    line_bot_api.reply_message(reply_token, message)
    
    return "OK"

def send_definition_message(reply_token, text, b_text):
    line_bot_api = LineBotApi(channel_access_token)
    t = message_template.definition
    t["body"]["contents"][0]["text"] = text
    t["body"]["contents"][1]["action"]["text"] = b_text[0]
    t["body"]["contents"][1]["action"]["label"] = b_text[0]
    message = FlexSendMessage(
        'definition template',
        t
    )
    line_bot_api.reply_message(reply_token, message)
    
    return "OK"

def send_notice_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    t = message_template.notice
    message = FlexSendMessage(
        'definition template',
        t
    )
    line_bot_api.reply_message(reply_token, message)
    
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
