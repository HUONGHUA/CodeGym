# coding utf-8
import math
a = float(input("Vui long nhap số tự nhiên: "))
if a%2 == 0:
    print("%.0f là số chẳn" %a)
elif a%2 == 1:
    print("%.3f là số lẻ :" %a)
else:
    print("%.3f khtng phải số nguyên"%a)