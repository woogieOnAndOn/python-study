numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
days = ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
time_zone = ['morning', 'afternoon', 'evening', 'night']

# (1)
print(3 in numbers) # -> True

# (2)
print(10 not in numbers) # -> True

# (3)
print(numbers + days) 
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

# (4)
print(time_zone * 2)
# -> ['morning', 'afternoon', 'evening', 'night', 'morning', 'afternoon', 'evening', 'night']

# (5)
print(numbers[2:5]) 
# -> [2, 3, 4]

# (6)
'''
s[i:j:k] 
0 <= n < (j-i)/k
인덱스 x = i + n*k
i, i+k, i+2*k, i+3*k
'''
print(numbers[2:5:2]) 
# -> 인덱스 x = 2, 4, {6}...
# -> [2, 4]

# (7)
print(len(numbers)) # -> 10
print(min(numbers)) # -> 0
print(max(numbers)) # -> 9

# (8)
print(numbers.index(8, 5, 10)) # -> 8

# (9)
print(days.count('Mon')) # -> 2

# ---------

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
days = ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
time_zone = ['morning', 'afternoon', 'evening', 'night']

# (1)
numbers[1:3] = time_zone;
print(numbers)
# -> [0, 'morning', 'afternoon', 'evening', 'night', 3, 4, 5, 6, 7, 8, 9]

# (2)
del numbers[0:5] 
print(numbers) # -> [5, 6, 7, 8, 9]

# (3)
numbers.append(10)
print(numbers) # -> [5, 6, 7, 8, 9]

# (4)
time_zone.clear()
print(time_zone) # -> []

# (5)
days_copy = days.copy()
print(days_copy) # -> ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

# (6)
days.extend(time_zone);
print(days)
# -> ['Mon', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', 'morning', 'afternoon', 'evening', 'night']

# (7)
double_time = time_zone * 2
print(double_time)
# -> ['morning', 'afternoon', 'evening', 'night', 'morning', 'afternoon', 'evening', 'night']

# (8)
numbers.insert(3, 10)
print(numbers) # -> [0, 1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# (9)
time_zone.pop()
print(time_zone) # -> ['morning', 'afternoon', 'evening']

# (10)
days.remove('Mon')
print(days) # -> ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

# (11)
numbers.reverse()
print(numbers) # -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]