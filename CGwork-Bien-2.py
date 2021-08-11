# coding utf-8
import math
a = float(input("Vui long nhap canh a"))
b = float(input("Vui long nhap canh b"))
c = float(input("Vui long nhap canh c"))
s = (a + b + c)/2
Dientich = math.sqrt(s* (s - a) * (s - b) * (s - c))
print("Dien tich cua tan giac la : " ,Dientich)
