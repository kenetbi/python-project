from functools import reduce

playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(x):
    return x[1] > 5.00

def minutes_to_seconds(x):
    duration = x[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100
    return minutes * 60 + round(seconds)

def add_durations(x, y):
    return x + y

longer = filter(longer_than_five_minutes, playlist)
seconds = list(map(minutes_to_seconds, playlist))
duration = reduce(add_durations, seconds)

print(list(longer))
print(seconds)
print(duration)

# def raised_2(x):
#   return pow(x,2)
# numbers = [1,2,3,4,5,6,7,8,9,10]
# doubled = map(raised_2, numbers)
# print(list(doubled))

# def filter_even(x):
#     return x % 2 == 0
# even_numbers = filter(filter_even, numbers)
# print(list(even_numbers))

# def multiply(x,y):
#     return x*y
# product = reduce(multiply, numbers)
# print(product)