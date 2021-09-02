# fruits = ["Angle","Cherry","Waos"]
# def add_fruit(fruits, fruit_to_add):
#     fruits.append(fruit_to_add)
#     print('fruis inside func',fruits)
# fruit_to_add = "Mango"
# add_fruit(fruits,fruit_to_add)
# print(fruits)
input_str = input("Please enter string :")

def count_chars(txt):
    result = 0
    for a in txt:
        result +=1
    return result
print('Length: ',count_chars(input_str))
print('Length: ',len(input_str))