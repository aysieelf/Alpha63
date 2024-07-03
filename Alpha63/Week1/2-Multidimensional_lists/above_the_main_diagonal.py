# N for how many rows and columns our 2d list has
n = int(input())

# creates a 2d list
a = [[2**(i+j) for j in range(n)] for i in range(n)]

# summarising only above the diagonal
ttl = 0
for index in range(n):
    ttl += sum(a[index][index+1:])

# printing the total sum
print(ttl)

