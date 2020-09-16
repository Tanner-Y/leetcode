a = """ def minMoves(arr):
    swaps = 0
    sorted = False
    l = len(arr)
    count_1 = sum(arr)
    count_0 = l-count_1
    left = (arr[:(l//2)])
    right = (arr[(l//2):])
    if sum(left) < sum(right):
        for i in range(count_0+1):
            if arr[i] == 1:
                swaps += count_0-i
        for i in range(count_0+1,l):
            if arr[i] == 0:
                swaps += i-count_0
    else:
        for i in range(count_1):
            if arr[i] == 0:
                swaps += count_1-i
        for i in range(count_1,l):
            if arr[i] == 1:
                swaps += i-count_1
        
    return swaps

print(minMoves([1,0,0,0,1,0,1])) """

b = """ def optimalPoint(magic, dist):
    for i in range(len(magic)):
        solution = i
        distPoints = dist[i:] + dist[:i]
        magicPoints = magic[i:] + magic[:i]
        currMagic = magicPoints.pop(0)
        for j in range(len(distPoints)):
            currMagic -= distPoints[j]
            
            if currMagic < 0:
                solution = -1
                break
            if magicPoints:
                currMagic += magicPoints.pop(0)
        if solution != -1:
            return solution
    return -1

print(optimalPoint([2,4,5,2],[4,3,1,3])) """

def largestArea(samples):
    # Write your code here
    n = len(samples)
    largest = 0
    for i in range(n):
        for j in range(n):
            if samples[i][j] == 1:
                counter=0
                y = i
                x = j
                while x < n-1 and samples[y][x] != 0 and (y+counter < n-1):

                    counter+=1
                    x+=1
                if counter <= largest:
                    continue
                valid = checkSubMatrix([i,j],[y+counter,x],samples)
                if valid and counter > largest:
                    largest = counter
    return largest

def checkSubMatrix(start,end, matrix):
        sy, sx = start[0], start[1]
        ey, ex = end[0], end[1]
        for y in range(sy,ey):
            for x in range(sx,ex):
                if matrix[y][x] == 0:
                    return False
        return True



s = [
    [1,1,1],
    [1,1,0],
    [1,0,1]]

print(largestArea(s))