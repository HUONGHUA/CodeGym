firstnumber = int(input("Nhap vao so dau tien :"))
secondnumber = int(input("Nhap vao so thứ 2 :"))

if secondnumber < firstnumber:
    print("Vui long nhap so sau lon hon so truoc")
else:
    for i in range(firstnumber,secondnumber+1):
        if i%15 == 0:
            print("FizzBuss")
            continue
        elif i%5 == 0:
            print("Buss")
            continue
        elif i%3 == 0:
            print("Fizz")
            continue
        else:
            print(i)
        