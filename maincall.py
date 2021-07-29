import numpy as np
import pandas as pd
import requests
import json


def myFunc(e):
    return e['confident']


def flexProduct(images, name, price, description, category,stock,Color,Size):
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
                                            "width": "100px"
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
    myobj = {"productImage": "https://storage.googleapis.com/chatbot-ecommerce/umber_shop/snap1.png"}
    res = requests.post(url, json=myobj)

    print(res)
    print('xxxxxxx')
    if(res.status_code == 200):
        rs = res.json()
        df = pd.json_normalize(rs['result'])

        print(df)
        # df  = df.loc[df['confident'] >= 0.3].groupby(['category'], as_index=False).mean()
        df = df.loc[df['confident'] >= 0.3]
        # df  = df.sort_values(by='confident', ascending=False)
        df = df.head(4)
        print(df)

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


if __name__ == "__main__":
    productsSearch()
