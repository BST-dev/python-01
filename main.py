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
        "contents": productsSearch()
    }

    flex_message2 = FlexSendMessage(
        alt_text='Python 01',
        contents=jsonFlex
    )
    line_bot_api.push_message(line_token, flex_message2)


def mainCategory(googleId=None, nameId=None):
    if googleId is not None:
        googleSheetId = googleId
    else:
        googleSheetId = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'

    sheetName = 'category'

    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)

    if nameId is not None:
        df = df.loc[df['name'] == str(nameId)]

    json_body = []
    if not df.empty:
        for index, row in df.iterrows():
            # print(row['name'], row['images'], row['price'])
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
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": str(row['name']),
                                                            "size": "xl",
                                                            "color": "#ffffff",
                                                            "weight": "bold"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "สินค้าขายดี",
                                                                    "color": "#ffffff",
                                                                    "align": "center",
                                                                    "size": "xs",
                                                                    "offsetTop": "3px"
                                                                }
                                                            ],
                                                            "position": "absolute",
                                                            "cornerRadius": "20px",
                                                            "offsetTop": "2px",
                                                            "backgroundColor": "#4682B4",
                                                            "height": "25px",
                                                            "width": "70px",
                                                            "offsetStart": "185px"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                        {
                                                            "type": "filler"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "ดูหมวดหมู่",
                                                            "color": "#ffffff",
                                                            "flex": 0,
                                                            "size": "xs",
                                                            "offsetTop": "6px",
                                                            "weight": "bold"
                                                        },
                                                        {
                                                            "type": "filler"
                                                        }
                                                    ],
                                                    "spacing": "sm",
                                                    "width": "125px",
                                                    "offsetStart": "20px"
                                                }
                                            ],
                                            "borderWidth": "1px",
                                            "cornerRadius": "4px",
                                            "spacing": "sm",
                                            "borderColor": "#ffffff",
                                            "margin": "xxl",
                                            "height": "40px",
                                            "backgroundColor": "#27ACB2",
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": str(row['name']),
                                            }
                                        }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "0px",
                                    "offsetStart": "0px",
                                    "offsetEnd": "0px",
                                    "backgroundColor": "#03303Acc",
                                    "paddingAll": "20px",
                                    "paddingTop": "18px"
                                }
                        ],
                    "paddingAll": "0px"
                }
            }
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


def myFunc(e):
    return e['confident']


def flexProduct(images, name, price, description, category, stock, Color, Size):
    content = {
        "type": "bubble",
        "body": {
                "type": "box",
            "layout": "vertical",
            "contents": [
                        {
                            "type": "image",
                            "url": str(images),
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
                                            "text": str(name),
                                            "size": "xl",
                                            "color": "#ffffff",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(price),
                                            "color": "#ffffff"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(description),
                                            "color": "#ffffff"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "จำนวน",
                                                    "color": "#ffffff"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": str(stock),
                                                    "offsetEnd": "10px",
                                                    "color": "#ffffff"
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
                                                            "width": "70%",
                                                            "height": "6px",
                                                            "backgroundColor": "#0D8186",
                                                            "position": "relative"
                                                        }
                                                    ],
                                                    "height": "6px",
                                                    "margin": "sm",
                                                    "backgroundColor": "#9FD8E36E",
                                                    "position": "relative",
                                                    "offsetTop": "8px",
                                                    "offsetEnd": "10px",
                                                    "width": "50%"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "สี",
                                                    "color": "#ffffff"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": str(Color),
                                                    "offsetEnd": "100px",
                                                    "color": "#ffffff",
                                                    "position": "absolute"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": "ไซส์",
                                                    "color": "#ffffff"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": str(Size),
                                                    "offsetEnd": "90px",
                                                    "color": "#ffffff"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "สั่งซื้อสินค้า",
                                                    "color": "#ffffff",
                                                    "flex": 0,
                                                    "offsetTop": "-2px",
                                                    "weight": "bold"
                                                },
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "spacing": "sm",
                                            "width": "100px",
                                            "action": {
                                                "type": "message",
                                                "label": "action",
                                                "text": 'สั่งซื้อ: ' + str(name),
                                            }
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
                                                    "layout": "vertical",
                                                    "contents": [
                                                        {
                                                            "type": "filler"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "flex": 0,
                                                            "text": "คลังสินค้า",
                                                            "color": "#ffffff",
                                                            "offsetBottom": "5px",
                                                            "offsetStart": "5px",
                                                            "weight": "bold"
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
                                            "spacing": "sm",
                                            "margin": "xxl",
                                            "height": "40px",
                                            "borderWidth": "1px",
                                            "borderColor": "#ffffff",
                                            "cornerRadius": "4px",
                                            "backgroundColor": "#FFD700",
                                            "width": "80px"
                                        }
                                    ],
                                    "borderWidth": "1px",
                                    "cornerRadius": "4px",
                                    "spacing": "sm",
                                    "borderColor": "#ffffff",
                                    "margin": "xxl",
                                    "height": "40px",
                                    "backgroundColor": "#27ACB2"
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
                                    "offsetTop": "-70px"
                                }
                            ],
                            "position": "absolute"
                        },
                {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": str(category),
                                    "color": "#ffffff",
                                    "offsetStart": "15px",
                                    "size": "sm"
                                }
                            ],
                            "position": "absolute",
                            "width": "100px",
                            "height": "25px",
                            "backgroundColor": "#ff334b",
                            "cornerRadius": "20px",
                            "borderColor": "#ffffff",
                            "borderWidth": "1px",
                            "offsetStart": "100px",
                            "margin": "100px",
                            "offsetTop": "185px"
                        }
            ],
            "paddingAll": "0px"
        }
    }

    return content


