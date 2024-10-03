# ระบบจัดการโรงแรม

class Room:
    def __init__(self,room_number,room_type,price,is_available=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available # เอาไว้เช็คว่าห้องนั้นว่างไหม ค่าเริ่มต้นเป็น False คือ ยังไม่ถูกจอง หรือ ว่าง
    
    # ฟังก์ชันการจองห้องพัก **ฟังก์ชันนี้จะถูกเอาไปใช้ตอนที่ลูกค้าจะทำการจองห้องพัก**
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
    def __init__(self,name,id_card):
        self.name = name
        self.id_card = id_card # เลขบัตรปชช.
        self.booked_rooms = [] # รายการการจองห้องพัก เก็บไว้เป็น List จะได้เก็บไว้หลายๆห้อง
    
    # ฟังก์ชันสำหรับการจองห้องพักของลูกค้า
    def book_room(self,room):
        if not room.is_available: # ห้องยังว่างไหม คือ ว่าง=False ซึ่งถ้ายังว่างจะเข้า loop การจอง ทำให้ค่า is_available กลายเป็น True
            room.booked_room() #เรียกใช้ method การจองห้องจากคลาส Room ซึ่งก็คือ booked_room
            self.booked_rooms.append(room) # เพิ่มห้องที่มีการจองแล้ว ไว้ใน List
            return f"{self.name} ได้จองห้อง {room.room_number} เรียบร้อยแล้ว"
        else:
            return f"ห้อง {room.room_number} ถูกจองไปแล้ว"

    def __str__(self):
        status_of_cus = "ยังไม่ได้ทำการจอง" if not self.booked_rooms else "จองแล้ว"
        return (f"รายละเอียดผู้เข้าพัก\n"
                f"ชื่อ: {self.name}\n"
                f"หมายเลขบัตรประชาชน: {self.id_card}\n"
                f"รายการห้องที่จอง: {status_of_cus}\n"
        )

      
class Hotel:
    def __init__(self):
        self.rooms = [] # เอาไว้เก็บห้องทั้งหมดในโรงแรม
        self.customers = [] # เอาไว้เก็บรายชื่อลูกค้าของโรงแรม
    
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

# สร้าง object ห้อง กับ object ลูกค้า
room1 = Room(101,"Standard",590)
room2 = Room(201,"deluxe",790)

# ลูกค้าทำการจองห้อง
customer1 = Customer("nisakorn",123456789)
customer1.book_room(room1) # จองห้องพัก
customer2 = Customer("Tantan",2699562616)

# สถานะลูกค้า
print(customer1)
print(customer2)
# สถานะห้อง
print(room1)
print(room2)