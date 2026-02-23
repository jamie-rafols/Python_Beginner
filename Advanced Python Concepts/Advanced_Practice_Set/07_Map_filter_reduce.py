from functools import reduce

cube = [1,2,3,4,5]
even = [10,11,12,13,14]
red = [1,2,3,4]

print(list(map(lambda x: x**3, cube)))

print(list(filter(lambda x: x%2 == 0, even)))

print(reduce(lambda x,y: x+y, red))