import re
from time import sleep

import pyautogui as pag
import pygetwindow as gw
from pyrobogui import robo
import pywinauto


def isOpen(appName):
    # Check that appName is a non-empty string
    if not isinstance(appName, str) or appName == "":
        raise ValueError("appName must be a non-empty string")

    # Compile a regular expression to search for appName in the window titles
    pattern = re.compile(appName, re.IGNORECASE)

    # Search for the pattern in the window titles
    matches = [pattern.search(title) for title in gw.getAllTitles()]

    # Check if any of the window titles contain appName
    running = any(matches)

    return running

def launchApp(appName):
    # Check if the app is already running
    if not isOpen(appName):
        # Press the start key
        pag.press("win")

        # Type the name of the app
        pag.typewrite(appName)

        # Press Enter to launch the app
        pag.press("enter")

def showWindow(appName):
    if any(appName in x for x in gw.getAllTitles()):
        window = gw.getWindowsWithTitle(appName)[0]
        if window.left < 0 or window.top < 0:
            # The window is minimized or hidden, so we need to restore it
            window.restore()
        window.activate()
        return True

def sapRT():
    robo.waitImageToAppear(image='./images/SAP/getRT_position.png')
    ms_position = pag.locateOnScreen(image='./images/SAP/getRT_position.png')
    while not pag.locateOnScreen(image='./images/SAP/zeroRT.png') or not pag.locateOnScreen(image='./images/SAP/lastRT.png'):
        pag.screenshot('./images/SAP/lastRT.png', region=(ms_position.left, ms_position.top, 120, 25))
        break

def startSAPSeasion(username, password):
    launchApp("SAP Logon")
    robo.doubleClick(image='./images/SAP/khairatProduction.png')
    robo.click(image='./images/SAP/SAP.png')
    activeWindow = gw.getActiveWindow()
    activeWindow.resizeTo(960, 1030)
    activeWindow.moveTo(0, 0)
    sapRT()
    pag.typewrite(username)
    pag.press('tab')
    pag.typewrite(password)
    pag.press('enter')
    sapRT()
    if pag.locateOnScreen('./images/SAP/keepLoggedUsers.png') is not None:
            robo.click(image='./images/SAP/keepLoggedUsers.png')
            robo.click(image='./images/SAP/greenEnter.png')
    sapRT()

def startWhatsApp():
    launchApp("Google Chrome")
    activeWindow = gw.getActiveWindow()
    activeWindow.resizeTo(965, 1039)
    activeWindow.moveTo(961, 0)
    robo.click(image='./images/Chrome/home.png', offsetRight=100)
    pag.typewrite('https://web.whatsapp.com/')
    pag.press('enter')
    robo.waitImageToAppear(image='./images/Chrome/waNoChatOpen.png')




startSAPSeasion('M-Hamed', '987951357')
startWhatsApp()