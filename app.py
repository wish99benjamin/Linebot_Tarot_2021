import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import CarouselColumn, URITemplateAction, MessageTemplateAction

from fsm import TocMachine
from utils import send_text_message, send_button_message, send_carousel_message

load_dotenv()


def create_new_machine():
    return TocMachine(
    states=[
        "user", 
        "else", 
        "relation",
        "health",
        "seven_days",
        "lecture",
        "one_1",
        "three_1",
        "three_2",
        "three_3",
        "seven_1",
        "seven_2",
        "seven_3",
        "seven_4",
        "seven_5",
        "seven_6",
        "seven_7",
        "notice"
        ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "else",
            "conditions": "is_going_to_else",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "relation",
            "conditions": "is_going_to_relation",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "health",
            "conditions": "is_going_to_health",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "seven_days",
            "conditions": "is_going_to_seven_days",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "lecture",
            "conditions": "is_going_to_lecture",
        },
        #1day
        {
            "trigger": "advance",
            "source": 
            [ "else", "lecture", "relation", "health"],
            "dest": "one_1",
            "conditions": "is_going_to_one_1",
        },
        #3days
        {
            "trigger": "advance",
            "source": 
            [ "else", "lecture", "relation", "health"],
            "dest": "three_1",
            "conditions": "is_going_to_three_1",
        },
        {
            "trigger": "advance",
            "source": "three_1",
            "dest": "three_2",
            "conditions": "is_going_to_three_2",
        },
        {
            "trigger": "advance",
            "source": "three_2",
            "dest": "three_3",
            "conditions": "is_going_to_three_3",
        },
        #7days
        {
            "trigger": "advance",
            "source": "seven_days",
            "dest": "seven_1",
            "conditions": "is_going_to_seven_1",
        },
        {
            "trigger": "advance",
            "source": "seven_1",
            "dest": "seven_2",
            "conditions": "is_going_to_seven_2",
        },
        {
            "trigger": "advance",
            "source": "seven_2",
            "dest": "seven_3",
            "conditions": "is_going_to_seven_3",
        },
        {
            "trigger": "advance",
            "source": "seven_3",
            "dest": "seven_4",
            "conditions": "is_going_to_seven_4",
        },
        {
            "trigger": "advance",
            "source": "seven_4",
            "dest": "seven_5",
            "conditions": "is_going_to_seven_5",
        },
        {
            "trigger": "advance",
            "source": "seven_5",
            "dest": "seven_6",
            "conditions": "is_going_to_seven_6",
        },
        {
            "trigger": "advance",
            "source": "seven_6",
            "dest": "seven_7",
            "conditions": "is_going_to_seven_7",
        },
        #notice
        {
            "trigger": "advance",
            "source": "user",
            "dest": "notice",
            "conditions": "is_going_to_notice",
        },
        #go to home page
        {
            "trigger": "advance", 
            "source": [
                "seven_7",
                "one_1",
                "three_3",
                "notice",
            ], 
            "dest": "user",
            "conditions": "is_going_to_user",
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")
machines = {}

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)



@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machines[event.source.user_id].state}")
        print(f"REQUEST BODY: \n{body}")

        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_new_machine()

        response = machines[event.source.user_id].advance(event)
        
        if response == False:
            print("reach here\n")
            if machines[event.source.user_id].state == 'user':
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
            elif machines[event.source.user_id].state == "one_1" or machines[event.source.user_id].state == "three_1" or machines[event.source.user_id].state == "three_2" or machines[event.source.user_id].state == "three_3" or machines[event.source.user_id].state == "seven_1" or machines[event.source.user_id].state == "seven_2" or machines[event.source.user_id].state == "seven_3" or machines[event.source.user_id].state == "seven_4" or machines[event.source.user_id].state == "seven_5" or machines[event.source.user_id].state == "seven_6" or machines[event.source.user_id].state == "seven_7":
                if event.message.text == "觀看更多牌義":
                    machines[event.source.user_id].definition(event)

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine = create_new_machine()
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
