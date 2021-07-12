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


def lineFlex():
    jsonFlex = {
        "type": "carousel",
        "contents": main()
    }
    flex_message2 = FlexSendMessage(
        alt_text='Python 01',
        contents=jsonFlex
    )
    line_bot_api.push_message(line_token, flex_message2)


def main():
    googleSheetId_tee = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'
    googleSheetId_no = '1nUE0YBP2jnKerVmeMz3fpF70qExD6hrPmGV80Q8ycWo'
    sheetName = 'Products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId_no, sheetName)

    df = pd.read_csv(url)
    df['price'] = df['price'].str.replace(',', '').astype(float)

    # df = df.loc[df['price'] > 2000]
    # df = df.loc[df['category'].isin(['เสื้อแขนยาว'])]
    df = df.loc[df['category'] == 'เตียงนอน']

    json_body = []
    for index, row in df.iterrows():
        print(row['name'], row['images'], row['price'])
        content = {
            "type": "bubble",
            "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": str(row['images']),
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "2:3",
                            "gravity": "top"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(row['name']),
                                            "size": "sm",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(row['price']),
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0
                                        }
                                    ],
                                    "spacing": "lg"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "icon",
                                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "Add to cart",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm"
                                        },
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#9C8E7Ecc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(row['category']),
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "offsetTop": "3px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "18px",
                            "backgroundColor": "#ff334b",
                            "offsetStart": "18px",
                            "height": "25px",
                            "width": "53px"
                        }
                    ],
                "paddingAll": "0px"
            }
        } 
        json_body.append(content) 
   
    return json_body


if __name__ == "__main__":
    lineFlex()
