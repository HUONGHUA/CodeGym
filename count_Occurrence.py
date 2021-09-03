dict = "Here are simple rules to define a function in Python. Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ). Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses."
dict2 = " Any input any parameters or any arguments should be placed within any these parentheses. You can also define parameters inside these parentheses."

word = "any"

def count_Occurrennces(dict2,word):
    a = dict2.split(" ")
    count = 0
    print(a)
    for i in range(0,len(a)):
        if word == a[i] :
            count += 1
    return count
print(count_Occurrennces(dict2,word))
