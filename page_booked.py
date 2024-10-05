# ส่วนของพนักงานโรงแรม

import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter.ttk import Combobox
from tkinter import ttk
from tkcalendar import DateEntry
#from db import add_employee

window = tk.Tk()
window.title("จองโรงแรม")
window.geometry("400x400")
font1 = ['Arial',14,'normal']
font2 = ['Arial',12,'normal']
font3 = ['Arial',13,'normal']

header = tk.Label(window,text="จองโรงแรม",font=font1)
header.pack(pady=10)

frame_form = tk.Frame(window)
frame_form.pack(pady=10,)

label_name = tk.Label(frame_form,text="ชื่อ :")
label_name.grid(sticky='nsew',row=0,column=0,padx=(0,10))

entry_name = tk.Entry(frame_form)
entry_name.grid(sticky='nsew',row=0,column=1,pady=(0,10))

label_lname = tk.Label(frame_form,text="นามสกุล :")
label_lname.grid(sticky='nsew',row=1,column=0,padx=(0,10))

entry_lname = tk.Entry(frame_form)
entry_lname.grid(sticky='nsew',row=1,column=1,pady=(0,10))

label_contact = tk.Label(frame_form,text="เบอร์โทร :")
label_contact.grid(sticky='nsew',row=2,column=0,padx=(0,10))

entry_contact = tk.Entry(frame_form)
entry_contact.grid(sticky='nsew',row=2,column=1,pady=(0,10))

label_typeroom = tk.Label(frame_form,text="ประเภทห้อง :")
label_typeroom.grid(row=3,column=0,padx=(0,10))

items = tk.StringVar()
typeroom = ['Standard','Delux','Suite']
combobox_typeroom = Combobox(frame_form,values=typeroom,textvariable=items)
combobox_typeroom.grid(row=3,column=1,pady=(0,10))

# วันเข้าพัก
label_checkin = tk.Label(frame_form,text="วันเข้าพัก :")
label_checkin.grid(row=4,column=0,padx=(0,10))

checkin_date = DateEntry(frame_form,width=12,background='darkblue',foreground='white',borderwidth=2,year=2024)
checkin_date.grid(row=4,column=1,pady=(5,10))

# วันเช็คเอาท์
label_checkout = tk.Label(frame_form,text="วันออก :")
label_checkout.grid(row=5,column=0,padx=(5,10))

checkout_date = DateEntry(frame_form,width=12,background='darkblue',foreground='white',borderwidth=2,year=2024)
checkout_date.grid(row=5,column=1,pady=(0,10))

# จำนวนคนเข้าพัก
label_person = tk.Label(frame_form,text="จำนวนผู้เข้าพัก :")
label_person.grid(sticky='nsew',row=6,column=0,padx=(0,10))

entry_person = tk.Entry(frame_form)
entry_person.grid(sticky='nsew',row=6,column=1,pady=(5,10))

# ปุ่มจอง
def selected():
    data_name = entry_name.get() #เก็บข้อความตั้งแต่อักขระแรกจนถึงอันสุดท้ายและเก็บไว้ที่ตัวแปร data_name
    data_lname = entry_lname.get()
    data_contact = entry_contact.get()
    data_typeroom = items.get()
    
    # สร้างหน้าต่างรายละเอียดการจอง
    detail_window = Toplevel(window)
    detail_window.title("รายละเอียดการจอง")
    detail_window.geometry("300x200")
    
    # หัวข้อ
    detail_booked = tk.Label(detail_window,text="ยืนยันการจอง",font=font1,anchor='center')
    detail_booked.pack(pady=10)
    
    # กรอบรายละเอียด
    frame_datails = tk.Frame(detail_window)
    frame_datails.pack(expand=True)
    
    label_datails = tk.Label(frame_datails,text=f'''
    ชื่อ-สกุล: {data_name} {data_lname}
    เบอร์ติดต่อ: {data_contact}
    ประเภทห้อง: {data_typeroom}  
    ''',justify='center',anchor='w',font=font3) #,justify='left', anchor='w'
    label_datails.grid(row=0, column=0, columnspan=2,pady=(0,10))
    
    ok_btn = tk.Button(frame_datails,text="ยืนยัน",width=10,command=booked)
    ok_btn.grid(row=1,column=0,padx=10,pady=10,sticky='ew')
    close_btn = tk.Button(frame_datails,text="ยกเลิก",width=10,command=detail_window.destroy)
    close_btn.grid(row=1,column=1,padx=10,pady=10,sticky='ew')
    
def booked():
    print (f"ยืนยันการจองสำเร็จ !")

booked_btn = tk.Button(frame_form,text="จอง",width=10,command=selected)
booked_btn.grid(row=7,columnspan=2,pady=(5,10))





window.mainloop()