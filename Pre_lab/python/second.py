'''
แตกหน่วยวินาที
จงเขียนโปรแกรมเพื่อรับจำนวนวินาทีที่ใช้ออกกำลังกาย 2 ครั้ง แล้วแสดงผลเวลารวมที่ใช้ในการออกกำลังกายในรูปของจำนวนชั่วโมง นาที และวินาที ตามลำดับ

ข้อมูลเข้า
บรรทัดแรก แสดงข้อความ "Enter your exercise time 1: " และรอรับจำนวนเต็ม s1 แทนจำนวนวินาทีที่ใช้ออกกำลังกาย ครั้งที่ 1
บรรทัดสอง แสดงข้อความ "Enter your exercise time 2: " และรอรับจำนวนเต็ม s2 แทนจำนวนวินาทีที่ใช้ออกกำลังกาย ครั้งที่ 2

ข้อมูลออก
แสดงจำนวนชั่วโมง นาที และวินาที ของเวลาออกกำลังกายรวมทั้งสองครั้ง ในรูปแบบตามตัวอย่าง

'''

#รับค่า
s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))

#คำนวณ
total_s = s1 + s2
hour = total_s // 3600
minute = (total_s % 3600) // 60
second = total_s % 60

#ผล
print(f"It is {hour} hours {minute} minutes and {second} seconds.")
