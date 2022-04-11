def fibonnaci(n):
    ###This function prints the fibonacci series upto the nth term e.g. fibonnaci(5) -> 0, 1, 1, 2, 3.###
    if n <= 1:
        return (n)
    return (fibonnaci(n - 1) + fibonnaci(n - 2))

#number of terms n
n = int(input("How many terms of the fibonnaci series do you want to be displayed?\n"))
for i in range(n):
    print(f"Term {i + 1} in the series is: {fibonnaci(i)}")
