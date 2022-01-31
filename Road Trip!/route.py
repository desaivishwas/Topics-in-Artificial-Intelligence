#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: [Vishwas Desai and visdesai], [Sharanbasav Sumbad and ssumbad], [Shilpa Kumari and shkumari]
#
# Based on skeleton code by V. Mathur and D. Crandall, January 2021
#

# Late submission for Part 2


# !/usr/bin/env python3
# importing necessary packages

import heapq
import sys
import math


# # from queue import PriorityQueue


# loading the data from road-segments.txt and city-gps.txt

def load_road_seg():
    with open("road-segments.txt", 'r') as f:
        routes = f.readlines()
    return routes


gps_coords = []


def load_city_gps():
    with open("city-gps.txt", 'r') as f:
        line = f.readlines()
        # split  latitudes and longitudes
        for l in line:
            l = l.strip().split(" ")
            gps_coords = float(l[1]), float(l[2])
    return gps_coords


routes = load_road_seg()
gps_coords = load_city_gps()


# --------------------------------------------------------------------------------------------------------

# checks whether the given input for city exist in the list of cities or not
def loc_city(cname, gps_coords):
    if cname in gps_coords:
        return gps_coords[cname]
    return False


# Helper functions to calculate heuristics

# Src: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
#
# Euclidean distance is a naive method of finding the distance between 2 coordinates. A better approach would be to us haversine
# formula to find the angular/geodesic distance of a sphere.
#
# code snippet from https://gist.github.com/rochacbruno/2883505

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # radius of earth
    radius = 6378  # in meters
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    d = radius * c
    # converting Km to miles
    d = d / 1.609
    return d


# helper function to find the max speed in the given data for all the routes

def maxSpeed(routes):
    # max = -900000
    for r in routes:
        speed = [(r[3])]
        speed.sort()
        max_speed = max(speed)  # 65
    return max_speed


# helper function to find the mas segment length for a certain distance
def max_seg_l(routes):
    for r in routes:
        segment_l = [(r[2])]
        segment_l.sort()
        max_segment_l = max(segment_l)  # 923
    return max_segment_l


def distance(start, end):
    lo1, lat1 = start
    lo2, lat2 = end
    dist = haversine(lo1, lat1, lo2, lat2)
    return dist


road = [h[4] for h in routes]


def safe(route):
    if road[:2] == "I-":
        accidents = distance(route) * 0.00001
    else:
        accidents = distance(route) * 0.00002
    return accidents


#  get a list of next stops to be made form start city
def next_cities(routes, c):
    nextStop = []
    for r in routes:
        next = r.strip().split(" ")
        if next[0] == c or next[1] == c:
            nextStop.append(next[0], next[1], float(next[2]), float(next[3]), next[4])
    return nextStop


# -----------------------------------------------------------------------------------------------------------------

# cost function for segments, distance, time, safe
def cf(cost, le, speed, highway):
    c = 0
    if cost == 'segments':
        c = 1  # assuming edge cost will be 1
    elif cost == 'distance':
        c = le  # len(route)
    elif cost == 'time':
        c = le / speed
    elif cost == 'safe':
        c = safe(le)
    return c


def heuristic(cost, end_xy, cost_type):
    h = 0
    route_t, total_miles, total_segments, total_time = cost_type
    city = route_t[-1]
    if cost == "distance":
        start_xy = loc_city(city, gps_coords)
        h = distance(start_xy, end_xy)
    elif cost == "segments":
        seg_dist = 923
        start_xy = loc_city(city, gps_coords)
        h = distance(start_xy, end_xy) / seg_dist
    elif cost == "time":
        max_speed = 65
        start_xy = loc_city(city, gps_coords)
        h = distance(start_xy, end_xy) / max_speed
    elif cost == "safe":
        start_xy = loc_city(city, gps_coords)
        h = distance(start_xy, end_xy) * 1
    return h


# generate successor nodes
def successors(city):
    succ = routes[city].keys()
    return succ


def get_route(start, end, cost):
    """
    Find shortest driving route between start city and end city
    based on a cost function.
    1. Your function should return a dictionary having the following keys:
        -"route-taken" : a list of pairs of the form (next-stop, segment-info), where
           next-stop is a string giving the next stop in the route, and segment-info is a free-form
           string containing information about the segment that will be displayed to the user.
           (segment-info is not inspected by the automatic testing program).
        -"total-segments": an integer indicating number of segments in the route-taken
        -"total-miles": a float indicating total number of miles in the route-taken
        -"total-hours": a float indicating total amount of time in the route-taken
        -"total-expected-accidents": a float indicating the expected accident count on the route taken
    2. Do not add any extra parameters to the get_route() function, or it will break our grading and testing code.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """

    # route_taken = [("Martinsville,_Indiana", "IN_37 for 19 miles"),  ("Jct_I-465_&_IN_37_S,_Indiana", "IN_37 for 25 miles"), ("Indianapolis,_Indiana", "IN_37 for 7 miles")]

    # return {"total-segments": len(route_taken), "total-miles": 51, "total-hours": 1.07949, "total-expected-accidents": 0.000051, "route-taken": route_taken}

    # heapq documentation : https://docs.python.org/3/library/heapq.html
    # heapq referred from https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
    priority_visited = {}
    routes = load_road_seg()
    gps_coords = load_city_gps()
    # fringe = PriorityQueue()
    fringe = []
    route_t = [start]
    total_miles, total_segments, total_time, total_accidents = 0, 0, 0, 0
    initial = (route_t, total_miles, total_segments, total_time)
    priority = heuristic(cost, end, initial)
    heapq.heappush(fringe, (priority, initial))
    heapq.heapify(fringe)
    end_xy = loc_city(end, gps_coords)
    max_speed = maxSpeed(routes)
    seg_dist = max_seg_l(routes)
    visited = {}

    if start == end:
        return total_miles, total_segments, total_time, total_accidents  # 0, 0, 0, 0
    visited[start] == True
    priority_visited[start] = priority

    # while not fringe.empty():
    # checking the next stop from present location
    while len(fringe) != 0:
        st = heapq.heappop(fringe)
        visited.append(st[2])
        # next_cities = successors(start)
        nextStop = successors(st, routes, gps_coords, cost, end_xy, max_speed, seg_dist)
        for n in nextStop:
            total_segments = total_segments + 1
            total_miles, speed_l = routes[start][end]
            total_time = total_miles / max_speed
            total_accidents = safe(route_t)
            if n[2] == end:
                return {"total-segments": total_segments, "total-miles": total_miles, "total-hours": total_time,
                        "total-expected-accidents": total_accidents, "route-taken": (n[3])}
            heapq.heappush(fringe, n)

    return None


# Please don't modify anything below this line
#
if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise (Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "safe"):
        raise (Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n Total segments: %6d" % result["total-segments"])
    print("    Total miles: %10.3f" % result["total-miles"])
    print("    Total hours: %10.3f" % result["total-hours"])
    print("Total accidents: %15.8f" % result["total-expected-accidents"])

# -------------------------------------------------------------------------------------------------------------------
#                                                 Citations
# -------------------------------------------------------------------------------------------------------------------

# https://gist.github.com/rochacbruno/2883505
# https://scipbook.readthedocs.io/en/latest/routing.html (travelling salesman problem)
# https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
# https://sandipanweb.wordpress.com/2020/12/08/travelling-salesman-problem-tsp-with-python/
# https://www.codesdope.com/blog/article/priority-queue-using-heap/
# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# for heuristics : https://en.wikipedia.org/wiki/Admissible_heuristic |  https://en.wikipedia.org/wiki/Consistent_heuristic
