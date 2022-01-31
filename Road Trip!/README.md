# Road Trip!

### Problem statement
#### Find the shortest distance between 2 cities from the given datasets

#### Formulating the Problem Statement

- State Space : Space of all routes from `start-city` to `end-city`
  

- Initial State : `start-city` (post-pandemic trip begins here!!)
  

- Successor: Next possible states i.e. cities between start-city and end-city
  

- Cost Function:`segments , distance, time, safe`
  

- Goal State: `end-city` (post-pandemic trip ends here!!)

#### Tweaks made to the initial code
- For any state, the successor function finds the successor cities of the present city. The routes are assumed to be 
  bi-directional and hence the successor looks for cities at both first and second positions from the data file.


- `load_road_seg`, `load_city_gps` are used to load the 2 data files namely road-segments.txt and city-gps.txt, `loc_city` is another function used to check weather the input city is in the text file or not


- `haversine` is used to find the geodesic distance between x and y coordinates
  


-  `maxSpeed` for finding the maximum speed of all the routes and is later used in `successors`, `max_seg_l` for finding the max segment length, `distance` to find the distance using `haversine`


-  `cf` is to calculate the cost for each cost type, `heuristic` defines heuristic to be used for each cost type


- `successors` to generate successors for every state  ,`get_route` to find the shortest distance based on the cost function

### **_cost-function_**
    - segments: finding the optimal route which takes the minimum number of segments to reach the goal state

    - distance: finding the optimal route which shortens the total distance nedded to reach the goal state

    - time: finding optimal route which shortens the total time taken

    - safe: finidng optimal route which reduces the total expected accidents to reach goal state

_Submission is part of CSCI B551 - Elements of Artificial Intelligence assignments_

