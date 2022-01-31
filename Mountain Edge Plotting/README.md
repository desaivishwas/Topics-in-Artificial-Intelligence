# Mountain Edge Plotting
_Using Simple Bayes' Net, Viterbi and Human feedback_


## Problem Statement : 
- Identifying the shapes of the mountain

- We are trying to find the ridge line between the mountain and the sky using Simple Bayes' Net, Viterbi and Human feedback

- Estimating the corresponding column for each ridge line

- We pass the following System arguments;
  1) The sample image
  2) Row co-ordinate and Column co-ordinate
  
## Motivation :

- This technique is useful for army, flight travelling, and other useful and safety applications.
- This kind of image processing helps us automate a lot of things.
- We compare simple bayes' net, viterbi algorithm and human feedback outputs here.

## Implementation : 

### edge_strength
-We have been given a function namely edge_strength that measures how strong the image gradient is at each point.

### draw_edge
- This function helps us draw the edge on the image with the correct amount of thickness and color.

------------

- For detecting the ridge using Simple Bayes' net we find the maximum edge strength per column and return an array.  The denominator can be ignored for all the terms.
- For detecting the ridge using Viterbi algorithm, we use defined transition probabilities, sum the edge strength and define two arrays
- One is the final array and the other one is to store the previous state for back tracking.
- We then calculate the initial state probabilities.
- We then calculate the state probabilities of each node.
- We go back to the previous solution that was memoized and then output the image.
- For human feedback, we take the human input values as our state probabilities.
- We propagate through the change, and maximize to find the solution.

---------
- For ridge detection using Simple Bayes' nets, we use the color : Red
- For ridge detection using Viterbi, we use the color : Blue
- For ridge detection using human feedback, we use the color : Green
----------
Sample Test Image example: 

- Output

![mountain](https://github.com/desaivishwas/Topics-in-Artificial-Intelligence/blob/58183424c656d3c531a21df8e39d67b8e3cfc1be/Mountain%20Edge%20Plotting/mountain_output.jpg)


## References: 

- https://www.cse.unr.edu/~bebis/ISVC13_Horizon.pdf
- https://link.springer.com/article/10.1007/s00773-017-0464-8

