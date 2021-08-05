# -*- coding: utf-8 -*-
row1 = '+{:-<15} |{:-^20}|{:-^20}| {:->15} +' . format('','','','','')
row2 = '|{:+<15} |{:^20} |{:^20}| {:>15} |' . format('Họ và tên', 'Ngày Sinh' ,'Lớp học' , ' Nơi ở')
row3 = '|{:+<15} |{:^20} |{:^20}| {:>15} |' . format('Hứa Thanh Hường', '18/02/1990' ,' PYF2109' , 'ĐÀ NẴNG')
row4 = '+{:-<15} |{:-^20}|{:-^20}| {:->15} +' . format('','','','','')
print(row1)
print(row2)
print(row3)
print(row4)
