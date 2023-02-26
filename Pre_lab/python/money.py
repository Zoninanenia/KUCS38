'''
ทอนเงิน 1
จงเขียนโปรแกรมแสดงธนบัตรที่ต้องใช้ในการทอนเงินลูกค้า โดยการรับจำนวนเงินของลูกค้า และรับจำนวนเงินเป็นราคาของสินค้าที่ต้องการซื้อ

กำหนดให้มีธนบัตรเป็นจำนวนเงิน 1, 10, 20, 50, 100, 500, และ 1000 บาท

กำหนดให้จำนวนเงินของลูกค้ามีค่ามากกว่าหรือเท่ากับจำนวนเงินเป็นราคาของสินค้าที่ต้องการซื้อ และเป็นจำนวนเต็มบวกเสมอ

ข้อมูลเข้า

บรรทัดแรก แสดงข้อความ "Total Money: " และรอรับจำนวนเต็ม แทนจำนวนเงินของลูกค้า
บรรทัดสอง แสดงข้อความ "Total Cost: " และรอรับจำนวนเต็มแทนจำนวนเงินเป็นราคาของสินค้าที่ต้องการซื้อ
ข้อมูลออก

แสดงจำนวนธนบัตรแต่ละใบ โดยเป็นจำนวนที่น้อยที่สุดที่เป็นไปได้

ห้ามใช้ if-else, for loop, while loop ในการเขียนโปรแกรม

'''

#input
total_money = int(input("Total Money: "))
total_cost = int(input("Total Cost: "))

#solve
change = total_money - total_cost

thousand = change // 1000
change = change % 1000

five_hundred = change // 500
change = change % 500

one_hundred = change // 100
change = change % 100

fifty = change // 50
change = change % 50

twenty = change // 20
change = change % 20

ten = change // 10
change = change % 10

one = change // 1

#output
print("1000 |", thousand)
print(" 500 |", five_hundred)
print(" 100 |", one_hundred)
print("  50 |", fifty)
print("  20 |", twenty)
print("  10 |", ten)
print("   1 |", one)