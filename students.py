import json

class Student:
  def __init__(self, id, name, birthdate, address, specialization, grade):
    self.id = id
    self.name = name
    self.birthdate = birthdate
    self.address = address
    self.specialization = specialization
    self.grade = grade
  def __str__(self):
    return f'{self.id}: {self.name} - {self.birthdate} - {self.address} - {self.specialization} - {self.grade}'

class StudentList:
  def __init__(self, students):
    self.students = students

  def __str__(self):
    return '\n'.join(student.__str__() for student in self.students)

  def add(self, id, name, birthdate, address, specialization, grade):
    existed_student = self.find_by_id(id)
    if existed_student is not None:
      return None
    student = Student(id, name, birthdate, address, specialization, grade)
    self.students.append(student)
    return student

  def update(self, id, name, birthdate, address, specialization, grade):
    match_student = self.find_by_id(id)
    if match_student is None:
      return None

    match_student.name = name
    match_student.birthdate = birthdate
    match_student.address = address
    match_student.specialization = specialization
    match_student.grade = grade
    return match_student
  
  def find_by_id(self, id):
    return next((student for student in self.students if student.id == id), None)

  def remove(self, id):
    match_student = self.find_by_id(id)
    if match_student is not None:
      self.students.remove(match_student)
    return match_student

class App:
  def __init__(self, db):
    self.db = db
    self.studentList = StudentList([])
    # self.studentList = StudentList([
    #   Student('1', 'Nguyen Van A' ,'01-02-2001' ,'Ha Noi' ,'Toan Hoc' ,'Lop AM1'),
    #   Student('2', 'Tran Thi B' ,'03-04-2002' ,'Hue' ,'Van Hoc' ,'Lop AM2'),
    #   Student('3', 'Ly Dai C' ,'04-05-2003' ,'Binh Dinh' ,'Ly hoc' ,'Lop AM3'),
    #   Student('4', 'Hoang Thi D' ,'06-07-2004' ,'Ho Chi Minh' ,'Ngoai Ngu Hoc' ,'Lop AM4')
    # ])

  def load(self):
    f = open(self.db)
    data = json.load(f)
    students = [Student(x['id'], x['name'], x['birthdate'], x['address'], x['specialization'], x['grade']) for x in data]
    f.close()
    self.studentList = StudentList(students)

  def save(self):
    json_string = json.dumps([student.__dict__ for student in self.studentList.students], indent=2)
    f = open(self.db, "w")
    f.write(json_string)
    f.close()

  def show_menu(self):
    print(
    '''
Please choice menu :
1) Show list
2) Find
3) Add
4) Update
5) Remove
6) Load db
7) Save db
8) Exit program
    '''
    )

  def run(self):
    while True :
      self.show_menu()
      user_choice = input('Please choose: ')
      if user_choice == '1':
        print(self.studentList)
      elif user_choice == '2':
        id = input("Please input student id: ")
        match_student = self.studentList.find_by_id(id)
        print('Not found' if match_student is None else match_student)
      elif user_choice == '3':
        id = input("id: ")
        name = input("name: ")
        birthdate = input("birthdate: ")
        address = input("address: ")
        specialization = input("specialization: ")
        grade = input("grade: ")
        added_student = self.studentList.add(id, name, birthdate, address, specialization, grade)
        print('Student id existed' if added_student is None else added_student)
      elif user_choice == '4':
        id = input("id: ")
        name = input("name: ")
        birthdate = input("birthdate: ")
        address = input("address: ")
        specialization = input("specialization: ")
        grade = input("grade: ")
        updated_student = self.studentList.update(id, name, birthdate, address, specialization, grade)
        print('Not found' if updated_student is None else updated_student)
      elif user_choice == '5':
        id = input("Please input student id: ")
        removed_student = self.studentList.remove(id)
        print('Not found' if removed_student is None else removed_student)
      elif user_choice == '6':
        self.load()
      elif user_choice == '7':
        self.save()
      else:
        print('Exit....')
        break

App('data.json').run()
