import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter.ttk import Combobox
from tkcalendar import DateEntry

def selected():
    # ดึงข้อมูลจากฟอร์ม
    data_name = entry_name.get()
    data_lname = entry_lname.get()
    data_contact = entry_contact.get()
    data_typeroom = items.get()

    # สร้างหน้าต่างใหม่ (Toplevel)
    top = Toplevel(window)
    top.title("รายละเอียดการจอง")
    top.geometry("300x200")

    # สร้าง Label และจัดตำแหน่งข้อความในหน้าต่างใหม่
    label_header = tk.Label(top, text="ยืนยันการจอง", font=("Arial", 14), anchor='center')
    label_header.pack(pady=10)

    label_details = tk.Label(top, text=f'''
    ชื่อ-สกุล:   {data_name} {data_lname}
    เบอร์ติดต่อ: {data_contact}
    ประเภทห้อง: {data_typeroom}
    ''', justify='left', anchor='w')
    label_details.pack(pady=10)

    # ปุ่มปิดหน้าต่าง
    close_btn = tk.Button(top, text="ปิด", command=top.destroy)
    close_btn.pack(pady=10)

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("จองโรงแรม")
window.geometry("400x400")

# ฟอร์มการกรอกข้อมูล
font1 = ['Arial',14,'normal']
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

# ปุ่มจอง
booked_btn = tk.Button(frame_form,text="จอง",width=10,command=selected)
booked_btn.grid(row=4,columnspan=2,pady=(5,10))

window.mainloop()
