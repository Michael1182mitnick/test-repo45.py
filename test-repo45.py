# Write a Python program to count the occurrences of a specific element in a list.

new_list = [10, 15, 20, 10, 30, 40, 70, 10, 90, 100]

x = 10
count = 0

for elem in new_list:
    if (elem == x):
        count += 1

print("{} has occured {} times".format(x, count))
