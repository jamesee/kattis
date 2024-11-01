
from pprint import pprint
from math import inf

# solve voronoi diagram using floodfill
def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

#=======================================================================[brute-force method]
def fill_map(pt: list[int,int], sites: list[list[int,int]])-> int | str:
    distance = list(map(lambda p2: (pt[0]-p2[0])**2 + (pt[1] - p2[1])**2, sites))
    return 'X' if distance.count(min(distance)) > 1 else distance.index(min(distance))

def PDMap_bruteforce(row: int,col: int,sites: list[list[int]]) -> list[list[int]]:
    return list(list(fill_map([r,c], sites) for c in range(col)) for r in range(row))

#=======================================================================[floodfill method ver1]
'''
working code but inefficient

pseudocode:
1.  use the sites to floodfill with its index number. 
    If the sites can floodfill simultanenously, theotically we can get the equidistant boundary when each floodfill meet

2.  as we do floodfill of each site in sequence, the lower indexed site will encrouch into other's region

3.  do 2 floodfill maps in opposite sequence of sites. 

4.  Find the region where the 2 maps are different, then calculate the euclidean distant of the different pixels.

'''


def floodfil(row: int,col: int,sites: list[list[int,int,int]]) -> list[list[int]]:
    mymap = [['' for _ in range(col)] for _ in range(row)]
    mydir = [(-1, 0), (0,-1), (1, 0), (0, 1)]

    queue = list()
    visited = set()
    for site in sites:
        r, c, index = site
        mymap[r][c] = index
        queue.append(site)
        visited.add((r, c))

    while queue:
        r, c, index = queue.pop(0)
        for dr, dc in mydir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0<= nc < col and (nr, nc) not in visited:
                mymap[nr][nc] = index
                queue.append((nr, nc, index))
                visited.add((nr, nc))
    return mymap

def euclidean_dist(p1: tuple[int,int], p2: tuple[int, int]) -> float:
    return ((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def diff_maps(map1: list[list[int]], map2: list[list[int]]) -> list[tuple[int,int]]:

    row, col = len(map1), len(map1[0])
    return [(r, c, map1[r][c], map2[r][c]) for c in range(col) for r in range(row) if map1[r][c] != map2[r][c]]

def PDMap_floodfill_ver1(row: int,col: int,sites: list[list[int]]) -> list[list[int]]:

    mysites = [(*site, index) for index, site in enumerate(sites)]
    mysites_reverse = [(*site,len(sites) - i) for i, site in enumerate(sites[::-1])]

    map1 = floodfil(row, col, mysites)
    map2 = floodfil(row, col, mysites_reverse)
    diff = diff_maps(map1, map2)

    for d in diff:
        r, c, s1, s2 = d
        if euclidean_dist((r,c), sites[s1]) <  euclidean_dist((r,c), sites[s2]):
            map1[r][c] = s1
        elif euclidean_dist((r,c), sites[s1]) >  euclidean_dist((r,c), sites[s2]):
            map1[r][c] = s2
        else:
            map1[r][c] = 'X'
    return map1

#=======================================================================[floodfill method ver2]
'''
not working yet, debugging


pseudocode:

1.  create 2 maps. sitemap and distmap (to store the minimum distance)

2.  store the coordinate, index and distance as (r, c, index, distance) when doing floodfill
    distance is the distance from the site[index]

3.  evaluate each pixel for:
    i.  if not visited before, fill the sitemap and distmap immediately
    ii. if visited before, 
            if newdist < distmap[nr][nc], then distmap[nr][nc] = newdist and sitemap[nr][nc] = index
            if newdist == distmap[nr][nc], then sitemap[nr][nc] = 'X'

'''

def PDMap_floodfill_ver2(row: int, col: int, sites: list[list[int, int]]) -> list[list[int, int]]:

    sitemap = [[-1 for _ in range(col)] for _ in range(row)]
    distmap = [[inf for _ in range(col)] for _ in range(row)]
    delta = [(-1, 0), (0,-1), (1, 0), (0, 1)]

    queue = list()
    visited = set()

    #initialise sites
    for index,(r, c) in enumerate(sites):
        queue.append((r, c, index, 0))          # (r, c, index, distance from sites[index])
        sitemap[r][c] = index
        distmap[r][c] = 0
    
    while queue:
        r, c, index, distance = queue.pop(0)
        visited.add((r, c))

        newdist = distance + 1
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited:
                sitemap[nr][nc] = index
                distmap[nr][nc] = newdist
                queue.append((nr, nc, index, newdist))
            elif (nr, nc) in visited:
                if newdist < distmap[nr][nc]:
                    sitemap[nr][nc] = index
                    distmap[nr][nc] = newdist
                elif newdist == distmap[nr][nc]:
                    sitemap[nr][nc] = 'X'

    # print('-'*38, '[distmap]')
    # pprint(distmap)
    # print('-'*38, '[sitemap]')
    # pprint(sitemap)
    return sitemap


'''
0000000X11
0000000111
0000000111
000000X111
X000001111
22222X1111
2222221111
2222222111
2222222111
2222222X11
'''



if __name__ == "__main__":

    print('-'*38, '[brute-force method]')
    mTightPrint(PDMap_bruteforce(10,10,[[2,3],[4,9],[7,2]]))
    print()
    
    print('-'*38, '[floodfill method ver1]')
    mTightPrint(PDMap_floodfill_ver1(10,10,[[2,3],[4,9],[7,2]]))
    print()
    
    print('-'*38, '[floodfill method ver2]')
    mTightPrint(PDMap_floodfill_ver2(10,10,[[2,3],[4,9],[7,2]]))

    # mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
    # mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # print()
    # mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # pprint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # pprint(PDMap(7,8,[[1,3],[4,7],[6,2]]))
