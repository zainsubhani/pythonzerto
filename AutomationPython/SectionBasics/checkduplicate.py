some_list = ['a', 'd', 'e', 'v', 'a', 'a', 'g', 'd', 'z']
some_list.sort()
result = []

for i in range(len(some_list) - 1):  # prevent index out of range
    if some_list[i] == some_list[i + 1]:
        result.append(some_list[i])

print("Sorted list:", some_list)
print("Duplicate indices:", result)

     