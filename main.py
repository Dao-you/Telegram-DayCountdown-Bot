import datetime
import requests
import os

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
# $pip install Pillow requests

# 機器人 API 資訊
TelegramBottoken = ""
TelegramChatID   = ""

# 防呆裝置
if TelegramBottoken == "" or TelegramChatID == "":
    print("請記得在程式碼中輸入 Telegram Bot API 資訊")
    os._exit

# 傳送 Telegram 訊息 (Not in use)
def telegram_bot_sendtext(bot_message):
    
    parse_mode = ""
    disable_notification = "True"
    send_text  = f'https://api.telegram.org/bot{TelegramBottoken}/sendMessage?chat_id={TelegramChatID}&parse_mode={parse_mode}&text={bot_message}&disable_notification={disable_notification}'

    response = requests.get(send_text)

    return response.json()

# 傳送 Telegram 圖片
def telegram_bot_sendphoto(caption, photo):

    url = f"https://api.telegram.org/bot{TelegramBottoken}/sendPhoto?chat_id={TelegramChatID}&caption={caption}"
    response = requests.post(url, 
               files={'photo': ('photo.png',photo,'image/png')})
    return response


# 將天數寫在圖片上
def write_it(day):
    
    pixel     = 1280
    bgcolor   = (255,255,255)
    fontcolor = (0,0,0)

    image     = Image.new("RGB",(pixel,pixel),bgcolor)
    dayfont   = ImageFont.truetype("GenJyuuGothic-Heavy.ttf",int(pixel*0.50) )
    titlefont = ImageFont.truetype("GenJyuuGothic-Heavy.ttf",int(pixel*0.08) )

    draw = ImageDraw.Draw(image)

    # 天數繪製
    w, h = draw.textsize(text=day, font=dayfont)
    draw.text( ( (pixel - w) // 2, int(pixel*0.08) ) ,
        day, font=dayfont, fill=fontcolor)

    # 標題繪製
    w, h = draw.textsize(text="2023 GSAT", font=titlefont)
    draw.text(( (pixel-w)//2 , int(pixel*0.66) ), 
        text="2023 GSAT", font=titlefont, fill=fontcolor)

    del draw

    return image

# 天數計算
today = datetime.date.today()
GSAT = datetime.date(year=2023, month=1, day=13)
print((GSAT - today).days)

# 製作圖片並以 BytesIO 儲存
byte_io = BytesIO()
write_it(f"{(GSAT - today).days}").save(byte_io, 'png')
byte_io.seek(0)

# 訊息傳送
print(telegram_bot_sendphoto(f"距離學測還剩下{(GSAT - today).days}天", byte_io))