def productsSearch():
    url = 'https://chatbot-api-k56iahpiqa-as.a.run.app/productSearch-api'
    myobj = {
        "productImage": "https://storage.googleapis.com/chatbot-ecommerce/umber_shop/snap1.png"}
    res = requests.post(url, json=myobj)
    if(res.status_code == 200):
        rs = res.json()
        df = pd.json_normalize(rs['result'])
        df = df.loc[df['confident'] >= 0.3].groupby(
            ['category'], as_index=False).mean()
        # df  = df.sort_values(by='confident', ascending=False)
        df = df.head(3)

        googleSheetId = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'
        sheetName = 'products'
        url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            googleSheetId, sheetName)
        gg = pd.read_csv(url)

        json_body = []
        if not df.empty:
            for index, row in df.iterrows():
                nameId = str(row['category']).replace("%20", " ")
                products_df = gg.loc[gg['name'] == str(nameId)]
                if not products_df.empty:
                    products_dict = products_df.to_dict('records')
                    products_dict = products_dict[0]
                    content = flexProduct(products_dict['images'], products_dict['name'],
                                          products_dict['price'], products_dict['description'], products_dict['category'], products_dict['stock'], products_dict['Color'], products_dict['Size'])
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
            # print(row['name'], row['images'], row['price'])
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
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": str(row['name']),
                                                            "size": "xl",
                                                            "color": "#ffffff",
                                                            "weight": "bold"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "สินค้าขายดี",
                                                                    "color": "#ffffff",
                                                                    "align": "center",
                                                                    "size": "xs",
                                                                    "offsetTop": "3px"
                                                                }
                                                            ],
                                                            "position": "absolute",
                                                            "cornerRadius": "20px",
                                                            "offsetTop": "2px",
                                                            "backgroundColor": "#4682B4",
                                                            "height": "25px",
                                                            "width": "70px",
                                                            "offsetStart": "185px"
                                                        }
                                                    ]
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
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "text": str(row['description']),
                                                    "color": "#ebebeb",
                                                    "size": "sm",
                                                    "flex": 0
                                                }
                                            ],
                                            "spacing": "lg"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "contents": [
                                                        {
                                                            "type": "filler"
                                                        },
                                                        {
                                                            "type": "icon",
                                                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip14.png",
                                                            "offsetTop": "8px"
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "เพิ่มใส่ตะกร้า",
                                                            "color": "#ffffff",
                                                            "flex": 0,
                                                            "size": "xs",
                                                            "offsetTop": "6px",
                                                            "weight": "bold"
                                                        },
                                                        {
                                                            "type": "filler"
                                                        }
                                                    ],
                                                    "spacing": "sm",
                                                    "width": "125px",
                                                    "offsetStart": "20px",
                                                    "action": {
                                                        "type": "message",
                                                        "label": "action",
                                                        "text": str(row['name']),
                                                    }
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "text",
                                                                    "text": "คลังสินค้า",
                                                                    "flex": 0,
                                                                    "size": "xs",
                                                                    "weight": "bold",
                                                                    "color": "#FFFFFF",
                                                                    "offsetTop": "9px",
                                                                    "offsetStart": "10px"
                                                                }
                                                            ],
                                                            "spacing": "sm",
                                                            "width": "125px",
                                                            "offsetStart": "5px"
                                                        }
                                                    ],
                                                    "borderWidth": "1px",
                                                    "cornerRadius": "4px",
                                                    "spacing": "sm",
                                                    "height": "40px",
                                                    "width": "95px",
                                                    "margin": "40px",
                                                    "borderColor": "#ffffff",
                                                    "backgroundColor": "#FFD700"
                                                }
                                            ],
                                            "borderWidth": "1px",
                                            "cornerRadius": "4px",
                                            "spacing": "sm",
                                            "borderColor": "#ffffff",
                                            "margin": "xxl",
                                            "height": "40px",
                                            "backgroundColor": "#27ACB2"
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
                                    "backgroundColor": "#4682B4",
                                    "offsetStart": "75px",
                                    "height": "25px",
                                    "width": "150px"
                            }
                        ],
                    "paddingAll": "0px"
                }
            }
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


if __name__ == "__main__":
    lineFlex()
