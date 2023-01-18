import pyperclip as pc
import arabic_reshaper
from langdetect import detect_langs
import datetime
import gspread



now = datetime.datetime.now()

# connect to google sheets
service_account = gspread.service_account(filename='gs_account.json')
sheet = service_account.open('Ai workflow')
otl = sheet.worksheet('OrdersTaskList')

def process_message(msg, created_by):
    new_msg = str(msg)
    try:
        ##### If it's a Quotation #####
        if new_msg[2] == '1':
            if otl.find(msg, in_column=5) is None:
                otlTime = now.strftime("%d/%m/%Y %I:%M %p")
                otlDefault = {'Created by': '', 'Create DateTime': otlTime, 'Customer Name': '', 'Customer': '', 'Quotation': '', 'Need Approval': '', 'Brand Managers': '', 'Financial': '', 'Approved': '', 'Creditlimit': '', 'Branch Manager': '', 'CL Financial': '', 'CL Approved': '', 'Finished Date': ''}
                otlUpdate = {'Created by': created_by, 'Quotation': msg}
                otlUpdate = dict(otlDefault, **otlUpdate)
                otlData = list(otlUpdate.values())
                otl.append_row(otlData, value_input_option='USER_ENTERED')
                return pc.copy("تم اضافة الطلبية وجاري العمل على المطلوب")
            else:
                return pc.copy("الطلبية مكررة")
    except:
        textlang = str(detect_langs(msg))
        ##### Arabic Response #####
        if textlang.find('ar') == 1:
            new_msg = arabic_reshaper.reshape(new_msg)[::-1]
            if new_msg in [
                arabic_reshaper.reshape("هلا")[::-1],
                arabic_reshaper.reshape("اهلا")[::-1],
                arabic_reshaper.reshape("الو")[::-1],
                arabic_reshaper.reshape("مرحبا")[::-1],
                ]:
                return pc.copy("هلا ومرحبا")
            elif new_msg in arabic_reshaper.reshape("السلام عليكم")[::-1]:
                return pc.copy("وعليكم السلام ورحمة الله وبركاته")
        
        ##### English Response #####
        elif textlang.find('en') == 1:
            new_msg = msg.lower()
            if new_msg in ("hi"):
                return pc.copy("Hey!")
            elif new_msg in ("hello"):
                return pc.copy("hi2")
        else:
            return pc.copy("I don't understand")
        
        

    
