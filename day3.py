def palindrome_checker(number):
    ### This function checks from 0 to  the input number and prints out all the palindromes between it. a palindrome is anything that reads the same both backward and forward e.g. Tenet, 101. Example: palindrome_checker(12) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11###

    counter = 0
    for num in range(number):
        if str(num)[::-1] == str(num):
            print(num)
            counter += 1

    return counter


print(palindrome_checker(500))
