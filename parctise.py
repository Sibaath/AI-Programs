import heapq


def reconstruct(state,parent):
    path = []
    while state:
        path.append(state)
        state = parent[state]
    return path[::-1]

def neighbours(jug1,jug2,jug1c,jug2c):
    
    neighbour = []
    
    neighbour.append((jug1c,jug2))
    neighbour.append((jug1,jug2c))
    
    neighbour.append((0,jug2))
    neighbour.append((jug1,0))
    
    neighbour.append((0,jug2))
    neighbour.append(jug1,0)
    
    water = min(jug1,jug2c-jug2)
    neighbour.append((jug1-water,jug2+water))
    
    water = min(jug1c-jug1,jug2)
    neighbour.append((jug1+water,jug2-water))
      
    return neighbour

def diff(jug1,jug2,state):
    return min(abs(jug1c-jug1[0]),abs(jug2c-jug2[1]))

def astar(jug1c,jug2c,res,tar):
    start = (0,0)
    pq = []
    visited = set()
    visited.add(start)
    parent = {}
    heapq.heappush(pq,(diff(start,res),start))
    parent[start] = None
    
    while pq:
        _,move,(jug1,jug2) = heapq.heappop(pq)
        
        if (tar == 1 and jug1 == tar) or (tar == 2 and jug2 == tar):
            return reconstruct((jug1,jug2),parent)
        
        for state in neighbours(jug1,jug2,jug1c,jug2c):
            if state not in visited:
                visited.add(state)
                parent[state] = (jug1,jug2)
                heapq.heappush(pq,(diff(state,res),state))
        return None

def water_jug(jug1,jug2,res,tar):
    solution = astar(jug1,jug2,res,tar)
    if solution:
        for i in solution:
            print(i)
    

jug1c = int(input())
jug2c = int(input())
res = int(input())
tar = int(input())
water_jug(jug1c,jug2c,res,tar)