
class Manager_money:

    def __init__(self, time, object, money, type, note):
        self.time = time
        self.object = object
        self.money = money
        self.type = type
        self.note = note

    def __str__(self):
        return f'{self.time} | {self.object}  | {self.money} | {self.type} | {self.note} '

    def cal_type(self):
        pass
    def add_info(self):
        info_list = []
        info_list.append()

