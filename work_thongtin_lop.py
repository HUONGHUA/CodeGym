# import calc_main as c
# print(c.sum(10,20))
# print(c.sub(10,20))
# print(c.divide(10,20))
# print(c.multi(10,20))
# from calc_main import *
# print(sum(10,20))
# print(sub(10,20))
# print(divide(10,20))
# print(multi(10,20))
# information :}

BANA = ["NGUYEN VAN A", "NAM", "HA NOI" , 82 , 91 ]
BANB = ["NGUYEN VAN B", "NU ", "DA NANG" , 99 , 84]
BANC = ["NGUYEN VAN C", "NAM" , "HO CHI MINH" , 88 , 100]
person = [BANA,BANB,BANC]
BAND = ["NGUYEN VAN D", "NAM", "HAI GIANG" ,  88 , 00]
person.append(BAND)
# Add infomation
def check_DTH():
    global DTH
    DTH = 0
    while True:
        try:
            DTH = int(input("Please enter point fo DTH (Điều kiện: 0<= dlt <= 100): "))
        except ValueError:
            print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")
            continue
        if 0 <= DTH <= 100:
            break
    return DTH
def check_DLT():
    global DLT
    while True:
        try:
            DLT = int(input("Please enter point for DLT (Điều kiện: 0<= dlt <= 100): "))
        except ValueError:
            print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")
            continue
        if 0 <= DLT <= 100:
            break
    return DLT
def info_person():
    global DTH
    global DLT
    name = input("Please enter name : ")
    gender = input("Please enter gender:")
    city = input("Please enter adress : ")
    check_DTH()
    check_DLT()
    f = [name, gender, city, DTH, DLT]
    print(f)
    return person.append(f)
## Khởi tạo thêm thành viên
while True:
    userinput = input("Ban có muốn thêm thành viên không (Y/N) ?")

    if userinput == "N":
        break
    elif userinput == "Y":
        info_person()
    else:
        print("Bạn nhập không chính xác Vui long nhap lai")
        continue
# In ra các thành viên
print("Danh Sách của các thành viên là :")
def print_person():
    for i in person:
        print(i)
## Xet đậu - trượt từng thành viên
print_person()
print("Danh sách điểm các thanh viên :")
for i in range(len(person)-1):
    DTB = (person[i][3] + person[i][4])//2
    if DTB >= 75:
        print(f'{person[i][0]} thi đỗ ',DTB)
    else:
        print(f'{person[i][0]} thi trược',DTB)
        person.pop(i)
## Thanh viên con lại trong lớp
print("Danh sách còn lại trong lớp")
print_person()
print(len(person))






