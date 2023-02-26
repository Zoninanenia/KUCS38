'''
คะแนนสอบย่อย
จงเขียนโปรแกรมรับค่ามา 5 ค่า โดยแต่ละค่าเป็นคะแนนเก็บของการสอบย่อยในแต่ละครั้ง

ข้อมูลเข้า
บรรทัดแรก ถึงบรรทัดที่ห้า รับจำนวนจริงเก็บค่าคะแนนสอบย่อยในแต่ละครั้ง โดยคะแนนสอบย่อยในแต่ละครั้งสามารถเป็นค่าลบได้ และเป็นจำนวนจริง

ข้อมูลออก
บรรทัดแรก แสดงข้อความ "Total Score: " ตามด้วยผลรวมของคะแนนสอบย่อยทั้งสองครั้ง
บรรทัดที่สอง แสดงข้อความ "Average: " ตามด้วยค่าเฉลี่ยของคะแนนสอบย่อยทั้งสองครั้ง

'''

#input
score1 = float(input())
score2 = float(input())
score3 = float(input())
score4 = float(input())
score5 = float(input())

#solve
total_score = score1 + score2 + score3 + score4 + score5
average_score = total_score / 5

#output
print(f"Total Score: {total_score}")
print(f"Average: {average_score}")