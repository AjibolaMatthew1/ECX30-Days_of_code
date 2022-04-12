# Welcome to this repository! :)

## This is the repository that contains my solution to the 30 day challenge of
## code and design offered by ECX (Engineering Career Expo). 

The files have been numbered according to their days for easy navigation. I hope you find
it useful. If you are a beginner at python or even an intermediate, you'll  definitely
find something useful in it.

[Day 1 Solution](./day1.py)
Challenge Prompt
> List to Set - Create a function that takes in a list as input, and returns(and prints) a new list with all repetitions reduced to one appearance alone, as output.

I don't think I was smart with this problem and the meme below describes my approach.
![Me rn!](https://i.kym-cdn.com/entries/icons/original/000/028/139/cover.jpg)

My solution didn't consider space complexity. I could have used a loop through the list and created a new list of unique items, but I didn't want to have a linear time complexity O(n). So I instead created a dictionary. One more possible solution is using set as it takes in only unique values, but I was concerned about the ordering.

E.G:
```
f(["a", "b", "a", "a", 3, 3, 2, "hello", "b"] ) => ["a", "b", 3, 2, "hello"]. #output
```

-----

[Day 2 Solution](./day2.py)
Challenge Prompt
> Find the mode in the list taken as an input in the day1 challenge above. 

For this problem, I used a dictionary to solve it. I created a word counter dictionary with the key as the specific item in the list and the value as the number of times it occured(frequency). Then, I found the maximum value of the values, using the max() function in python.

-----

[Day 3 Solution](./day3.py)
Challenge Prompt 
> Write a function that prints out all Palindromic numbers less than a given input, and returns the total number —of palindromes— found!

Well, using the python reverse string slicing, this wasn't difficult.

-----


[Day 4 Solution](./day4.py)
Challenge Prompt 
> Write a function that takes an integer as input, and prints out its conversion to Hexadecimal as output.

For this problem, I chose to create a dictionary to serve as a store for my hexadecimal numbers and characters. This allowed me to to use a while loop to continually divide input number by 16 and then acccess the approprimate hexadecimal number/character using the dictionary.

-----


[Day 5 Solution](./day5.py)
Challenge Prompt 
> Using recursion, write a function that prints out the first "n" members of the Fibonacci series.

Everyone knows the popular -> fib(n) = fib(n-1) + fib(n - 2), I created a function to implement just that.

-----

[Day 6 Solution](./day6.py)
Challenge Prompt 
> A man is stuck at the bottom of a well. Each day, he climbs up 8 metres, and then at night, he slips downwards by 3 metres. Using loops(any loop of your choice),  write a function to determine(and print!) how many days it takes for him to climb out of a well of any given depth, where the depth of the well is taken as input.

I used a loop to solve this. I ensured to add the 8 meters ascent and subtract the 3 meters descent too...

-----


[Day 7 Solution](./day7.py)
Challenge Prompt 
> Make a Wordle game.

Description: Wordle is a single player game, in which a user is required to guess a 5-letter hidden word in 6 Attempts.

*The user makes a first guess.( E.G: "Skate").

* Print out a progress guide, like this. "√××√+",

* "√" Indicates that the letter at that position was guessed correctly.

* "+" indicates that the letter at that position is in the hidden word, but in a different position.

*"×" indicates that the letter at that position is wrong, and isn't in the hidden word.

*This process is repeated until the user either guesses the hidden word correctly—in which case, he Wins!—, or exhausts his 6 Attempts, losing.


*The "hidden word" is generated randomly from a list of 5-letter words hard-coded by you.


Day 7 was DEFINITELY very fun! Thinking through the logic to make the game was nice. I had few bugs, which kept popping but it finally worked. I created different functions for each of the specifics i wanted to do. I wanted to follow the **FUNCTIONAL PROGRAMMING** path. I created also my main function that contained the most important logic.  I also utilised a text files containing lots of words so I would be able to get valid words. It wouldn't have been a fun game if *ghrt counted as a word, init? 

[Day 8 Solution](./day8.py)
Challenge Prompt 
> Write a function that takes in as parameters, a plaintext( string)to encode, and a _shift value _, and outputs the encoded value of the string.

*Write another similar function that takes in the encoded string, with a shift_value, and decodes it.


*Finally, write a third function that takes in a text, a shift value, and a third parameter to indicate whether to encode or decode the given text.(I.e f("string", 5, True/false) ) , And print out the encoded(or decoded) text accordingly.

I solved them using ascii characters.

