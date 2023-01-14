from pyrobogui import robo, pag
import pyperclip as pc
import datetime

now = datetime.datetime.now()

def remove_text_inside_brackets(text, brackets="<>"):
    count = [0] * (len(brackets) // 2) # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b: # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1)**is_close # `+1`: open, `-1`: close
                if count[kind] < 0: # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else: # character is not a [balanced] bracket
            if not any(count): # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)

def getMsg():
    position = robo.imageNeddle('./images/msgBox.png', imageNr='last')
    robo.rightClick(x=position[0], y=position[1], offsetRight=6)
    robo.click(image='./images/inspect.png')
    robo.rightClick(image='./images/div.png',full_match=True)
    robo.click(image='./images/copy.png')
    robo.click(image='./images/copyElement.png')
    message = pc.paste()
    message = repr(remove_text_inside_brackets(message))
    msgTime = now.strftime('%I')[0]
    if msgTime == '0':
        message = message[1:-15]
    else:
        message = message[1:-17]
    pag.hotkey('f12')
    return message

def getSender():
    position = robo.imageNeddle('./images/options.png', imageNr='last')
    robo.rightClick(x=position[0], y=position[1], offsetLeft=150)
    robo.click(image='./images/inspect.png')
    robo.rightClick(image='./images/span.png',full_match=True)
    robo.click(image='./images/copy.png')
    robo.click(image='./images/copyElement.png')
    sender = pc.paste()
    sender = repr(remove_text_inside_brackets(sender))
    sender = sender.replace("'", "").replace("+", "")
    pag.hotkey('f12')
    return sender

msg = getSender()
print(msg)