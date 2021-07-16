import numpy as np
import pandas as pd
# for Loop
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage
)


line_bot_api = LineBotApi(
    '3dPbSuIeWniyXniHMiO1R+iAwS+QPEvgTFs9ufpNDYJFvDNB8aknvQ5eVxw6TUaqiNjqwx+mt/E4EJz72zIxxBQxSZY6ZcDbfGfTzOyBktgQNum7Jsp1IWYD/223NbKbxxeybzJC+BHQwRPmxbxLBQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5b28ea727e5c7ffd890ebbcf8b1e1ece')
line_token = 'Ufc8cfcb89117f9b5b00770bf540bdcb3'


def flex1():
    jsonFlex = { }
    return jsonFlex


def flex2():
    jsonFlex = { }
    return jsonFlex


def lineFlex():
    flex_message2 = FlexSendMessage(
        alt_text='Python 01',
        contents=flex2()
    )
    line_bot_api.push_message(line_token, flex_message2)


if __name__ == "__main__":
    lineFlex()
