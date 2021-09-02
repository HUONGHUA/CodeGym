number = [2,4,5,6,1,3,4,5,6,7,8,11]
number.sort(reverse=True)
print(number)
print('Maximum of number is: ',number[0])
number.sort()
print('Miximum of number is: ',number[0])
print('Avg of number is',(number[0]+number[len(number)-1])//2)