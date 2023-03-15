'''
Minecraft
เราต้องการให้ Steve ขุดพื้นที่ให้เป็นสี่เหลี่ยมพื้นผ้าโดยที่ 1 block จะเท่ากับ 1 ตร.ม โดยเราจะรับค่าความยาว ความกว้าง และความสูงเป็นจำนวนจริงเพื่อให้ Steve ทำการขุด block ตามที่เราต้องการ จากนั้นจงหาว่า Steve จะใช้เวลากี่นาทีในการขุด block จนเสร็จ แสดงผลเป็นชั่วโมง (hours) นาที (minutes) วินาที (second) โดยคิดเวลาตอนขุด 1 block จะเท่ากับ 5 วินาที


ตัวอย่าง Input/Ouput
Enter width: 15
Enter length: 15
Enter depth: 15
Steve will take 4 hours 41 minutes 15 seconds.

'''
import math

#input
width = float(input("Enter width: "))
length = float(input("Enter length: "))
depth = float(input("Enter depth: "))

#process
block = width * length * depth
time = block * 5
hours = math.floor(time / 3600)
minutes = math.floor((time % 3600) / 60)
seconds = int(time % 60)


#output
print(f"Steve will take {hours} hours {minutes} minutes {seconds} seconds.")
