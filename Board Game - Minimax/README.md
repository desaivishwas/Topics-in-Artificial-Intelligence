#  Board Game Minimax - Pikachu

##### Referred sources have been cited 

### Problem Statement
    Pikachu, a popular childhood game in rural Midwest America has an N x N board (where n >= 7). Each stone is called a pichu and there balck and white pichus on the board. The pichus move arounf the board according tot he constarints laid out
        - Move a single Pichu of his or her color one square forward, left, or right, if that square is empty
        - Move a single Pichu of his or her color to \jump" over a single piece of the opposite color by moving two squares forward, left, or right, if that square is empty. The jumped piece is removed from the board as soon as it is jumped.
        - Move a single Pikachu of his or her color any number of squares forward, left, right, or backwards, to an empty square, as long as all squares in between are also empty.
        - Move a single Pikachu of his or her color to \jump" over a single piece of the opposite color and landing any number of squares forward, left, right, or backwards, as long as all of the squares between the Pikachu's start position and jumped piece are empty and all the squares between the jumped piece and the ending position are empty. The jumped piece is removed as soon as it is jumped.

### Description

- The input is given as a string which we are converting it to a 2D matrix to get the index of the pikachu and pichu in a easier way

- According to the constraints, the pichu moves one square forward, left or right if the square is empty and, so we are running 2 for loops for row and column

- A pikachu is formed when a pichu reaches the last row of the opponent's clan.

- After each execution of the program, a new configuration of the board is given as output
 
### Finding out the successors states for Pichu and Pikachu

- We wrote separate functions(4) for white pichu, black pichu, white pikachu, black pikachu. In these functions, we check for the best possible move for any given pichu / pikachu based on the board configuration and adhering to the constraints given.

- After getting the moves, we implement the minimax algorithm for our moves with alpha beta pruning

- Initially we expand the current configuration of the board where the max player plays, then based on the evaluation function we determine the next move of the player.

### From Pichu to Pikachu
- According to the rules of the game, the pichu becomes a pikachu when it reaches the opposite end of the board i.e. when white pichu goes to the Nth row it becomes a white pikachu and similarly when a black pichu goes to the 0th row it becomes a white pichu.

- Pikachu have additional capabilities when compared to pichus which is they can move any number os steps forward, backward, left or right as long as they are empty and can jump on its opposite color, but the jumping part is analogous to a normal pichu

### Minimax and Alpha Beta Pruning

- We explore our game tree to a certain depth, and then we back up our alpha and beta values 

- Given a state in a game, calculate the best move by searching forward all the way to the goal states

- Our `find_max, fin_min, alpha_beta` functions search the game to determine best action, use alpha-beta pruning which cuts off search and uses an evaluation function.

- We prune those branches which won't be of any use to us

### Goal State

- This function checks if we have reached the terminal state of their game and returns a boolean value

- `is_goal_state` function is being used by our `find_max` and `find_min` functions to check and return the best board having the right moves based on the input given

### Challenges faced 

- Figuring out the moves for pichu and pikachu was a bit of a struggle initially, we had to change our `valid_moves` function few time before we were able to get the right moves for the pichus and pikachus

- It was difficult for us to find the next best state when the input was in the form of a string and hence we changed into a 2D matrix for better understanding and ease of use

- Implementing the evaluation function was successful after considering many functions, but we finally settled upon calculating the difference in the number of white and black pichus and pikachus and the weighted cost

- We were getting errors when depth of the game tree was greater than 5 which we were able to resolve later

- We were getting list index out of range error for both black and white pichu which was resolved by adding row and column boundaries for the same
