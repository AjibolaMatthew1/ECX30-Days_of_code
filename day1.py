test_list = ['a', 'b', 'b', 'c']
new_list = []
word_counter_dict = {}

for i in test_list:
    if i in word_counter_dict.keys():
        word_counter_dict[i] += 1
    else:
        word_counter_dict[i] = 1
#print(word_counter_dict)

highest = []
values = list(word_counter_dict.values())

for i in range(len(values)):
    while i != (len(values) - 1):
        if values[i] > values[i + 1]:
            highest.append(values[i])
    if values[i] > values[i - 1]:
        highest.append(values[i])

print(highest)
print(values)

# for i, j in word_counter_dict.items():
#     highest = 0
#     if j > j + 1:
#         highest = j


# print(new_list)
        