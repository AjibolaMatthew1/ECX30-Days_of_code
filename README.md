# Welcome to this repository! :)

## This is the repository that contains my solution to the 30 day challenge of
## code and design offered by ECX (Engineering Career Expo). 

The files have been numbered according to their days for easy navigation. I hope you find
it useful. If you are a beginner at python or even an intermediate, you'll  definitely
find something useful in it.

[Day 1 Solution](./day1.py)
Challenge Prompt
> List to Set - Create a function that takes in a list as input, and returns(and prints) a new list with all repetitions reduced to one appearance alone, as output.
I actually wasn't smart with this problem. 
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
