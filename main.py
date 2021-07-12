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


# def Credentials_gg():
#     SCOPES = ['https://www.googleapis.com/auth/drive',
#               'https://www.googleapis.com/auth/bigquery']
#     credentials = service_account.Credentials.from_service_account_info(
#         {
#             "type": "service_account",
#             "project_id": "pythontrading",
#             "private_key_id": "23362b26aae271e7b0e95ecb0fd72f1a7b8a4711",
#             "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuN4MPrmgVnUDB\nLezkCxavipqtPZft6LC/DJHMxrbtPUJJFHEtwMV+eM0zamFP5qyiSBfHCDRGrbq8\nJRjhL6cDbjR2BUpPtntqoBJIzzr35Y9hYk18BPcShm+cvwaltPgq7hvk6fNK8NfL\nh+j3yWmtaPtoLWd9cCkWSXpt2jtKZGWLxkAKDEZGrU01jImWC1EI6fFBc3Yhpk8R\nC1IiUBkLvLnAvu0uWOQ3Az3iqvHrA90YaqNJSg2+I31z/K5kciPVa/Nb3amdOoIh\n8VHU2QOPICPkekeQrADVSnGMxo4tTyoHrN/Yj0U/G9T+LUSLKrgp/5SuNSOfrJoG\nsPVMZc0lAgMBAAECggEABqPHezbEsUQxxlsLewKALhcMf5tIGdFjQRjHysPtD1wl\nFVdx29JLxJ7yhSniBRNP04yHWXbS1TnEUuzgBp8UELGnzrKzaxfTmtP4dm1tfCqz\n3PyL4vTmfL6CbPkr1e9wgORbzEztUJcexltK8fyraihE4qrOVa3LZxXMVHj7hwF9\n6vzN/xbTF9am8FoDN40C6HxHzGFHTf7BjgrAtgP7ZJdonWPoI9k0bhHk/ZZLfxTo\nrTCqeyRNypjiX4MOS3W2xZaqPb+pcjAw00fc68Y90F4eOZ9zNAjxUuDsYW9d7zGc\nnBfhg5izAOFahawTfkE9QVLSfDcO7FYAjPkK4gjcSQKBgQDg/+kBU2a1E2X6ArkE\nkueT1st9PnpNFWlurVaqBjvX0wvgbKgmgfDiGq/NPYnl5ioRKHXakhYVwhQqcfPb\no5g0QAerHzS1izk9DOHN+oUjagoeWhDQUq9gl3mAUuiTkPPW3KcEq74dS/rCJvOd\nyh6B9sAJhvhDy9sMBNjYMRWtCQKBgQDGOGmpNrqpctmUIIK/qC4RwJBYHgX6g47k\nDHQI9oWEoNFRXhRqZ38DzJre9EZsJMlsMw2yn2VGONHbicrwEIM0JT7+ESl1bk+S\nkb+ttPPbXifR9l6ekzhD6g4ASALjuSBwBjQYQ0Q+njQR/hXWyf3wS0ZT4WkV5yVh\nHkAoebWCPQKBgQDd8NFgc2pOl5Hx6Zmjv10bYbdcFbMCMmrLt8RS9s8094MxnzzG\nr0pzXiun4loSItXAEw8dyRhr4gOOUtVfBKJwd/CYhbGymmCdrgVW7xVBd6n/gowv\nUkCYoRJC2IV+em9stD8zxk1EDNyPg2ivbt5lCIcpXq+qAH5T/rv/lXtyMQKBgCYb\nPDzal6HxwWBXq6sastiY02cNRor1dafjuP7sHZj0rajd1EDsap+ZWwCXp14s6EgT\nvINlXzvTuoxg/hGOqxqAOo7vT7ASp9t+h4Hmcqbuf+s+WMxVcxCjU1O8hEmxEkpW\n9vbfH6SGF26KETq8lEP4xKllgSVDzYzRGvZtB3blAoGAISRAd2TQwt4DM/yHTdp7\n7CIk2iAubqYG4pevUKZP28soV5CgX1pVyfwB73mca8yjRcTHBukN5zO3AuMXO4HV\nr7KNw+Gk9HyyYae6DCt6p9++D1Wnm5OUC8p1jPZY8uf+OODdOys64vphat6Kk7UX\nRhmJ9HdLwGvCflKtjtQ+b1k=\n-----END PRIVATE KEY-----\n",
#             "client_email": "ptp-colab-df2bigquery@pythontrading.iam.gserviceaccount.com",
#             "client_id": "109785944474523033400",
#             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#             "token_uri": "https://oauth2.googleapis.com/token",
#             "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#             "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/ptp-colab-df2bigquery%40pythontrading.iam.gserviceaccount.com"
#         }, scopes=SCOPES
#     )
#     return credentials


# def con():


def main():
    googleSheetId = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'
    sheetName = 'Products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)
    json_body = []
    for index, row in df.iterrows():
            y = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip1.jpg",
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
                                            "text": "Brown's T-shirts",
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
                                            "text": "¥35,800",
                                            "color": "#ebebeb",
                                            "size": "sm",
                                            "flex": 0
                                        },
                                        {
                                            "type": "text",
                                            "text": "¥75,000",
                                            "color": "#ffffffcc",
                                            "decoration": "line-through",
                                            "gravity": "bottom",
                                            "flex": 0,
                                            "size": "sm"
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
                                    "text": "SALE",
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
            json_body.append(y)  

    json_text2 = {
        "type": "carousel",
        "contents": json_body
    }
    flex_message2 = FlexSendMessage(
        alt_text='HongLong Model',
        contents=json_text2
    )
    line_bot_api.push_message(pulimz_line, flex_message2)


if __name__ == "__main__":
    main()
