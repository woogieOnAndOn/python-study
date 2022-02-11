numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
days = ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
time_zone = ['morning', 'afternoon', 'evening', 'night']

print(3 in numbers) # -> True

print(10 not in numbers) # -> True

print(numbers + days) 
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

print(time_zone * 2)
# -> ['morning', 'afternoon', 'evening', 'night', 'morning', 'afternoon', 'evening', 'night']

print(numbers[2:5]) 
# -> [2, 3, 4]

'''
s[i:j:k] 
0 <= n < (j-i)/k
인덱스 x = i + n*k
i, i+k, i+2*k, i+3*k
'''
print(numbers[2:5:2]) 
# -> 인덱스 x = 2, 4, {6}...
# -> [2, 4]

print(len(numbers)) # -> 10
print(min(numbers)) # -> 0
print(max(numbers)) # -> 9
print(numbers.index(8, 5, 10)) # -> 8
print(numbers.index(3, 5, 10)) # -> Exception has occurred: ValueError 3 is not in list
print(days.count('Mon')) # -> 2