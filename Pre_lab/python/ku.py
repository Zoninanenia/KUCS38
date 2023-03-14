'''
มอสีเขียวน่าเรียน
น้องบีเป็น DEK66 ที่เข้ามาเรียนในสาขาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยสีเขียวแห่งหนึ่ง ซึ่งผ่านการคัดเลือกเข้าศึกษาต่อในระดับอุดมศึกษาในรอบที่ 1 (Portfolio) ซึ่งน้องบีจะต้องมาอยู่หอ แต่ยังไม่รู้ว่าควรจะใช้จ่ายเงินต่อเดือนเท่าไร จากที่น้องบีได้เคยเขียนโปรแกรม Python และเรียนทางด้านคอมพิวเตอร์มาบ้างจึงตัดสินใจสร้างโปรแกรมคำนวณค่าใช้จ่ายรายเดือน

โดยมีเงื่อนไขดังนี้

ค่าเทอมนิสิตชั้นปีที่ 1 จะได้ลด 10% ของค่าเทอมปกติ
ค่าหอจะได้รับ 35% ของค่าเทอม
ค่าครองชีพจะได้รับ 60% ของค่าหอ

'''

#input
year = int(input("Year: "))
education_fee = float(input("Education Fee: "))

# คำนวณค่าเทอม
term_fee = education_fee * (0.9 if year == 1 else 1)

# คำนวณค่าหอ
dormitory_fee = term_fee * 0.35

# คำนวณค่าครองชีพ
living_expenses = dormitory_fee * 0.6

print(int(term_fee))
print(int(dormitory_fee))
print(int(living_expenses))
