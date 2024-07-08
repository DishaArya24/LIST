# Write a program to find the largest number in a list
numbers =  [50,6,45,78,95,12,45,56]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
