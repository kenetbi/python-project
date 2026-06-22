numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]

print(f"Original Numbers: {numbers}")
print(f"Even Numbers: {even_num}")
print(f"Odd Numbers: {odd_num}")