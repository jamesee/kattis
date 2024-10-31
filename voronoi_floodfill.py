
from pprint import pprint
from math import inf

# solve voronoi diagram using floodfill
def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

def PDMap(row: int, col: int, sites: list[list[int, int]]) -> list[list[int, int]]:

    sitemap = [[-1 for _ in range(col)] for _ in range(row)]
    distmap = [[inf for _ in range(col)] for _ in range(row)]
    delta = [(-1, 0), (0,-1), (1, 0), (0, 1)]

    queue = list()
    visited = set()

    #initialise sites
    for index,(r, c) in enumerate(sites):
        queue.append((r, c, index, 0))      # (r, c, index, distance from sites[index])
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
            elif (nr, nc) in visited and newdist < distmap[nr][nc]:
                    sitemap[nr][nc] = index
                    distmap[nr][nc] = newdist
            elif (nr, nc) in visited and newdist == distmap[nr][nc]:
                    sitemap[nr][nc] = 'X'

    print('-'*38, '[distmap]')
    pprint(distmap)
    print('-'*38, '[sitemap]')
    pprint(sitemap)
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
    # mTightPrint(PDMap(50,80,[[20,10], [30,30],[40,20],[45,55],[10,55],[35,70],[35,60]]))
    # mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    PDMap(10,10,[[2,3],[4,9],[7,2]])
    # mTightPrint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # pprint(PDMap(10,10,[[2,3],[4,9],[7,2]]))
    # pprint(PDMap(7,8,[[1,3],[4,7],[6,2]]))
