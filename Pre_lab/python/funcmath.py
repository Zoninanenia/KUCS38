'''
ฟังก์ชันทางคณิตศาสตร์
จงเขียนโปรแกรมเพื่อรับค่า x ไปใช้ในการคำนวณฟังก์ชันทางคณิตศาสตร์

ให้คำนวณหาคำตอบของฟังก์ชันของ f(x) และ g(x) จากสมการด้านบน

ข้อมูลเข้า
หนึ่งบรรทัด คือค่า x ทึ่เป็นจำนวนจริง

ข้อมูลออก
หนึ่งบรรทัด ประกอบด้วย คำตอบของฟังก์ชันของ f(x) เมื่อรับ input ค่า x คั่นด้วยเว้นวรรค คำตอบของฟังก์ชันของ g(x) เมื่อรับ input ค่า x ที่เป็นจำนวนจริง

'''

#input
x = float(input())

#solve
fx = (3/4) * x + 5 * x ** 2 
gx = ((7 * x) - 9/2) ** 2

print(fx , gx)