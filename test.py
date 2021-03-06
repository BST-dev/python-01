import numpy as np
import pandas as pd
import requests
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


def lineFlex(request):
    try:
        request_json = request.get_json()
        if request.args and 'googleId' in request.args:
            # return request.args.get('message')
            googleId = request.args.get('googleId')
            sheetId = request.args.get('sheetId')
            nameId = request.args.get('nameId')
            categoryId = request.args.get('categoryId')
            if(sheetId == 'products'):
                contents = {
                    "type": "carousel",
                    "contents": mainProduct(googleId=googleId, sheetId=sheetId, categoryId=categoryId, nameId=nameId)
                }
            elif(sheetId == 'productSearch'):
                imageurl = request.args.get('imageurl')
                contents = {
                    "type": "carousel",
                    "contents": productsSearch(imageurl)
                }
            else:
                contents = {
                    "type": "carousel",
                    "contents": mainCategory(googleId=googleId, nameId=nameId)
                }
        elif request_json and 'message' in request_json:
            return request_json['message']
        else:
            return {"message": 'error', "detail": 'Parameter not found'}

        jsonFlex = {"response_type": "object"}
        jsonFlex["line_payload"] = [
            {
                "type": "flex",
                "altText": "ข้อมูล",
                "contents": contents
            }
        ]
        headers = {
            'Response-Type': 'object'
        }
        return (jsonFlex, 200, headers)

    except Exception as e:
        print(e)
        return {"message": 'error', "detail": str(e)}


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
            content = flexCategory(row['images'], row['name'])
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
    else:
        df = df.loc[df['category'] == 'เดรส']

    json_body = []

    if not df.empty:
        for index, row in df.iterrows():
            # print(row['name'], row['images'], row['price'])
            content = flexProduct(row['images'], row['name'],
                                  row['price'], row['description'], row['category'], row['stock'], row['Color'], row['Size'])
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


def flexCategory(images, name):
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
                                                    "text": "ดูสินค้า",
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
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "backgroundColor": "#03303Acc",
                            "paddingAll": "20px",
                            "paddingTop": "18px",
                            "action": {
                                "type": "message",
                                "label": "action",
                                "text": str(name),
                            }
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
                        }
            ],
            "paddingAll": "0px"
        }
    }
    return content 

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


def productsSearch(imageurl):
    print(imageurl)
    url = 'https://chatbot-api-k56iahpiqa-as.a.run.app/productSearch-api'
    myobj = {"productImage": str(imageurl)}
    res = requests.post(url, json=myobj)
    if(res.status_code == 200):
        rs = res.json()
        df = pd.json_normalize(rs['result'])
        df = df.loc[df['confident'] >= 0.3]
        # df  = df.sort_values(by='confident', ascending=False)
        df = df.head(4)

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
