## Python: The `range()` Function

### Getting Started

- Create a new GitHub repo named **range-challenges-starter**
- Upload your code to your new repo once you've written and tested your scripts
- Teacher will review your work during Teacher Time


### Challenges

- Use a comment to label each challenge
- Example: `# Counting Up & Down, # Number Cubes`, etc.

### Counting Up & Down

- Start by prompting the user to enter an **integer**
    - HINT: The Python `int()` function will come in handy here!
- Then write a FOR loop that uses the `range()` function and TWO arguments (1 as the start value, and the *variable* containing your integer **+ 1 as your stop value**)
-  Finally, write a second FOR loop that prints 'We have lift off!' once the loop counts DOWN from 10 to 1 using the *variable* containing your integer **as your start value** and a step value of **-1**
- What will you use as your **stop** value in the `range()` function to get Python to count down to 1?



### Number Cubes
- Use a FOR loop and the `range()` function to generate and print the cubes of the numbers 1 - 10.
- Print a sentence that says: The cube of {whatever number} is {result}.

### Multiplication Table

- Assume you want to create a simple multiplication table for the number 7
- Start by assigning the value 7 to a variable `number`
- Use a FOR loop and the `range()` function with two arguments, a start value and a stop value
- Write a formula that tells Python how to do the math for your table
- Print a sentence that says: {number you chose} X {i} = {result}, where `i` is the variable name used to set up your FOR loop (use a different variable name if you wish)


### List Iteration

- **NOTE**: To *iterate* is a programming term that just means 'to loop' or 'to repeat over and over'
- Outside your FOR loop, define a Python variable named `total` and set its starting value to 0 (zero)
- Create a list of numbers that starts at 10 and goes up to 100 by tens, i.e., 10, 20, 30, etc.
- Next, create another variable `num_elements` and use the built-in `len()` function to store the length of the list in your  `num_elements` variable
- Then set up your FOR loop using a variable `i`, the `range()` function, and the `num_elements` variable inside the parentheses that follow `range`
- Inside your FOR loop, write a formula that lets Python calculate a running total of the numbers your list contains
    - Use an [augmented assignment operator](https://llego.dev/posts/comprehensive-guide-augmented-assignment-operators-python/) to do this
    - **DEFINITION**: **Augmented assignment operators** perform standard arithmetic operations like addition or multiplication and **assign the result of a calculation back to a variable**
    - You'll also need **the name of your list** immediately followed by []
    - The **[]** will contain the variable `i`, which stores the index for each list item
- Outside your FOR loop, use a `print` statement to say what the sum of the numbers in your list is
- Double check the sum by using a print statement and the `sum()` function with your list

