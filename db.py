import sqlite3

# เชื่อมต่อกับฐานข้อมูล sqlite
# ระบุ path ที่สร้างใน DB Browser
def connect_db():
    connection = sqlite3.connect("data/mydata.db")
    print("เชื่อมต่อฐานข้อมูลสำเร็จ !")
    return connection

def add_employee(fname,lname,address,contact,salary):
    try:
        # สร้าง cursor สำหรับการสั่งงาน SQL
        connection = connect_db()
        cursor = connection.cursor()

        # เพิ่มข้อมูลลงในตาราง
        # cursor.execute('''
        # INSERT INTO Employee(fname,lname,address,contact,salary)
        # VALUES (?,?,?,?,?)              
        # ''',(fname, lname, address, contact, salary))
    
        # ลบข้อมูลในตาราง
        #cursor.execute("DELETE FROM Employee WHERE id='14'")

        # บันทึกการเปลี่ยนแปลง **คำสั่งนี้จำเป็นเฉพาะเมื่อทำการเปลี่ยนแปลงข้อมูลในฐานข้อมูล เช่น การ INSERT, UPDATE, หรือ DELETE**
        connection.commit()

        # เรียกใช้คำสั่ง SELECT เพื่อดึงข้อมูลจากตารางที่เราสร้างใน DB Browser
        cursor.execute("SELECT * FROM Employee")

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
            
add_employee("ชินจัง", "จอมแก่น", "ญี่ปุ่น", "1212121212", 500)