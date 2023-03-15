'''
ระยะห่างระหว่างจุด
จงเขียนโปรแกรมคำนวนระยะห่างระหว่างจุด A (x1, y1) กับ B (x2, y2) โดยที่ข้อมูลเข้าเป็นจำนวนจริง โดยแสดงผลเป็นจำนวนจริง 2 หลัก

ตัวอย่าง Input/Ouput

--Distance Calculator--
Point X1: 2.4
Point Y1: 7.2
Point X2: 4.2
Point Y2: 4.2
Distance: 3.50

'''

#head
import math
print("--Distance Calculator--")

#input
x1 = float(input("Point X1: "))
y1 = float(input("Point Y1: "))
x2 = float(input("Point X2: "))
y2 = float(input("Point Y2: "))

#process
dis = math.sqrt( (x2-x1) ** 2 + (y2 - y1) ** 2 )

#output
print(f"Distance: {dis:.2f}")
