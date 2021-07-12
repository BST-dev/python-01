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

def main():
    googleSheetId = '15-oS5W-cV3UHZMT3Mzaawhz59EH9NGiFyK0AzTNKzJw'
    sheetName = 'Products'
    url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId, sheetName)
    df = pd.read_csv(url)
    df['price'] = df['price'].str.replace(',', '').astype(float)

    # df = df.loc[df['price'] > 2000]

    print(df.info())



if __name__ == "__main__":
    main()
