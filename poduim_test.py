
import numpy as np
import pandas as pd
import requests
import json
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
        "contents": mainProduct(
            googleId = "1nUE0YBP2jnKerVmeMz3fpF70qExD6hrPmGV80Q8ycWo",
            sheetId  = "products",
            categoryId = "Accessories",
            nameId   = None
        )
    } 

    flex_message2 = FlexSendMessage(
        alt_text='Python 01',
        contents=jsonFlex
    )
    line_bot_api.push_message(line_token, flex_message2)
 
def mainProduct(googleId=None, sheetId=None, categoryId=None, nameId=None):
    if googleId is not None:
        googleSheetId = googleId
    else:
        googleSheetId = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'

    sheetName = 'products'

    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)
   
    df['price'] = df['price'].str.replace(',', '').astype(float)

    if nameId is not None:
        df = df.loc[df['name'] == str(nameId)]

    if categoryId is not None:
        df = df.loc[df['category'] == str(categoryId)]
  
    json_body = [] 
    if not df.empty:
        for index, row in df.iterrows(): 
            content = flexProduct(
                data={
                    "images": row['images'],
                    "name": row['name'],
                    "price": row['price'],
                    "description": row['description'],
                    "category": row['category'],
                    "stock": row['stock'],
                    "Color": row['Color'],
                    "Size": row['Size'],
                }
            )
            json_body.append(content) 
    else:
        content = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "contents": [
                    {
                        "type": "text",
                        "text": "ไม่พบการค้นหา",
                        "wrap": True,
                        "weight": "bold",
                        "gravity": "center",
                        "size": "xl"
                    }
                ]
            }
        }
        json_body.append(content) 
    return json_body
 
def flexProduct(data):
    content = {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "image",
                    "url": str(data['images']),
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
                                    "text": str(data['name']),
                                    "size": "xl",
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
                                    "text": "ราคา " + str(data['price']),
                                    "size": "lg",
                                    "color": "#ffffff"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "สอบถาม",
                                        "text": 'สอบถามเพิ่มเติม: ' + str(data['name']),
                                    },
                                    "color": "#333333",
                                    "style": "primary",
                                    "margin": "xs"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "message",
                                        "label": "สั่งซื้อ",
                                        "text": 'สั่งซื้อ : ' + str(data['name']),
                                    },
                                    "style": "primary",
                                    "margin": "md"
                                }
                            ],
                            "position": "relative",
                            "spacing": "none",
                            "margin": "md"
                        }
                    ],
                    "offsetBottom": "0px",
                    "offsetStart": "0px",
                    "offsetEnd": "0px",
                    "backgroundColor": "#696969",
                    "paddingAll": "20px",
                    "paddingTop": "18px"
                },
                {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                            "type": "text",
                            "text": str(data['category']),
                            "color": "#ffffff",
                            "align": "center",
                            "size": "xs",
                            "offsetTop": "3px",
                            "offsetStart": "none"
                        }
                    ],
                    "position": "absolute",
                    "cornerRadius": "20px",
                    "offsetTop": "18px",
                    "backgroundColor": "#696969",
                    "offsetStart": "12px",
                    "height": "25px",
                    "width": "65px",
                    "alignItems": "center",
                    "borderWidth": "none",
                    "justifyContent": "center",
                    "offsetEnd": "none",
                    "paddingAll": "none",
                    "paddingTop": "none",
                    "margin": "none"
                }
            ],
            "paddingAll": "0px"
        }
    }
    return content
 
if __name__ == "__main__":
    lineFlex()