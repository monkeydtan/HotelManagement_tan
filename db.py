import sqlite3

# เชื่อมต่อกับฐานข้อมูล sqlite
# ระบุ path ที่สร้างใน DB Browser
def connect_db():
    connection = sqlite3.connect("data/data_booked.db")
    print("เชื่อมต่อฐานข้อมูลสำเร็จ !")
    return connection

def add_booked(fname,lname,contact,type_room,checkin_date,checkout_date,night,person):
    try:
        # สร้าง cursor สำหรับการสั่งงาน SQL
        connection = connect_db()
        cursor = connection.cursor()

        # เพิ่มข้อมูลลงในตาราง
        cursor.execute('''
        INSERT INTO Booked(fname,lname,contact,type_room,checkin_date,checkout_date,night,person)
        VALUES (?,?,?,?,?,?,?,?)              
        ''',(fname,lname,contact,type_room,checkin_date,checkout_date,night,person))

        # บันทึกการเปลี่ยนแปลง **คำสั่งนี้จำเป็นเฉพาะเมื่อทำการเปลี่ยนแปลงข้อมูลในฐานข้อมูล เช่น การ INSERT, UPDATE, หรือ DELETE**
        connection.commit()

        # เรียกใช้คำสั่ง SELECT เพื่อดึงข้อมูลจากตารางที่เราสร้างใน DB Browser
        cursor.execute("SELECT * FROM Booked")

        # ดึงผลลัพธ์ทั้งหมดจากการ query
        rows = cursor.fetchall()

        # แสดงผลข้อมูลที่ดึงมา
        for row in rows:
            print(row)
    
    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

    # ปิดการเชื่อมต่อเมื่อทำงานเสร็จ
    finally:
        if connection:
            connection.close()
            print("ปิดการเชื่อมต่อฐานข้อมูลแล้ว")

def delete(fname):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        # ลบข้อมูลในตาราง
        cursor.execute("DELETE FROM Booked WHERE fname=?",(fname,))
        print(f"ลบสำเร็จ")
        
        # บันทึกการเปลี่ยนแปลง
        connection.commit() # ยืนยันการลบ
                
    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        
    finally:
        if connection:
            connection.close()
            print("ปิดการเชื่อมต่อฐานข้อมูลแล้ว")

# ตรวจสอบ / ทดสอบการ select
def selected(fname):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        # ตรวจสอบข้อมูล
        cursor.execute("SELECT * FROM Booked WHERE fname=?",(fname,))

        # ดึงผลลัพธ์ทั้งหมดจากการ SELECT
        rows = cursor.fetchall() # ก็คือข้อมูลทุก column ของคนคนนั้น
        
        # ตรวจสอบว่ามีข้อมูลหรือไม่
        if rows:
            print("ข้อมูลที่พบ: ")
            for row in rows:
                print(row)
        else:
            print("ไม่พบข้อมูลที่มี fname =",fname)
    
    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        
    finally:
        if connection:
            connection.close()
            print("ปิดการเชื่อมต่อฐานข้อมูลแล้ว")
        
  
def update_data(night,fname):
    try:
        connnection = connect_db()
        cursor = connnection.cursor()
        
        # Update ข้อมูล **SET คือค่าที่ต้องการอัพเดท WHERE คือ ค่าที่ใช้ในการค้นหา
        cursor.execute("UPDATE Booked SET night=? WHERE fname=?",(night,fname))
        print(f"อัปเดตจำนวนคืนสำเร็จสำหรับคุณ {fname}")

        # บันทึกการเปลี่ยนแปลง
        connnection.commit()
            
    except sqlite3.Error as e:
        print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")

    # ปิดการเชื่อมต่อเมื่อทำงานเสร็จ
    finally:
        if connnection:
            connnection.close()
            print("ปิดการเชื่อมต่อฐานข้อมูลแล้ว")

     
# การเรียกใช้ฟังก์ชันต่างๆ
# add_booked() ==> รับค่าจากการกรอกฟอร์มแล้ว         
# selected("Tan") # ตรวจสอบข้อมูลของคนจากการค้นชื่อ fname
# delete("kkkk") # ลบข้อมูลของคนจากชื่อ    
#update_data(3,"Tan")    
