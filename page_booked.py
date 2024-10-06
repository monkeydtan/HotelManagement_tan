# ส่วนของพนักงานโรงแรม

import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter.ttk import Combobox
from tkinter import ttk
from tkcalendar import DateEntry
import db # import ไฟล์ฐานข้อมูลเข้ามา
from datetime import datetime # ใช้ library datetime ซึ่งเป็นไลบรารี่ที่ใช้สำหรับการจัดการและคำนวณเกี่ยวกับวันที่และเวลา

class HotelBooking:
    def __init__(self,root):
        self.window = root
        self.window.title("จองโรงแรม")
        self.window.geometry("400x400")
        # กำหนด font เป็นคุณสมบัติของคลาส
        self.font1 = ['Arial',14,'normal']
        self.font2 = ['Arial',12,'normal']
        self.font3 = ['Arial',13,'normal']

        header = tk.Label(self.window,text="จองโรงแรม",font=self.font1)
        header.pack(pady=10)

        self.frame_form = tk.Frame(self.window)
        self.frame_form.pack(pady=10,)

        label_name = tk.Label(self.frame_form,text="ชื่อ :")
        label_name.grid(sticky='nsew',row=0,column=0,padx=(0,10))

        self.entry_name = tk.Entry(self.frame_form)
        self.entry_name.grid(sticky='nsew',row=0,column=1,pady=(0,10))

        label_lname = tk.Label(self.frame_form,text="นามสกุล :")
        label_lname.grid(sticky='nsew',row=1,column=0,padx=(0,10))

        self.entry_lname = tk.Entry(self.frame_form)
        self.entry_lname.grid(sticky='nsew',row=1,column=1,pady=(0,10))

        label_contact = tk.Label(self.frame_form,text="เบอร์โทร :")
        label_contact.grid(sticky='nsew',row=2,column=0,padx=(0,10))

        self.entry_contact = tk.Entry(self.frame_form)
        self.entry_contact.grid(sticky='nsew',row=2,column=1,pady=(0,10))

        label_typeroom = tk.Label(self.frame_form,text="ประเภทห้อง :")
        label_typeroom.grid(row=3,column=0,padx=(0,10))

        self.items = tk.StringVar()
        typeroom = ['Standard','Delux','Suite']
        combobox_typeroom = Combobox(self.frame_form,values=typeroom,textvariable=self.items)
        combobox_typeroom.grid(row=3,column=1,pady=(0,10))

        # วันเข้าพัก
        label_checkin = tk.Label(self.frame_form,text="วันเข้าพัก :")
        label_checkin.grid(row=4,column=0,padx=(0,10))

        self.checkin_date = DateEntry(self.frame_form,width=12,background='darkblue',foreground='white',borderwidth=2,year=2024)
        self.checkin_date.grid(row=4,column=1,pady=(5,10))

        # วันเช็คเอาท์
        label_checkout = tk.Label(self.frame_form,text="วันออก :")
        label_checkout.grid(row=5,column=0,padx=(5,10))

        self.checkout_date = DateEntry(self.frame_form,width=12,background='darkblue',foreground='white',borderwidth=2,year=2024)
        self.checkout_date.grid(row=5,column=1,pady=(0,10))


        # จำนวนคนเข้าพัก
        label_person = tk.Label(self.frame_form,text="จำนวนผู้เข้าพัก :")
        label_person.grid(sticky='nsew',row=6,column=0,padx=(0,10))

        self.entry_person = tk.Entry(self.frame_form)
        self.entry_person.grid(sticky='nsew',row=6,column=1,pady=(5,10))

        booked_btn = tk.Button(self.frame_form,text="จอง",width=10,command=self.selected)
        booked_btn.grid(row=7,columnspan=2,pady=(5,10))
        

    # ปุ่มจอง พอกดจองแล้วจะแสดงหน้าต่างใหม่ที่มี รายละเอียดและปุ่มยืนยัน ปุ่มยกเลิก
    def selected(self):
        self.data_name = self.entry_name.get() #เก็บข้อความตั้งแต่อักขระแรกจนถึงอันสุดท้ายและเก็บไว้ที่ตัวแปร data_name
        self.data_lname = self.entry_lname.get()
        self.data_contact = self.entry_contact.get()
        self.data_typeroom = self.items.get()
        self.data_checkinDate = self.checkin_date.get_date() #เก็บข้อมูลว/ด/ป ที่เช็คอิน
        self.data_checkoutDate = self.checkout_date.get_date() #เก็บข้อมูลว/ด/ป ที่เช็คเอ้า
        self.data_person = self.entry_person.get()


        # สร้างหน้าต่างรายละเอียดการจอง
        detail_window = Toplevel(self.window)
        detail_window.title("รายละเอียดการจอง")
        detail_window.geometry("400x400")

        # หัวข้อ
        detail_booked = tk.Label(detail_window,text="ยืนยันการจอง",font=self.font1,anchor='center')
        detail_booked.pack(pady=10)

        # กรอบรายละเอียด
        frame_datails = tk.Frame(detail_window)
        frame_datails.pack(expand=True)

        label_datails = tk.Label(frame_datails,text=f'''
            ชื่อ-สกุล: {self.data_name} {self.data_lname}
            เบอร์ติดต่อ: {self.data_contact}
            ประเภทห้อง: {self.data_typeroom}
            วันที่เข้าพัก: {self.data_checkinDate}
            วันที่ออก: {self.data_checkoutDate}
            จำนวนผู้เข้าพัก: {self.data_person}   
            ''',justify='center',anchor='w',font=self.font3) #,justify='left', anchor='w'
        label_datails.grid(row=0, column=0, columnspan=2,pady=(0,10))

        ok_btn = tk.Button(frame_datails,text="ยืนยัน",width=10,command=self.booked)
        ok_btn.grid(row=1,column=0,padx=10,pady=10,sticky='ew')
        close_btn = tk.Button(frame_datails,text="ยกเลิก",width=10,command=detail_window.destroy)
        close_btn.grid(row=1,column=1,padx=10,pady=10,sticky='ew')

    # ยืนยันการจอง และบันทึกข้อมูลลงใน db    
    def booked(self):
        #print (f"ยืนยันการจองสำเร็จ !")
        data_name = self.entry_name.get()
        data_lname = self.entry_lname.get()
        data_contact = self.entry_contact.get()
        data_typeroom = self.items.get()
        data_checkinDate = self.checkin_date.get_date() #เก็บข้อมูลว/ด/ป ที่เช็คอิน
        data_checkoutDate = self.checkout_date.get_date() #เก็บข้อมูลว/ด/ป ที่เช็คเอ้า
        data_person = self.entry_person.get()

        # หาจำนวนคืนที่พัก
        # checkin = datetime.strptime(data_checkinDate,"%d/%m/%y")
        # checkout = datetime.strptime(data_checkoutDate,"%d/%m/%y")

        # คำนวณคืน
        num_nights = (self.data_checkoutDate-self.data_checkinDate).days

        # ตรวจสอบข้อมูลก่อนบันทึก
        if not self.data_name or not self.data_lname or not self.data_contact or not self.data_typeroom or not self.data_checkinDate or not self.data_checkoutDate:
            messagebox.showerror("Error","กรุณากรอกข้อมูลให้ครบถ้วน")
            # เรียกใช้ฟังก์ชันบันทึกข้อมูลจากไฟล์ db.py
            return # return จะทำให้ฟังก์ชัน booked() หยุดทำงานทันทีที่บรรทัดนี้ถูกเรียกใช้งาน หมายความว่าไม่มีการดำเนินการใด ๆ ถัดไปในฟังก์ชันนี้ (เช่น การบันทึกข้อมูลลงในฐานข้อมูลจะไม่เกิดขึ้น)

        db.add_booked(self.data_name,self.data_lname,self.data_contact,self.data_typeroom,self.data_checkinDate,self.data_checkoutDate,num_nights,self.data_person)
        messagebox.showinfo("การจองโรงแรม","จองห้องพักเรียบร้อยแล้ว")
        print(f"บันทึกข้อมูล: {self.data_name}, {self.data_lname}, {self.data_contact}, {self.data_typeroom} , {self.data_checkinDate} ,{self.data_checkoutDate} , {num_nights},{self.data_person}")


                    
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelBooking(root)
    root.mainloop()
    