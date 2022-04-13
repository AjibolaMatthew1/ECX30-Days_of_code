def prime_number_checker(number):
    if number == 1:
        print("The number inputted is not a prime number")
    if number == 2:
        print("The number is a prime number")
        return True
    for i in range(2 , number):
        if number % i == 0:
            print("The number inputted is not a prime number")
            return False
        else:
            print("The number is a prime number")
            return True 

prime_number_checker(7)
prime_number_checker(3)
prime_number_checker(4)
prime_number_checker(17)
prime_number_checker(14)
prime_number_checker(1)
prime_number_checker(2)
prime_number_checker(43)
prime_number_checker(47)
prime_number_checker(97)
prime_number_checker(83)
prime_number_checker(24)
