def rotateImage(a):
    n = len(a)
    for x in range(int(n/2)):
        for y in range(x,n-x-1):
            tmp = a[x][n-1-y]
            
            a[x][n-1-y] = a[x][y]
            a[x][y] = a[n-1-y][x]
            a[n-1-x][y] = a[n-1-y][n-1-x]
            a[n-1-y][n-1-x] = tmp
    return a



a = [
[1,2,3], 
[4,5,6], 
[7,8,9]]


out = [
[7,4,1], 
[8,5,2], 
[9,6,3]]

print(rotateImage(a))

