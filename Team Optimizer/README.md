# Team optimizer in Python

### Problem Statement
The  solver()  function.The function should return the final groups (each named according to the students in the group, separated by hyphens), and the total cost (number of complaints).The cost should be optimzed so as to give the best total cost and best possible teams according to the preferences givenen by the students.

## Abstract

- State Space: The state space for this problem includes all possible combinations of all group sizes ranging 0-3. The successor
function is any student that is switched with another student in a group according to the preferred list. Goal state is not defined. 
Heuristic function is also not taken into consideration.



- Successor:
It can be considered as the all the possible combinations which give out a cost lower than the original cost upon swapping the elements in the list.
  

- Goal State:
The goal state is achieved when there are no more people to assign to any more groups. This ensures that every
person belongs to a group. The goal state is achieved while ensuring that the previous states were all locally best
the solutions. This simply means that out of all possible groups, the one that has the lowest cost is locally the best.
  

- Cost function:
The cost function here is the objective cost of each state. This cost is used for selecting the lowest scoring candidate from the list.


The approach used in solving the problem is that , first we format the given file and convert the input file acordingly,
we basically use list of list to create a set of all the groups in a one big list.
then we start swapping the elements of the list among them and also check the cost, if the cost reduces for a certain state then we update that cost,
and then move ahead with next best combination. After we have done this with all the elemnets in a lista nd all the list keeping the prefered and not prefered constraints
The final output with the least cost is displayed.



### Challenges Faced
The main problem was as to how to approach the problem, as there was proper defined goal state (with respect to the arrangements of group members) only the numberical cost was reduced to the as minimum as possible keeping in mind the preferences of the people.
The primitive way to go about it is to use brute force method which involved searching for all possible cases of all solutions. Then we needed to evolve the then current solution to find a better solution.
we referred the below cited references on how to go about the problem based on that we moved ahead with the primitive approach.
This was alo the first time we had to use yield statement in python.
So it took me while  to figure out what it did and why is it used in our code.


### References for Part 3:

[1] https://www.reddit.com/r/algorithms/comments/46poqg/looking_for_an_algorithm_to_assign_things_to/

[2] https://scholars.unh.edu/cgi/viewcontent.cgi?article=2385&context=thesis

[3] https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
