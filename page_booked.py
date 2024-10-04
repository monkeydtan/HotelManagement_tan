# ส่วนของพนักงานโรงแรม

import tkinter as tk
from tkinter import messagebox
from db import add_employee

window = tk.Tk()
window.title("จองโรงแรม")
window.geometry("400x400")
font1 = ['Arial',14,'normal']
font2 = ['Arial',12,'normal']

header = tk.Label(window,text="จองโรงแรม",font=font1)
header.pack(pady=10)

window.mainloop()