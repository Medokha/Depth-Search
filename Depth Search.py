# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:09:04 2022

@author: Dell
"""
# =============================================================================
#     Depth  Search
# =============================================================================
adj_list = {
            'a': ['b', 'c'],
            'b': ['d', 'e'],
            'c': ['b', 'f'],
            'd': [],
            'e': ['f'],
            'f': []
           }
color = {}
parent = {}
trav_time = {}
dfs_trav_output = []

for node in adj_list.keys():
    color [node] = 'white'
    parent[node] = None
    trav_time[node] = [-1,-1]

time = 0
def dfs(u):
    global time
    color[u] = 'gray'
    trav_time[u][0] = time
    dfs_trav_output.append(u)

    for q in adj_list[u]:
        if color[q] == 'white':
            parent[q] = u
            dfs(q)

    color[u] = 'black'
    trav_time[u][1] = time
    time+=1

dfs('a')
print("-----the output-----\n")

for node in adj_list.keys():
    print(node,"->",trav_time[node])

print()
print(color)
print(parent)
print(trav_time)
print()
print("traverse -->" ,dfs_trav_output)


