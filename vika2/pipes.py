def checkpipes():
    n, m = input().split()
    n = int(n)
    m = int(m)

    pipes = []
    for i in range(n):
        pipes.append(input())

    compass = []
    for i in range(n+2):
        l = []
        for j in range(m+2):
            t = (0,0)
            l.append(t)
        compass.append(l)

    for i in range(n):
        for j in range(m):
            cell = pipes[i][j]
            west = compass[i+1][j][1]
            north = compass[i][j+1][0]

            if cell == 'A':
                if west or north:
                    return "Impossible"
                else:
                    compass[i+1][j+1] = (0,0)
            elif cell == 'B':
                if not (west ^ north):
                    return "Impossible"
                elif west:
                    compass[i+1][j+1] = (0,1)
                elif north:
                    compass[i+1][j+1] = (1,0)
            elif cell == 'C':
                if west and north:
                    compass[i+1][j+1] = (0,0)
                elif west and not north:
                    compass[i+1][j+1] = (1,0)
                elif not west and north:
                    compass[i+1][j+1] = (0,1)
                elif not west and not north:
                    compass[i+1][j+1] = (1,1)
            elif cell == 'D':
                if not (west and north):
                    return "Impossible"
                compass[i+1][j+1] = (1,1)
            
            if j == m-1:
                # Bannað að fara í austur
                if compass[i+1][j+1][1]:
                    return "Impossible"


            if i == n-1:
                # Bannað að fara í suður
                if compass[i+1][j+1][0]:
                    return "Impossible"
                                            
    return "Possible"

print(checkpipes())
