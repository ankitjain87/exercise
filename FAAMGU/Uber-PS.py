# import requests
# import mysql.connector
# import pandas as pd

# Given a list of [origin, destination] pairs (you can think of them as plane tickets), sort them into a single continuous route.

# Sample Input

# [
#     ["SFO", "EWR"],
#     ["SJC", "LAX"],
#     ["DFW", "SJC"],
#     ["EWR", "OAK"],
#     ["LAX", "SFO"]
# ]
# Desired output

# ["DFW", "SJC", "LAX", "SFO", "EWR", "OAK"]

# 1 - dict => {dest: src},  dest= set(), 
# 2 - iterate over src, find this starting point. {}
# 3 - path = []
# 4 - Loop or recursive DFW - SJC - LAX 

# SFO - EWR - OAK
# {
#     SFO: EWR, 
#     SJC: LAX,.... }
    
#     O(N + U + U)

# Given a set of [origin, destination] nodes with no guarantees of connectedness and non-branching, find the longest continuous route. 

# Sample input
# [
#     ["SFO", "EWR"],
#     ["SJC", "LAX"],
#     ["DFW", "SJC"],
#     ["EWR", "OAK"],
#     ["PHL", "MSP"],
#     ["SLC", "ONT"],
#     ["LDN", "MSP"],
#     ["MSP", "ATL"],
#     ["LAX", "SFO"],
#     ["EWR", "TRT"],
#     ["SJC", "CDG"],
#     ["CDG", "NDL"],
#     ["EWR", "BOS"],
#     ["BOS", "PHL"]
# ]

# Desired output
# ["DFW", "SJC", "LAX", "SFO", "EWR", "BOS", "PHL", "MSP", "ATL"]



# path = [[SFO - LAX - EWR], [SJC - LAX - OAK - BOS]]
# SFO -> [SFO - LAX - EWR]
# SJC - [SJC - LAX - OAK - BOS]







# SFO -> [EWR]
# SJC -> [LAX, CDG]
# EWR -> [OAK, TRT, BOS]


# 1. Starting point 
# 3. path
# 2. dfs -> 



input_data = [
    ["SFO", "EWR"],
    ["SJC", "LAX"],
    ["DFW", "SJC"],
    ["EWR", "OAK"],
    ["PHL", "MSP"],
    ["SLC", "ONT"],
    ["LDN", "MSP"],
    ["MSP", "ATL"],
    ["LAX", "SFO"],
    ["EWR", "TRT"],
    ["SJC", "CDG"],
    ["CDG", "NDL"],
    ["EWR", "BOS"],
    ["BOS", "PHL"]
]

from collections import defaultdict
from copy import deepcopy


def dfs(src, data, route, path=[]):
    destinations = data[src]
    long = []
    while destinations:
        next_dest = destinations.pop(0)
        if next_dest in route:
            path = path + route[next_dest]
        else:
            path = dfs(next_dest, data, route, path)
            
        if not long or len(long) < len(path):
            long = path
        
                    
    long.append(src)
    return long


data_dict = defaultdict(list)
for src, dst in input_data:
    data_dict[src].append(dst)
    
route = {}

for key in data_dict.keys():
    data_copy = deepcopy(data_dict)
    path = dfs(key, data_copy, route)
    route[key] = path
    # print(path)
            
longest = [] 
for key, val in route.items():
    if len(val) > len(longest):
        longest = val

longest.reverse()
print(longest)
    
    


