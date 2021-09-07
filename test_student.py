class Student:
    def __init__(self, id, birthday, name, adress, specialization, grade):
        self.id = id
        self.birthdate = birthday
        self.name = name
        self.adress = adress
        self.specialization = specialization
        self.grade = grade
    def show_student(self):
        print(f'{self.id} : {self.name}- {self.birthdate} - {self.adress} - {self.specialization} - {self.grade}')


class StudentList:
    def __init__(self,students):
        self.students = students


    def add_student(self):

        self.id = input("ID")
        self.birthdate = input ("Birthday")
        self.name = input("Name :")
        self.adress = input("Adress: ")
        self.specialization = input("Spec :")
        self.grade = input("Grade")

        add_s = Student(self.id, self.name, self.birthdate, self.adress, self.specialization, self.grade)
        students.append(add_s)

        return students


    def update(self):
        pass

    def find_student(self,id):
        match_student = next((student for student in self.students if student.id == id), None)
        if match_student is None:
            print('Not found')
        else:
            match_student.show_student()
        return match_student



    def show_student(self):
        for student in students:
            student.show_student()


    def remove_student(self,id):
        match_student = self.find_student(id)
        if match_student is None:
            print('Not found')
        else:
            self.students.remove(match_student)
            self.show_student()
    4




    def show_menu(self):
     print ('''        
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



s1 = Student('1', 'Nguyen Van A', '01-02-2001', 'Ha Noi', 'Toan Hoc', 'Lop AM1')
s2 = Student('2', 'Tran Thi B', '03-04-2002', 'Hue', 'Van Hoc', 'Lop AM2')
s3 = Student('3', 'Ly Dai C', '04-05-2003', 'Binh Dinh', 'Ly hoc', 'Lop AM3')
s4 = Student('4', 'Hoang Thi D', '06-07-2004', 'Ho Chi Minh', 'Ngoai Ngu Hoc', 'Lop AM4')
students = [s1, s2 ,s3 ,s4]
s = StudentList(students)

def get_choice():
    return input("Please enter your choice : ")


while True:

    s.show_menu()
    user_choice = get_choice()
    if user_choice == "1":
        s.show_student()
    elif user_choice == "2":
        s.add_student()
    elif user_choice == "5":
        id = input("Please enter ID to find : ")
        s.find_student(id)
    elif user_choice == "4":
        id = input("Please enter ID for remove : ")
        s.remove_student(id)



