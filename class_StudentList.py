# # :newlist = [expression for item in iterable if condition == True]
# # # def myfunc(n):
# # #   return abs(n - 50)
# # # ## Săp xếp gần với 50!
# # # thislist = [100, 50, 65, 82, 23]
# # # thislist.sort(key = myfunc)
# # # print(thislist)
# # #
# # # ## Sắp xếp lower
# # # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # # thislist.sort(key = str.lower)
# # # print(thislist)
# # #
# # # #
# # # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# # #
# # # newlist = [x if x != "banana" else "orange" for x in fruits]
# # #
# # # print(newlist)
#
#
#
# # nameList = ["Nguyen" ,"Tra" , "Quốc", "Chung"]
# # print(a) if a in nameList:
#
# class Student():
#     def __init__(self, name, sex, adress, thoery, practic, id):
#         self.name = name
#         self.sex = sex
#         self.adress = adress
#         self.thoery = thoery
#         self.practic = practic
#         self.id = id
#
#     # def show(self):
#     #     # for x in students:
#     #     #     print('%s'%x)
#     #     print(f'{self.name} - {self.sex} - {self.adress} - {self.thoery} - {self.practic} - {self.id}')
#     #
#     #
#     # def remove(self,id_remove):
#     #     math_student = next((student for student in students if student[5] == id_remove), None)
#     #     if math_student is None:
#     #         print(" Not found")


s1 = ["Nguyen Van A", "Nam", "HN", 30, 50, 101]
s2 = ["Nguyen Van B", "Nam", "DN", 40, 50, 102]
s3 = ["Nguyen Thi C", "Nu", "DL", 90, 10, 103]

students = [s1, s2, s3]


class new_Student:

    def show(self):
        for x in students:
            print(x)

    def remove(self,id_remove):
        for x in students:
            if x[5] == id_remove:
                students.remove(x)
                print(x)
                break


    def add(self):
        add_name = input("Please enter add_name : ")
        add_sex = input("Please enter add_sex : ")
        add_adress = input(" Please enter add_adress : ")
        add_practic = self.input_add_practic()
        add_theory = self.input_add_thoery()
        add_id = self.check_id()
        add_student = [add_name, add_sex, add_adress, add_theory, add_practic, add_id]
        students.append(add_student)
        return students

    def check_id(self):
        while True:
            add_id = int(input("Plese enter add_id : "))
            list_id = [student[5] for student in students]
            if add_id in list_id:
                print("Sorry ! This ID is available")
                continue
            else:
                break
        return add_id
    def input_add_thoery(self):
        while True:
            add_thoery = 0
            try:
                add_thoery = int(input(" Please enter add_thoery : "))
            except ValueError:
                print("Giá trị nhập vào không phải là số. Vui lòng nhập lại!")
                continue
            if 0 <= add_thoery <= 100:
                break
            else:
                print("Sorry.Plese enter again ! ( 0<= Math <=100 )")
        return add_thoery
    def input_add_practic(self):
        while True:
            add_practic = 0
            try:
                add_practic = int(input(" Please enter add_pratic : "))
            except ValueError:
                print("Sorry Enter is not number. Please try again")
                continue
            if 0 <= add_practic <= 100:
                break
            else:
                print("Sorry.Plese enter again ! ( 0<= Math <=100 )")
        return add_practic
    
s = new_Student()

while True:
    user_choice = input('''
                            Menu :
                            Enter 1 to Show :
                            Enter 2 to Remove : 
                            Enter 3 to Add :
                            And Enter "Exit" to stop:                 
                            Please choice : ''')

    if user_choice == "1":
        s.show()
    elif user_choice == "2":
        id_remove = input("Please enter ID for remove : ")
        s.remove(id_remove)
    elif user_choice == "3":
        s.add()
    elif user_choice == "Exit":
        print("Exit program ! ")
        break

    else:
        print("Sorry ! Try agian !")




























