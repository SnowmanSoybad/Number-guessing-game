import random
number = (random.randint(1, 10))
x = 0

while True:
    i = int(input("ทายดูเลข 1-10: "))
    x += 1
    if i < number:
        print("คำตอบยังไม่ถูก มากกว่านี้")
    elif i > number:
        print("คำตอบยังไม่ถูก น้อยกว่านี้")
    else:
        print("คำตอบของคุณถูกแล้ว")
        break
print("คุณลองไปตอบไปทั้งหมด %d ครั้ง" % x)