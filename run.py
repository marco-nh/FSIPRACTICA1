# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_graph_search(ab).path())
print(search.branch_and_bound_subest_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] (BFG) : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

print("---------------------------------------------")
df = search.GPSProblem('D', 'F'
                       , search.romania)

print(search.breadth_first_graph_search(df).path())
print(search.depth_first_graph_search(df).path())
print(search.branch_and_bound_graph_search(df).path())
print(search.branch_and_bound_subest_graph_search(df).path())

# Result:
# [<Node F>, <Node B>, <Node P>, <Node C>, <Node D>] (DFG) : 211 + 101 + 138 + 120 = 570
# [<Node F>, <Node S>, <Node R>, <Node C>, <Node D>] 99 + 80 + 146 + 120 = 445

print("---------------------------------------------")

oh = search.GPSProblem('O', 'H'
                       , search.romania)

print(search.breadth_first_graph_search(oh).path())
print(search.depth_first_graph_search(oh).path())
print(search.branch_and_bound_graph_search(oh).path())
print(search.branch_and_bound_subest_graph_search(oh).path())

# Result:
# [<Node H>, <Node U>, <Node B>, <Node F>, <Node S>, <Node O>] (BFG) : 98 + 85 + 211 + 99 + 151 = 644
# [<Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>] : 98 + 85 + 101 + 97 + 80 + 151 = 620