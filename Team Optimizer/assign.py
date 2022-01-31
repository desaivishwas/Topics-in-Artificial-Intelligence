#!/usr/local/bin/python3
# assign.py : Assign people to teams
#
# Code by: Sharanbasav-ssumbad , Vishwas-visdesai , Shilpa-shkumari
#
# Based on skeleton code by R. Shah and D. Crandall, January 2021
#
import random
import string
import jsons
import math
import sys

import time


# Function to format the input file accordingly so that accessing the list of name is easy.
# This function will return a dictionary with keys userId, prefered-list and non-prefered.
def format_file(file):
    input_file = file
    input_data = []
    with open(input_file) as file:
        for l in file:
            l = l.replace("\n", "")
            l_data = l.split(" ")
            prefered = []
            not_prefered = []
            if l_data[1] != "_":
                sep = l_data[1].split("-")
                prefered = [pref_person for pref_person in sep]
            if l_data[2] != "_":
                sep = l_data[2].split("-")
                not_prefered = [non_pref_person for non_pref_person in sep]

            data = {'UserID': l_data[0], 'prefered_list': prefered, 'not_prefered_list': not_prefered, 'team_index': 0}
            input_data.append(data)

    return input_data


# This function will calculate the cost by comparing the elements in the list and data and return the
# cost for that combination
def cost_calc(list, data):
    cost = 0
    for i in list:
        for j in i:
            usr_pref = uid_check(data, j)
            for m in range(len(i)):
                if i[m] != j:
                    if i[m] in usr_pref['prefered_list']:
                        continue
                    else:
                        cost = cost + 1
    for i in list:
        for j in i:
            usr_pref = uid_check(data, j)
            for m in range(len(i)):
                if i[m] != j:
                    if i[m] in usr_pref['not_prefered_list']:
                        cost = cost + 1
    return cost


# used in calculation of cost according to the prefered and non prefered list
def uid_check(list, id):
    for i in list:
        if i["UserID"] == id:
            return i

# The solver function to give the teams accordingly to the user preference and best optimal function.
def solver(teams):
    data = format_file(teams)
    students = []
    for i in range(0, len(data)):
        students.append(data[i]['UserID'])
    len_std = len(students)
    cnt = 0
    if len_std % 3 != 0:
        cnt = 1
    len_init = int(len_std / 3) + cnt
    #
    strt = []
    indx1 = 0
    for i in range(len_init):
        tmp = []
        end = indx1 + 3
        if end > len(students):
            end = len(students)
        for k in range(indx1, end):
            tmp.append(students[k])
        strt.append(tmp)
        indx1 += 3
    initial_cost = cost_calc(strt, data)
    new_cost = 0
    # we are interchanging the users accordingly as many times as to give out the best cost.
    for i in range(len(strt) - 1):
        for k in range(i + 1, len(strt) - 1):
            for j in range(3):
                strt[i][j], strt[k][j], = strt[k][j], strt[i][j]
                new_cost = cost_calc(strt, data)
                if new_cost >= initial_cost:
                    strt[i][j], strt[k][j] = strt[k][j], strt[i][j]
                else:
                    initial_cost = new_cost
    lstindex = len(strt) - 1
    for i in range(0, len(strt) - 1):
        for j in range(len(strt[lstindex])):
            strt[i][j], strt[lstindex][j] = strt[lstindex][j], strt[i][j]
            new_cost = cost_calc(strt, data)
            if new_cost >= initial_cost:
                strt[i][j], strt[lstindex][j] = strt[lstindex][j], strt[i][j]
            else:
                initial_cost = new_cost
    result = {"assigned-groups": [], "total-cost": ''}
    final_cost = initial_cost - len(strt)
    for i in strt:
        result["assigned-groups"].append("-".join([x for x in i]))
    result["total-cost"] = final_cost

    # return result

    # Simple example. First we yield a quick solution
    yield (result)

    # Then we think a while and return another solution:
    time.sleep(10)
    yield (result)

    # This solution will never be found, but that's ok; program will be killed eventually by the
    #  test script.
    while True:
        pass

    yield (result)


# solver(sys.argv[1]) : calling solver function

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        raise (Exception("Error: expected an input filename"))
    solution = solver(sys.argv[1])
    print(solution)

    
