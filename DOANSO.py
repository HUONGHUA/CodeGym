# import random
# while True:
#     input("Nhan Enter de tung xuc xac")
#     num = random.randint(1,6)
#     print("Ban da tung duoc so",num)
#     option = input("Ban muon co tung tiep khong ? (y/n)")
#     if option == 'n':
#         break
# print("Done")
# import random
# print("Hello world")
#
# var = random.randint(1,10) # Khai báo random
# count= 0  # Khai báo đếm
# while count <3:
#     number = int(input("Vui long nhap vao tu 1- 10 :"))
#     if number == var:
#         print("Correct")
#         break
#     else:
#         print("Ban da doan sai")
#     count += 1
# else:
#     print("false ! Bạn đã hết lượt . Số đó là :",var)
# import turtle
# import math
# for i in range(1,6):
#     s = '*'* i
#     print(s)
# for i in range(5, 0, -1):
#     k = '*' * i
#     print(k)
# for i in range(5, 0, -1):
#     k = '*' * i
#     print((5-i)*" "+k)

import math
slnt = int(input("Nhap vao giới hạn số nguyên tốt"))
count = 0

# for i in range(2,n//2+1):
#     if i in (2,3,5,7,11):
#         print(i,end='\t')
#     elif i%3==0 or i%5 == 0 or i%2 == 0:
#         continue
#     else:
#         print(i,end="\t")
n = 1
while count < slnt:
    n += 1
    for i in range(2,n//2+1):
        if n%i == 0:
            # print(f'{n} số nguyên tốt')
            break
    else:
        print(n,end="\t")
        count +=1
