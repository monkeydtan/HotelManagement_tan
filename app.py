from flask import Flask, render_template

app = Flask(__name__)

# route คือ เป็นการระบุ url เพื่อทำการเข้าถึงข้อมูล
@app.route("/") # ในวงเล็บคือชื่อ path ด้านใน ถ้ามีการระบุ url เป็น / จะให้ทำอะไร ดูจากบรรทัดถัดไป
def index(): # สร้างฟังก์ชัน
    # ให้ทำการแสดง... ตามโค้ดที่เขียนในฟังก์ชัน
    return render_template('index.html')

@app.route("/about")
def about():
    return "<h2>เกี่ยวกับฉัน</h2>"

@app.route("/admin")
def profile():
    return "<h2>แก้ไขโปรไฟล์</h2>"

@app.route("/user/<name>/<age>") #<name> เป็นพารามิเตอร์หรือตัวแปร name
def member(name,age):
    return "<h2>สวัสดีสมาชิก : {} , อายุ : {} </h2>".format(name,age)

if __name__ == "__main__":
    app.run()