n=4

r1=1
r2=1
r3=2
r4=2
v=18

graph={
    0: [[1,1,r1], [3,0,v]], #nodes connected to 0
    1: [[0,1,r1], [2,1,r2]], #nodes connected to 1
    2: [[1,1,r2], [3,1,r3], [3,1,r4]], #nodes connected to 2
    3: [[0,0,-v], [2,1,r3], [2,1,r4]] #nodes connected to 3
}
