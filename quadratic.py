# class Intge:
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def print_sub(self):
#         return print("Tong 2 so nguyen : ", self.a , "+" ,self.b , " = " , self.a + self.b ,)
#
#
#
# s = Intge(4,3)
# s.print_sub()
#
# # a = int(input("Please enter numer : "))
# # print(a//8,a%8) if a >= 8 else print(a)
# while True:
#     a = float(input("Please enter number :"))
#     print(round(a, 3))

# class Output:
#
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def __str__(self):
#         return f'{self.name} + {self.old}'
#
#     def show(self):
#         return f'{self.name} + {self.old}'
import math
class Input:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_rect(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            print("a,b,c is squar of RECT")
        else:
            print("a,b,c is None")

    def quadratic(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    print("Quadratic VSN")
                else:
                    print("VN")
            else:
                print("1N")
        else:
            delta = self.b ** 2 -  4 * self.a * self.c
            if delta > 0:
                x1 = float((-self.b + math.sqrt(delta)) / 2 * self.a)
                x2 = float((-self.b - math.sqrt(delta)) / 2 * self.a)
                print("Phuong trinh cos 2 nghiem : nx1 = {} \n nx2 = {}",format(x1,x2))


            elif delta == 0:
                x = - self.b/2*self.a
                print("Phuong trinh co 1 nghiem duy nhat x = : {}".format(x))
            else:
                print("PHUONG TRINH VN")
class Print(Input):

    def __init__(self, a, b, c, number):
        super().__init__(a, b, c)
        self.number = number

    def print_str(self):
        print("10 of first_number : ", self.number.split("N",1))

# rect1 = Input(12,1,1)
# rect1.check_rect()
fx = Input(1, 2, 3)
fx2 = Input(1, 2, 1)
fx.quadratic()
fx2.quadratic()



for i in range(10):
    print(i,end="")










