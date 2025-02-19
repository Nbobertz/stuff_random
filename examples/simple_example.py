
# Please create a simple example use of the pynn library for your end user. Assume that the end
# user knows a lot about their subject matter but has only a basic understanding of Python.
from pynn import nearest_neighbor_index as ny

#throw in some points as an array of tuples below. Feel free to pull these from wherever.
#the data goes in as x,y points.
#What this means is that you can simply pull the x,y data from an attribute table and throw it into the following tuple list.


#just
your_tup_data = [
    (1,0),
    (0,1),
    (15,15),
    (29,29),
    (29,0),
    (49,49),
    (200,100),
    (340,400),
    #etc. Put your data in (x,y) format above
]

tups_to_query = [
    (10,0),
    (20,0),
    (30,0),
    (50,50),
    (60,60),
    (1000,1000)


]

test = ny.NearestNeighborIndex(your_tup_data)

#loop through tups_to_query and we will figure out what is the closest point to it from your input data (your_tup_data)
for tup in tups_to_query:
    print("The closest tup (coordinate) to {a} is {b}. Brought to you by Nick!".format(a=tup,b=test.find_nearest_fast(tup)))



# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.
