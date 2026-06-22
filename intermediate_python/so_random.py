import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()

def fire_in_name(name):
    return "Fire" in name

def concatenate_name(name1, name2):
   return name1 + ", "+name2

def display_name_info(random_name, filtered, reduced):
    print("Fantasy Names:")
    for name in random_name:
        print(name)
    print(f"\nNames with Fire: {filtered}")
    print(f"Concatenated Names: {reduced}")

caps_suffix = list(map(capitalize_suffix, suffixes))
random_names = [create_fantasy_name(prefixes, caps_suffix) for x in range(10)]
filtered_fire = list(filter(fire_in_name, random_names))
concat_names = reduce(concatenate_name, filtered_fire)

display_name_info(random_names, filtered_fire, concat_names)

# # Define a generator function
# def square_generator(limit):
#   num = 1
#   while num <= limit:
#     yield num ** 2
#     num += 1

# # Use the generator to iterate over squares
# for square in square_generator(5):
#   print(square)