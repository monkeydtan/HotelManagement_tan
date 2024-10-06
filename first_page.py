import tkinter as tk
from tkinter import messagebox, Toplevel
import page_booked

window = tk.Tk()
window.title("หน้าหลัก")
window.geometry("400x400")
font1 = ['Arial',14,'normal']
font2 = ['Arial',12,'normal']
font3 = ['Arial',13,'normal']

# ปุ่มเช็คเอาท์
def checkout_button():
    print("ปุ่มเช็คเอาท์")

# ปุ่มจองห้องพัก
def booked_button():
    #print("ปุ่มจองห้องพัก")
    
    # สร้างหน้าต่างรายละเอียดการจอง
    booking_window = Toplevel(window)
    app = page_booked.HotelBooking(booking_window)

header = tk.Label(window,text="รายการ",font=font1)
header.pack(pady=10)

frame = tk.Frame(window)
frame.pack()

checkout_btn = tk.Button(frame,text="เช็คเอาท์",width=10,height=2,command=checkout_button)
checkout_btn.grid(sticky='nsew',row=0,column=0,padx=(0,10))

booked_btn = tk.Button(frame,text="จองห้องพัก",width=10,height=2,command=booked_button)
booked_btn.grid(sticky='nsew',row=0,column=1)

window.mainloop()