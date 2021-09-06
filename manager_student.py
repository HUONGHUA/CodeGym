
person = {
    "001" : ['Nguyen Van A' ,'01-02-2001' ,'Ha Noi' ,'Toan Hoc' ,'Lop AM1' ],
    "002" : ['Tran Thi B' ,'03-04-2002' ,'Hue' ,'Van Hoc' ,'Lop AM2'],
    "003" : ['Ly Dai C' ,'04-05-2003' ,'Binh Dinh' ,'Ly hoc' ,'Lop AM3'],
    "004" : ['Hoang Thi D' ,'06-07-2004' ,'Ho Chi Minh' ,'Ngoai Ngu Hoc' ,'Lop AM4']

}
class Student:



    # id_student = list(person.keys())
    # values_person = list(person.values())
    #
    # name_student = []
    # for i in values_person:
    #     name_student.append(i[0])
    #
    # date_of_birth_student = []
    # for i in values_person:
    #     name_student.append(i[1])
    #
    # adress_student = []
    # for i in values_person:
    #     adress_student.append(i[2])
    #
    # specialization_student = []
    # for i in values_person:
    #     specialization_student.append(i[3])
    #
    # class_student = []
    # for i in values_person:
    #     class_student.append(i[4])






    # def __init__(self,id_student,name_student,date_of_birth_student,adress_student,specialization_student,class_student):
    #     self.id_student = id_student
    #     self.name_student = name_student
    #     self.date_of_birth_student = date_of_birth_student
    #     self.adress_student = adress_student
    #     self.specialization_student = specialization_student
    #     self.class_student = class_student

    def show_student(self):
        for key, value in person.items():
            print(key, ":", value)

    def add_student(self):


        self.id_student = input("Please enter ID of student ")
        self.name_student = input("Please enter Name of sutdent")
        self.date_of_birth_student = input("Please enter Date of birth student")
        self.adress_student = input("Please enter Adress of student :")
        self.specialization_student = input("Please enter Specialization of student")
        self.class_student = input("Please enter Class of Student")
        add_key = self.id_student
        add_value = [self.name_student, self.date_of_birth_student, self.adress_student, self.specialization_student,
                     self.class_student]

        person[add_key] = add_value
        print("Ban đã thêm vào ID này :")

        print(add_key,":" ,add_value)

        print(person.items())

        return person

    def update_student(self):
        id = input("Vui long nhap id cần cập nhập : ")
        for key, value in person.items():
            if id == key:
                value2 = input("Vui long nhap value cần thay đổi")
                while True:
                    x = int(input("Vui long nhập nhập chức năng cần thay đôi"
                              " 1 ) Họ và tên "
                              " 2 ) Ngày sinh "
                              " 3 ) Địa chỉ "
                              " 4 ) Ngành học "
                              " 5 ) Lớp học"
                              ))
                    for i in range(0,5):
                        if i == x:
                            value[x-1] = value2

                    if 0 < x < 6:
                        break

                print(value)
                break
            else:
                print("Id không tồn tại")
        return person
    def remove_student(self):
        id = input("Vui long nhap id cân xoá")
        for key, value in person.items():
            if id == key:
                person.pop(id)
        return person


    def find_student(self):
        id = input("Vui long nhap id cân tim")
        for key,value in person.items():
            if id == key:
                print(key ,":",value)
                break
            else:
                print("Not Available")




    def sort_student(self):
        dict_items = person.items()
        sorted_items = sorted(dict_items,reverse=True)
        for i in sorted_items:
            print(i)


    def show_menu(self):
        print(
        '''
        Please choice menu :
        1) Xem danh mục sinh viên
        2) Thêm sinh viên vào danh mục 
        3) Cập nhập thôn tin của sinh viên
        4) Xóa thông tin sinh viên khỏi danh mục
        5) Tìm kiếm thông tin sinh viên trong danh mục theo từ khóa 
        6) Sắp xếp thôn tin sinh viên trong danh mục
        7) " Exit program "
         
            '''
        )

s = Student()

def get_choice():
    return input("Please your choice :")

while True :
    s.show_menu()
    user_choice = get_choice()
    print("Ban da chon " + user_choice)
    if user_choice == "1":
        s.show_student()
    elif user_choice == "2":
        s.add_student()
    elif user_choice == "3":
        s.update_student()
    elif user_choice == "4":
        s.remove_student()
    elif user_choice == "5":
        s.find_student()
    elif user_choice == "6":
        s.sort_student()
    elif user_choice == "7":
        print("Exit program : Thank you !")
        break



