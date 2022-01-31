## Expectimax: The Game of Sebastian

##### Referred sources have been cited

### Problem Statement:
- This game is full of luck and skill.

- The player has to roll 5 dice, inspects the dice and chooses any subset (including one or all) and rolls them.

- The player inspects the dice again again choose any subset and rolls them.

- The player must assign the outcome to exactly one category on their score card, depending on which five dice are showing after the third roll.

### Implementation:

- We made a function to initialize the first 6 states and the next 7 states.

- We created a dictionary that has the first 6 categories and it's values from 1 to 6. (This is in accordance with the categorical rules given to us in the problem statement)

- Next, we have the combo function, in which they take a list parameter and returns a list of the die combination. This idea has been taken from the discussion 8 walk through : A mini game of Chance. 
    Instead of nested loops, we use a helper function which is analogous to combos3 function from D8.


- We made a function called score_roll, which will assign the categories to each roll of 5 dies.
    Depending on the conditions, score will update and the function will return the score.

- Next, we have a function called final_score, we maximize our score by choosing the appropriate category.
    For example, if we have a particular roll, that satisfies more than one category, then it will select the one that outputs the maximum score.

- We then assign a category from 7th to 13th, and choose the one that maximizes it.

- We then have an expectation_of_roll function, it takes the sum of the outcome, and divides it by the length of the number of games

- The max strategy function, takes the roll, scorecard and bonus parameters to find out the strategy that maximizes the score.

- The first_roll function returns the maximum strategy after the first roll of the dies.

- The second_roll function returns the maximum strategy after the second roll of the dies.

- After, the third roll, a category is assigned based on the number that comes on the dies.
