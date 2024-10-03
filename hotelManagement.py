# ระบบจัดการโรงแรม

class Room:
    def __init__(self,room_number,room_type,price,is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available # เอาไว้เช็คว่าห้องนั้นว่างไหม ค่าเริ่มต้นเป็น False คือ ยังไม่ถูกจอง หรือ ว่าง
    
    # ฟังก์ชันการจองห้องพัก **ฟังก์ชันนี้จะถูกเอาไปใช้ตอนที่ลูกค้าจะทำการจองห้องพัก**
    def booked_room(self):
        if self.is_available: # ถ้า not True = False คือ ถูกจองแล้ว
            self.is_available = False # ถูกจองแล้ว หรือ ไม่ว่าง
            return f"ห้อง {self.room_number} ประเภท {self.room_type} ถูกจองแล้ว"
        else:
            return f"ห้อง {self.room_number} ถูกจองไปแล้ว"
    
    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
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
        )

      
class Hotel:
    def __init__(self):
        self.rooms = [] # เอาไว้เก็บห้องทั้งหมดในโรงแรม
        self.booked_rooms = [] # รายการการจองห้องพัก เก็บไว้เป็น List จะได้เก็บไว้หลายๆห้อง
    
    # ฟังก์ชันการเพิ่มห้องพัก 
    def add_room(self,room):
        self.rooms.append(room)

    # ฟังก์ชันสำหรับการจองห้องพักของลูกค้า
    def book_room(self,customer,room):
        if room.is_available: # ห้องยังว่างไหม คือ ว่าง=True
            room.booked_room() #เรียกใช้ method การจองห้องจากคลาส Room ซึ่งก็คือ booked_room
            self.booked_rooms.append(room) # เพิ่มห้องที่มีการจองแล้ว ไว้ใน List
            return (f"------------------------------------\n"
                f"{customer.name} ได้จองห้อง {room.room_number} เรียบร้อยแล้ว\n"
                f"------------------------------------"
            )
        else: # ถ้าห้องไม่ว่าง
            return f"ห้อง {room.room_number} ถูกจองไปแล้ว"

    # ฟังก์ชันสำหรับแสดงห้องว่างทั้งหมด
    def show_available_rooms(self):
        available_rooms = [str(room) for room in self.rooms if room.is_available]  # ตรวจสอบห้องว่าง
        if available_rooms:
            return f"รายละเอียดห้องว่าง \n" + "\n".join(available_rooms)
        else:
            return "ไม่มีห้องว่าง"
        
    # ฟังก์ชันการเช็คเอ้าท์ห้องพัก
    def checkout_room(self,room): #รับ parameter ชื่อ room ซึ่งคือห้องที่ลูกค้าต้องการเช็คเอาท์
        if room in self.booked_rooms: # ตรวจสอบว่าห้องที่จะเช็คเอาท์นั้น อยู่ในรายการ self.booked.rooms ไหม หมายถึงเช็คว่าห้องนี้ถูกจองอยู่หรือไม่
            room.is_available = True # อัพเดทสถานะห้องที่ว่าง ซึ่งถ้า101ถูกจองอยู่ จะมีการอัพเดทสถานะให้กลับมาเป็นว่าง เพื่อให้ห้องนี้สามารถถูกจองได้อีก
            self.booked_rooms.remove(room) # ลบ101ออกจาก self.booked_rooms หรือลบห้องที่เช็คเอาท์ออกจากการจอง
            result = (f"------------------------------------\n"
                      f"ลูกค้าเช็คเอาท์ห้อง {room.room_number} เรียบร้อยแล้ว\n"
                      f"------------------------------------\n"
                      )
            result += self.show_available_rooms()
            return result
        else:
            return f"ห้อง {room.room_number} ยังไม่ได้ถูกจอง" 
        
  
        
# สร้าง object ห้อง กับ object ลูกค้า
room1 = Room(101,"Standard",590)
room2 = Room(201,"deluxe",790)
room3 = Room(301,"Suite",1290)

# สร้าง object ลูกค้า
customer1 = Customer("nisakorn",123456789)
customer2 = Customer("Tantan",2699562616)

# สร้าง object โรงแรม
hotel = Hotel()
#--------- เพิ่มห้องเข้าไปใน List -----------#
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

#--------- แสดงรายการห้องว่างก่อนการจอง ------------#
print(hotel.show_available_rooms())
 
#--------- ลูกค้าทำการจองห้อง ------------#
print(hotel.book_room(customer1,room1))
print(hotel.book_room(customer2,room3))

#--------- แสดงรายการห้องว่างหลังการจอง ------------#
print(hotel.show_available_rooms())

#--------- ลูกค้าเช็คเอ้าท์ ------------#
print(hotel.checkout_room(room1))

#--------- แสดงรายการห้องว่างหลัง check out ------------#
# print(hotel.show_available_rooms())
