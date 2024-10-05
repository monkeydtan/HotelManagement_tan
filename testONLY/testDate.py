import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def submit_date():
    selected_date = cal.get_date()
    print(f"Selected check-in date: {selected_date}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Hotel Booking - Check-in Date")
root.geometry("300x200")

# Label แสดงข้อความ
label = ttk.Label(root, text="Select Check-in Date:")
label.pack(pady=10)

# ปฏิทินเลือกวัน
cal = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2, year=2024)
cal.pack(pady=10)

# ปุ่ม Submit
submit_btn = ttk.Button(root, text="Submit", command=submit_date)
submit_btn.pack(pady=10)

root.mainloop()
