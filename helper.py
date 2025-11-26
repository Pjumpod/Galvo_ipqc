import datetime
import os
import tkinter as tk
from MyDialog import MyDialog


def datetime_format(datetime_input: datetime):
    return datetime_input.strftime("%Y-%m-%dT%H:%M:%S")


def format_timenow():
    now = datetime.datetime.now()
    return datetime_format(now)


def format_datenow():
    now = datetime.datetime.now()
    return now.strftime("%Y%m%d")


def fillbox(message, title=None, size="400x200"):
    root = tk.Tk()
    root.withdraw()
    try:
        x = MyDialog(root, title, message, size).result
    except TypeError:
        x = "STOP"
    if x is None:
        x = "STOP"
    root.destroy()
    return x


def username():
    en = fillbox("You are currently not logged in\n\rEnter your ID", "EN", "500x300")
    en_str = ""
    if len(en) == 6:
        en_str = en
    else:
        username()
    return en_str


def excel(starttime: str, unit_sn: str, seq_name: str, final_result: str, operator: str,
          Parameter1: tuple, Parameter2: tuple, Parameter3: tuple, Parameter4: tuple, Parameter5: tuple,
          Parameter6: tuple, Parameter7: tuple, Parameter8: tuple, Parameter9: tuple, Parameter10: tuple):
    timenow = format_timenow()
    _, seq_f = os.path.split(seq_name)
    seq_f = seq_f[::-1]
    ft = seq_f.split('.')
    seq_f = ft[1]
    seq_f = seq_f[::-1]
    seq_f = seq_f.strip()
    final_result = final_result.replace("ed", "").replace("ED", "").upper()
    seq_f_trim = seq_f.replace(" ", "_")
    logfile_path = "C:\\Report\\" + seq_f_trim + "_sum_" + format_datenow() + ".csv"
    csv_exist = os.path.isfile(logfile_path)
    content = unit_sn + ", " + starttime + ", " + timenow + ", " + final_result + ", " + operator + ", " + seq_f
    if csv_exist:
        title = ""
        max = ""
        min = ""
    else:
        title = "SN, START TIME, STOP TIME, RESULT, OPERATOR, TEST"
        max = ", , , , , MAX VALUE"
        min = ", , , , , MIN VALUE"
    loop = range(1, 6)
    for i in loop:
        if i == 1:
            Parameter = Parameter1
        elif i == 2:
            Parameter = Parameter2
        elif i == 3:
            Parameter = Parameter3
        elif i == 4:
            Parameter = Parameter4
        elif i == 5:
            Parameter = Parameter5
        elif i == 6:
            Parameter = Parameter6
        elif i == 7:
            Parameter = Parameter7
        elif i == 8:
            Parameter = Parameter8
        elif i == 9:
            Parameter = Parameter9
        else:
            Parameter = Parameter10
        if "dummy" not in Parameter[0].lower():
            if not csv_exist:
                title += ", " + Parameter[0]
                if Parameter[3].lower() != "string":
                    max += ", " + str(Parameter[6])
                    min += ", " + str(Parameter[5])
                else:
                    max += ", "
                    min += ", "
        if Parameter[1] != "":
            content += ", " + str(Parameter[4])
    file_id = open(logfile_path, 'a+')
    if not csv_exist:
        file_id.write(title + '\n')
        file_id.write(max + '\n')
        file_id.write(min + '\n')
    file_id.write(content + '\n')
    file_id.close()
    return logfile_path
