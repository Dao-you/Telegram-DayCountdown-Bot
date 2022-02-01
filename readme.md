# 倒數日子 Telegram 機器人

本程式以 **2023 年大學學科能力測驗**作為範例。

## 套件安裝

本機器人共使用兩個需要額外安裝的套件

分別是用來傳送 Telegram Bot API 請求的 requests

和用來繪製圖片的 Pillow (俗稱 PIL，不過正牌 PIL 已停止維護)

第一次使用需要額外到終端機中執行安裝。

```shell
pip install Pillow requests
```

## 機器人 API 資訊設定

在開始使用機器人之前，您必須先取得一些 API 資訊：
1. 建立一個 Telegram Bot 並**取得 Token**。
1. 取得聊天室 chat ID 
(群組、頻道及個人聊天室均可，但務必注意機器人帳號**擁有發言權限**)

取得資訊之後，在程式碼的 ``TelegramBottoken = `` 、 ``
TelegramChatID = `` 後方以字串形式填入相關資訊，它看起來會長得像這樣：

```python
# 機器人 API 資訊
TelegramBottoken = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
TelegramChatID   = "-1401592845274"
```

至於如何取得這些資訊，這不在這篇說明的範圍
不過如果你不知道的話，我還是很好心的幫你準備了連結：

1. 取得 Token：[Telegram 建立機器人 圖文教學](https://tgtw.cc/post-create-telegram-bot)
1. 取得 ChatID：[[Telegram] Telegram(五) 取得 Chat ID](http://blog.3dgowl.com/telegram-telegram%E4%BA%94-%E5%8F%96%E5%BE%97-chat-id/)

## 日期設定

你可以在程式碼中找到一個稱為 ``GSAT`` 的變數，只要改變後方函數內的 ``year``、``month``、``day`` 三個數值即可改變日期。

```python
# 天數計算
today = datetime.date.today()
GSAT = datetime.date(year=2023, month=1, day=13)
print((GSAT - today).days)
```

## 其他需要注意的事情

1. 送出訊息後，Console 會列印出 Telegram 那邊回傳回來的偵錯訊息，顯示 ``<response [200]>`` 為成功送出。
1. 程式中留有一個未使用的函數 ``telegram_bot_sendtext`` 以備不時之需，如果需要的話可以順便給你拿去用。
1. 如果你用了 ``telegram_bot_sendtext`` 函數，Telegram 那邊返回回來的偵錯訊息就有些複雜了，不過其實主要看最前面顯示發送有沒有成功就好。
1. 有任何問題或建議歡迎[來信](mailto:qaz00639@gmail.com)與我討論。(qaz00639@gmail.com)
1. 作者長得超帥的

## 相關文件

這裡是一些套件的相關使用方式，如果你想要修改程式的話，可以當作工具書查閱。

1. [Telegram Bot API sendMessage](https://core.telegram.org/bots/api#sendmessage)
1. [Telegram Bot API sendPhoto](https://core.telegram.org/bots/api#sendmessage)
1. [Pillow documentation](https://pillow.readthedocs.io/en/stable/)