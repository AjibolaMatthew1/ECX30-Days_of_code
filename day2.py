test_list = ['a', 'b', 'b', 'c']
test_list_two = ["a", "b", "a", "a", 3, 3, 2, "hello", "b"]


def mode_finder(item):
    ###This function takes in an input list and returns a list of the highest occuring number. Note if two numbers which occur most in the input list has the same frequency, they get both printed in the output list. E.g. mode_finder(['a', 'b', 'a']) -> ['a'] mode_finder(['1', '1', '1', 'a', 'a', 'a']) -> ['1', 'a']
    ###
    new_list = []
    word_counter_dict = {}
    list_of_highest = []
    for i in item:
        if i in word_counter_dict.keys():
            word_counter_dict[i] += 1
        else:
            word_counter_dict[i] = 1
    for i in word_counter_dict.keys():
        new_list.append(i)

    values = list(word_counter_dict.values())

    highest = max(values)
    for i, j in word_counter_dict.items():
        if j == highest:
            list_of_highest.append(i)

    print(list_of_highest)
    return (list_of_highest)


mode_finder(test_list)
mode_finder(test_list_two)
mode_finder(['1', '2', '1', '2', 'eg'])
mode_finder(["a", "b", "a", "a", 3, 3, 2, "hello", "b"])
