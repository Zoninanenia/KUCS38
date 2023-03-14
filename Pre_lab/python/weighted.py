'''
คำนวนเกรด
พี่โปรเป็นนิสิตสาขาวิทยาการคอมพิวเตอร์ ชั้นปีที่ 2 ที่สามารถเขียนภาษา Python ได้อย่างชำนาญและเก่งรายวิชาสถิติเบื้องต้น 1 จึงได้ช่วยโชกุนคำนวนเกรดเฉลี่ยแต่ละปีการศึกษา หากโชกุนได้เกรดเฉลี่ย 4.00 โชกุนจึงจะได้รับทุนการศึกษาจากภาควิชาวิทยาการคอมพิวเตอร์ ประจำปีการศึกษา 2566

'''

#input
grade1 = float(input("Grade (1/66): "))
credit1 = int(input("Credit (1/66): "))
grade2 = float(input("Grade (2/66): "))
credit2 = int(input("Credit (2/66): "))

#process
Avg = (grade1 * credit1 + grade2 * credit2) / ( credit1 + credit2 )

#output
print(Avg)
if Average == 4:
    print("Chokul receives a scholarship.")
