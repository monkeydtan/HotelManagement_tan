# ระบบจัดการโรงแรม

class Room:
    def __init__(self,room_number,room_type,price,is_available=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available # เอาไว้เช็คว่าห้องนั้นว่างไหม ค่าเริ่มต้นเป็น False คือ ยังไม่ถูกจอง หรือ ว่าง
    
    def booked_room(self):
        if not self.is_available: # ถ้า not false = true คือ ถูกจองแล้ว
            self.is_available = True # ถูกจองแล้ว
            return f"ห้อง {self.room_number} ประเภท {self.room_type} ถูกจองแล้ว"
        else:
            return f"ห้อง {self.room_number} ถูกจองไปแล้ว"
    
    def __str__(self):
        status = "Available" if not self.is_available else "Not Available"
        return (f"เลขห้อง : {self.room_number}\n"
                f"ประเภทห้อง : {self.room_type}\n"
                f"ราคาห้อง : {self.price}\n"
                f"สถานะ : {status}\n"           
        )
        
class Customer:
    def __init__(self,name,id_card,booked_rooms):
        self.name = name
        self.id_card = id_card # เลขบัตรปชช.
        self.booked_rooms = booked_rooms # รายการการจองห้องพัก

room1 = Room(101,"Standard",590)
room1.is_available
room1.booked_room()
print(room1)
      
# class Hotel:
#     def __init__(self):
#         self.rooms = [] # เอาไว้เก็บห้องทั้งหมดในโรงแรม
#         self.customers = [] # เอาไว้เก็บรายชื่อลูกค้าของโรงแรม
    
#     # ฟังก์ชันการเพิ่มห้องพัก 
#     def add_room(self,amount_room):
#         self.rooms.append(amount_room)

#     # ฟังก์ชันสำหรับแสดงห้องว่างทั้งหมด
#     def show_available_rooms(self):
#         rooms_details = "\n".join(str(room_number) for room_number in self.self.rooms)
#         customer_details = "\n".join(str(name) for name in self.customers)
#         return f"ห้องว่างทั้งหมด : \n{rooms_details}"
        
        
#     # ฟังก์ชันสำหรับให้ลูกค้าจองห้องพัก
#     def book_room(self,customer,number,type):
        
        
#     # ฟังก์ชันสำหรับการเช็คเอาท์ห้องพัก
#     # def checkout_room(self):