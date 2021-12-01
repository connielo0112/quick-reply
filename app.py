# 載入LineBot所需要的套件
import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(
    'HwJGPBlbe+C9YJAHihd4OPUc6fodiqnbYalhEklIOREBDLicUFj4TOzB0DeEeQ0HP1zJaHUlCibXXYm1zwL6a6To+l1ryjFk6/hHPbLvUhAml4cupsmfp18nclVpjYCnETSc4s7fRCvQ0WSeDqNUWAdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('44e98bf21462eaad3fb5bc068132823d')
line_bot_api.push_message(
    'U7eedc283198389e2aa9eed436d81099a', TextSendMessage(text='你可以開始了'))
# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
# get request body as text body = request.get_data(as_text=True) app.logger.info("Request body: " + body) # handle webhook body try:     handler.handle(body, signature) except InvalidSignatureError:     abort(400) return 'OK'
# 訊息傳遞區塊
# 基本上程式編輯都在這個function


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text = event.message.text
    if re.match('告訴我秘密', message):
        flex_message = TextSendMessage(text='以下有雷，請小心',
                                       quick_reply=QuickReply(items=[
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(action=MessageAction(
                                               label="別按我", text="你按屁喔！爆炸了拉！！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！")),
                                           QuickReplyButton(
                                               action=MessageAction(label="按我", text="按！"))
                                       ]))
        line_bot_api.reply_message(event.reply_token, flex_message)
    else:
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(message))


# 主程式
if name == "main":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
