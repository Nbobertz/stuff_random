import math
from collections import deque


class NearestNeighborIndex:
    """
    TODO give me a decent comment (hello, this is Nick phoning in, go to my function to see inline comments)

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points

    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        min_dist = None
        min_point = None

        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    # def find_nearest_fast(self, query_point):
    #     """
    #     TODO: Re-implement me with your faster solution.
    #
    #     find_nearest_fast returns the point that is closest to query_point. If there are no indexed
    #     points, None is returned.
    #     """
    #
    #     # #below is my code
    #
    #     #changes min to float(inf) this prevents a check during first loop since it's impossible for the distance between points to be larger than inf. Speed up stuff.
    #     min_dist = float('inf')
    #     min_point = None
    #
    #
    #     #this process uses the manhatten distance. It takes the absolute value of the distnaces between two points and updates if it is closer.
    #
    #     #think of manhatten as a graph
    #     #graph =
    #     #[0,0,1,0]
    #     #[0,0,1,0]
    #     #[0,1,1,0]
    #     #[1,1,0,0]
    #
    #     #there is no reason for us to check tangental when we can just check to the left,right,up,down. This saves us from having to calculate a circle around the point to see if we have another point in it. We just see if we can get to the nearest point via 2,3,4,5,6,7 direction changes.
    #
    #     #simply put, by only checking directions = [1,0],[-1,0],[0,1],[0,-1] and not 8 way diretcions we can simply skip half the checks that an circular check would do. This proccess works well on a graph.
    #
    #     #for more information about the pro's vs con's on Euclidean distance vs Manhattan distance see https://www.datacamp.com/tutorial/manhattan-distance
    #
    #     #now if you really want to speed things up you should use GeoHashing on your points ahead of time. Store this data in Reddis or Elasticache (AWS) with a microservice that stores the lookup and you can skip a ton of this computational time since we are just refrencing a glorified hashmap at the end of the day.
    #
    #     #-Nick B (runs at 1.38-1.52)
    #
    #     #this is the simple python one liner way of doing the manhatten distance. Saves time.
    #     for point in self.points:
    #
    #         dist = abs(point[0] - query_point[0]) + abs(point[1] - query_point[1])
    #
    #         # Update the closest point if this one is closer
    #         if dist < min_dist:
    #             min_dist = dist
    #             min_point = point
    #
    #     return min_point

    def find_nearest_fast(self, query_point):
        """
        TODO: Re-implement me with your faster solution.

        find_nearest_fast returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        # #below is my code

        #changes min to float(inf) this prevents a check during first loop since it's impossible for the distance between points to be larger than inf. Speed up stuff.
        min_dist = float('inf')
        min_point = None

        maxx = float('-inf')

        arr = []
        for x in self.points:
            arr.append(x)

        for tup in arr:
            x,y = tup
            dist = int((x**2)+(y**2))
            if dist >= maxx:
                maxx = dist



        tmp = int(dist**.5)
        tmp = int(dist ** .5)
        bound = tmp * 2
        boundaries = [0, bound], [0, (bound * -1)], [bound, 0], [(bound * -1), 0]

        # Build the grid with 'bound' size
        grid = []

        # Create a 2D grid (list of lists) and fill it with 0s
        for _ in range(bound):
            grid.append([0] * bound)

        ROWS,COLS = len(grid),len(grid[0])
        print(ROWS,COLS)

    def build_grid_and_BFS(self,targets):

        #this builds our 'playfield' for dfs on points. It takes the input points and builds a grid off of it.


        maxx = float('-inf')

        arr = []
        for x in self.points:
            arr.append(x)

        for tup in arr:
            x, y = tup
            dist = int((x ** 2) + (y ** 2))
            if dist >= maxx:
                maxx = dist

        tmp = int(dist ** .5)
        if tmp%4==0:
            bound = tmp
        else:
            bound = (tmp // 4 + 1) * 4 #we are making everything divisible by 4 so we can visualize it better

            # Build the grid with 'bound' size
        grid = []

        # Create a 2D grid (list of lists) and fill it with 0s
        for _ in range(bound):
            grid.append([0] * bound)

        #Now we are replacing the self.points with 1's in the graph

        for tup in arr:
            x, y = tup
            grid[x][y] = 1

        #Now we are going to do the same with the target tups, but now they are 2's
        arr2 = []
        for x in targets:
            arr2.append(x)

        for tup in arr2:
            x,y = tup
            grid[x][y] = 2


        #prints human readable grid for viss
        quart1 = int(bound*.25)
        quart2 = int(bound*.5)
        quart3 = int(bound*.75)
        print(grid[0:quart1])
        print(grid[quart1:quart2])
        print(grid[quart2:quart3])
        print(grid[quart3:])

        #time for BFS

        ROWS,COLS = len(grid),len(grid[0])
        visited = set() #keep track of where we have been as tuple

        def bfs(r, c):
            # BFS to find the closest '2' from (r, c)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 cardinal directions (up, down, left, right)
            q = deque([(r, c, 0)])  # Queue stores (row, col, distance)
            visited.add((r, c))

            while q:
                row, col, dist = q.popleft()

                # Check if we found a '2'
                if grid[row][col] == 2:
                    return (row, col), dist

                # Explore neighbors
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col, dist + 1))

        tmp3 = []
        #iterate through entire graph
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1
                    and (r,c) not in visited):
                    route = bfs(r,c)
                    tmp3.append(route)
                    visited.clear()

        for entry in range(0,len(arr)):
            x,y = tmp3[entry][0]
            dist = tmp3[entry][1]
            print("The closest point to your {a} is {b} and it takes {c} units to get there".format(a=arr[entry],b=(x,y),c=dist))






    def find_nearest(self, query_point):
        """
        TODO comment me.
        """

        # TODO implement me so this class runs much faster.
        return self.find_nearest_fast(query_point)
