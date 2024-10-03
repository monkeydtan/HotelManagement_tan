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

    def __str__(self):
        #status_of_cus = "ยังไม่ได้ทำการจอง" if not self.booked_rooms else "จองแล้ว"
        return (f"ชื่อ: {self.name}\n"
                f"หมายเลขบัตรประชาชน: {self.id_card}\n"
                # f"รายการห้องที่จอง: {status_of_cus}\n"
        )

      
class Hotel:
    def __init__(self):
        self.rooms = [] # เอาไว้เก็บห้องทั้งหมดในโรงแรม
        self.customers = [] # เอาไว้เก็บรายชื่อลูกค้าของโรงแรม
        self.booked_rooms = [] # รายการการจองห้องพัก เก็บไว้เป็น List จะได้เก็บไว้หลายๆห้อง
    
#     # ฟังก์ชันการเพิ่มห้องพัก 
    def add_room(self,room):
        self.rooms.append(room)

    # ฟังก์ชันสำหรับการจองห้องพักของลูกค้า
    def book_room(self,customer,room):
        if not room.is_available: # ห้องยังว่างไหม คือ ว่าง=False ซึ่งมี not ทำให้กลายเป็น not False หรือ True หมายถึงห้องไม่ว่างหรือถูกจองไปแล้ว
            return f"ห้อง {room.room_number} ถูกจองไปแล้ว"
        else: # ถ้ายังว่าง
            room.booked_room() #เรียกใช้ method การจองห้องจากคลาส Room ซึ่งก็คือ booked_room
            self.booked_rooms.append(room) # เพิ่มห้องที่มีการจองแล้ว ไว้ใน List
            return f"{customer.name} ได้จองห้อง {room.room_number} เรียบร้อยแล้ว"

# ฟังก์ชันสำหรับแสดงห้องว่างทั้งหมด
    def show_available_rooms(self):
        available_rooms = [str(room) for room in self.rooms if not room.is_available]  # ตรวจสอบห้องว่าง
        if available_rooms:
            return f"รายละเอียดห้องว่าง: \n" + "\n".join(available_rooms)
        else:
            return "ไม่มีห้องว่าง"
  
        

# สร้าง object ห้อง กับ object ลูกค้า
room1 = Room(101,"Standard",590)
room2 = Room(201,"deluxe",790)

# สร้าง object ลูกค้า
customer1 = Customer("nisakorn",123456789)
customer2 = Customer("Tantan",2699562616)

# สร้าง object โรงแรม
hotel = Hotel()
#--------- เพิ่มห้องเข้าไปใน List -----------#
hotel.add_room(room1)
hotel.add_room(room2)

#--------- แสดงรายการห้องว่างก่อนการจอง ------------#
print(hotel.show_available_rooms())
 
#--------- ลูกค้าทำการจองห้อง ------------#
print(hotel.book_room(customer1,room1))

# สถานะลูกค้า
# print(customer1)
# print(customer2)

# สถานะห้อง
# print(room1)
# print(room2)