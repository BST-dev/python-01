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
pulimz_line = 'Ufc8cfcb89117f9b5b00770bf540bdcb3'
honglong_group = 'Ce659b5d6661a97b7a59bf85c32ee7f41'

line_notitoken = 'ieSRB8aSJJnYkLIyNAshhQ13HoQ4ntd4XyYYC4EIO0t'  # group พี่ตั้ว
line_token = pulimz_line  # group พี่ตั้ว


def lineFlex():

    jsonline = {
        "type": "carousel",
        "contents": main()


    }
    flex_message2 = FlexSendMessage(
        alt_text='Python Model',
        contents=jsonline
    )
    line_bot_api.push_message(line_token, flex_message2)


def main():
    googleSheetId_Tee = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'
    googleSheetId_No = '1nUE0YBP2jnKerVmeMz3fpF70qExD6hrPmGV80Q8ycWo'
    sheetName = 'category'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId_Tee, sheetName)
    df = pd.read_csv(url)
    df['name'] = df['name'].astype(str)

    # df = df.loc[df['price'] > 2000]
    # df = df.loc[df['category'] == 'เสื้อสายเดี่ยว']

    json_body = []
    for index, row in df.iterrows():
        print(row['name'], row['images'])
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
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "จำนวน 100 ชิ้น",
                                            "color": "#ffffff"
                                        },
                                        {
                                            "type": "text",
                                            "text": "สี",
                                            "color": "#ffffff",
                                            "margin": "10px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "ไซส์",
                                            "color": "#ffffff",
                                            "margin": "5px"
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
                                                            "type": "filler"
                                                        }
                                                    ],
                                                    "position": "absolute",
                                                    "width": "70%",
                                                    "height": "6px",
                                                    "backgroundColor": "#0D8186"
                                                }
                                            ],
                                            "margin": "sm",
                                            "height": "6px",
                                            "backgroundColor": "#9FD8E36E",
                                            "width": "300px",
                                            "position": "absolute",
                                            "offsetTop": "52px"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": []
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [],
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
                                                    "type": "text",
                                                    "text": "สั่งซื้อ",
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
                                    "height": "40px",
                                    "backgroundColor": "#27ACB2"
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "icon",
                                            "url": "https://scontent.fbkk22-2.fna.fbcdn.net/v/t1.15752-9/216840953_517710789434953_8873452753647982621_n.png?_nc_cat=107&ccb=1-3&_nc_sid=ae9488&_nc_eui2=AeF31Srr976NH4NkpbWWS53NJ-8Myki6I_sn7wzKSLoj-_biEelqOsWNJ9-SD4AeJJI9LC3NSzPA98NPMyz1Vkxl&_nc_ohc=nplEFEXyD2AAX93xriG&tn=1adk_vDV4BDsPNxw&_nc_ht=scontent.fbkk22-2.fna&oh=bca17627ca89f351bce1a4d20d3be483&oe=60FB5B60",
                                            "margin": "50px",
                                            "size": "md",
                                            "offsetTop": "82px"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-0/p206x206/50010200_377499006140576_5122118206969872384_n.png?_nc_cat=110&ccb=1-3&_nc_sid=aee45a&_nc_eui2=AeGo7M9tZsevvvVc-tOw-lkKAOEwN6_enLUA4TA3r96ctdhbi5PZ8m1zBiMyfCOYXkUwjCbvrY8W8XWpIn2rTxs5&_nc_ohc=c2oLOZgyA_0AX-H2lwH&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=c77340875e64e00d0b83ff5acca7663c&oe=60FB9921",
                                            "size": "md",
                                            "margin": "10px",
                                            "offsetTop": "82px"
                                        },
                                        {
                                            "type": "icon",
                                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-0/p206x206/219846826_544090160172367_1044884041858372102_n.png?_nc_cat=102&ccb=1-3&_nc_sid=aee45a&_nc_eui2=AeFthHr3WxBtDOOBVFEslzMtetXaztbyuWV61drO1vK5ZdMsoP8kqmpGBluYzCopilp9lrF0OPGbk6NG8hf0I5wq&_nc_ohc=tLoeKAZvTCYAX84N7xF&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=e3c5e1d48a2c0500fc451c1f01241195&oe=60FAE534",
                                            "margin": "10px",
                                            "offsetTop": "82px"
                                        }
                                    ],
                                    "position": "absolute",
                                    "height": "500px",
                                    "width": "500px"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "M",
                                            "color": "#ffffff",
                                            "offsetTop": "105px",
                                            "margin": "10px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "L",
                                            "color": "#ffffff",
                                            "offsetTop": "105px",
                                            "offsetEnd": "10px"
                                        },
                                        {
                                            "type": "text",
                                            "text": "XL",
                                            "color": "#ffffff",
                                            "offsetTop": "105px",
                                            "offsetEnd": "20px"
                                        }
                                    ],
                                    "position": "absolute",
                                    "margin": "20px",
                                    "width": "150px",
                                    "height": "150px",
                                    "offsetStart": "60px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "icon",
                                    "url": "https://scontent.xx.fbcdn.net/v/t1.15752-0/s240x240/217898746_892520454670864_1103978059929240061_n.png?_nc_cat=109&ccb=1-3&_nc_sid=aee45a&_nc_eui2=AeHui9Mplf5McR-ctiAR9NBEaRzHlVU1erRpHMeVVTV6tBEWWH6ikwJ4hhlYQABBXIHBa4FRLZo3wC2XD8Cfhg9f&_nc_ohc=JrrOcdv4hh4AX8pKlf0&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=938d5ce96127c1780318e4248483c00e&oe=60FAA4C7",
                                    "margin": "40px",
                                    "size": "200px",
                                    "offsetTop": "-60px"
                                }
                            ],
                            "position": "absolute"
                        }
                    ],
                "paddingAll": "0px"
            }
        }
        json_body.append(content)

    return json_body


if __name__ == "__main__":
    lineFlex()
