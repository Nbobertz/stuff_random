
# Please create a simple example use of the pynn library for your end user. Assume that the end
# user knows a lot about their subject matter but has only a basic understanding of Python.
from pynn import nearest_neighbor_index as ny

#put your data into the array titled your_tup_data, then put your target x,y cordinates into tups_to_query and press run.

#what happens behind the scene is that we will construct a grid in memory, put your points in the grid, and then bfs


#just
your_tup_data = [
    (1,1),
    (5,5),
    (20,20)
    #etc. Put your data in (x,y) format above
]

tups_to_query = [
    (0,1),
    (7,2),
    (3,2),
]

test = ny.NearestNeighborIndex(your_tup_data)


test.build_grid_and_BFS(targets=tups_to_query)


#
# #loop through tups_to_query and we will figure out what is the closest point to it from your input data (your_tup_data)
# for tup in tups_to_query:
#     print("The closest tup (coordinate) to {a} is {b}. Brought to you by Nick!".format(a=tup,b=test.find_nearest_fast(tup)))



# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.
