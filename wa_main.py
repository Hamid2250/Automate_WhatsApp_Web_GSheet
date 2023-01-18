import re
from pyrobogui import robo, pag
import pyperclip as pc
import datetime
from replays import process_message
from time import sleep

now = datetime.datetime.now()

def getMsg():
    position = robo.imageNeddle('./images/msgBox.png', imageNr='last')
    robo.rightClick(x=position[0], y=position[1], offsetRight=6)
    robo.click(image='./images/inspect.png')
    robo.rightClick(image='./images/div.png',full_match=True)
    robo.click(image='./images/copy.png')
    robo.click(image='./images/copyElement.png')
    message = pc.paste()
    message = re.sub("<[^>]*>", "", message)
    msgTime = now.strftime('%I')[0]
    if msgTime == '0':
        message = message[0:-14]
    else:
        message = message[0:-17]
    pag.hotkey('f12')
    return message

def getSender():
    position = robo.imageNeddle('./images/options.png', imageNr='last')
    robo.rightClick(x=position[0], y=position[1], offsetLeft=150, offsetUp=5)
    robo.click(image='./images/inspect.png')
    sleep(1)
    robo.rightClick(image='./images/span.png',full_match=True)
    robo.click(image='./images/copy.png')
    robo.click(image='./images/copyElement.png')
    sender = pc.paste()
    sender = re.sub("<[^>]*>", "", sender)
    sender = sender.replace("'", "").replace("+", "")
    pag.hotkey('f12')
    return sender

def sendMessage(message):
    robo.click(image='./images/paperclip.png', offsetRight=50)
    pag.hotkey('ctrl', 'v')
    pag.typewrite('\n')
    position = robo.imageNeddle('./images/options.png', imageNr='last')
    robo.click(x=position[0], y=position[1])
    robo.click(image='./images/closeChat.png')

while True:
    if pag.locateOnScreen(image='./images/newMsg.png', confidence=0.8) is not None:
        robo.click(image='./images/newMsg.png', offsetLeft=80, timeout=-1)
        robo.waitImageToAppear(image='./images/paperclip.png')
        msg = getMsg()
        created_by = getSender()
        sendMessage(process_message(msg, created_by))

