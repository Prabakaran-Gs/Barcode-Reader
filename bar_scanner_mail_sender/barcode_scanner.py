import cv2
import time
# import sqlite3
import csvwriter
import mailsending
from datetime import datetime
from pyzbar.pyzbar import decode
#modules setup
# csvwriter.fi_cre()

image_code=cv2.VideoCapture(0)
image_code.set(3,640) #width
image_code.set(4,480) #height
camera=True
student_dict={}
#Camera startup and importation 
si_no=1
while camera==True:
    success,frame=image_code.read()
    for code in decode(frame):
        co_id=code.data.decode('utf-8')
        timestamp=str(datetime.now())
        timestamp=timestamp[:-7]
        cur_date,cur_time=map(str,timestamp.split())
        print("Your Student ID = "+co_id,end='  ')
        print("Time = ",timestamp)
        if str(co_id) not in student_dict.keys():
            student_dict[str(co_id)]=[co_id,cur_date,cur_time]
        else:
            printing_value=[si_no]+student_dict[str(co_id)] +[cur_time]
            csvwriter.insertval(printing_value)
            # connection=sqlite3.connect("Database.csv")
            
            si_no+=1
            mail=(str(co_id)).lower()+"@sairamtap.edu.in"
            del student_dict[str(co_id)]
            mailsending.send_mail(mail)
        time.sleep(3)
    cv2.imshow('Testing',frame)
    cv2.waitKey(1)