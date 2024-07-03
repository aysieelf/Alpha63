# receive N amount of targets to hit
# the first who hits all targets wins the round.
#
# However, George and Peter shoot at different speeds and accuracy, so for example
# George Gs secs
# Peter Ps secs
# George Gl latency
# Peter Pl latency
#
# Gl + Gs + Gl secs
#
# Input
# Read from the standard input:
#
# On the first line - the number N - the number of targets.
# On the second line - Gs - George's speed.
# On the third line - Gl - George's latency.
# On the fourth line - Ps - Peter's speed
# On the fifth line Pl - Peter's latency.

# Output
# Print to the standard output:
#
# There is one line of output:
# George - if George wins
# Peter - if Peter wins
# Draw - if the amount it takes is the same for both of them

# Constraints
# 1 <= N, Gs, Gl, Ps, Pl <= 232

# Sample Tests
# Input
# 5

# 1
# 1
# 2
# 2
# Output
# George
# Description
# There are 5 targets.
# George's speed is 1 and the latency is 1. The latency is applied twice. So (5 targets * 1 sec) = 5 + 1 sec + 1 sec = 7 sec
# Peter's speed is 2 and the latency is 2. The latency is applied twice. So (5 targets * 2 sec) = 10 + 2 sec + 2 sec = 14 sec
#
# So George wins this round!
# Input
# 3
# 3
# 1
# 1
# 1
# Output
# Peter
# Input
# 4
# 5
# 1
# 3
# 5
# Output
# Draw
#
# t = int(input())
# gs = int(input())
# gl = int(input())
# ps = int(input())
# pl = int(input())
#
# gosho = (t * gs) + (2 * gl)
# pesho = (t * ps) + (2 * pl)
#
# if gosho < pesho:
#     print('George')
# elif gosho > pesho:
#     print('Peter')
# else:
#     print('Draw')

# =================================== ex2
# numbers = []
#
# for n in range(5):
#     numbers.append(input())
#
# output = ''
# for pr in numbers:
#     product = int(pr[0]) * int(pr[1]) * int(pr[2])
#     output = output + str(product)[-1]
#
# print(output)

# =================================== ex3
# p = int(input())
#
# safe_houses = input().split()
# safe_houses = [int(safe) for safe in safe_houses]
#
# distances = []
#
# for spawn_point in range(p):
#     min_distance = p
#     for safe_house in safe_houses:
#         distance = abs(spawn_point - safe_house)
#         if distance < min_distance:
#             min_distance = distance
#     distances.append(min_distance)
#
# max_distance = max(distances)
# print(max_distance)

#
# p = int(input())
# safe_houses = input().split()
# safe_houses = [int(house) for house in safe_houses]
#
# points = []
#
# for spawn in range(p):
#     min_dist = p
#     for safe in safe_houses:
#         distance = abs(spawn - safe)
#         if distance < min_dist:
#             min_dist = distance
#     points.append(min_dist)
#
# print(max(points))

p = int(input())
safe_houses = input().split()
safe_houses = [int(house) for house in safe_houses]

points = []

for spawn in range(p):
    min_dist = p
    for safe in safe_houses:
        dist = abs(spawn - safe)
        if dist < min_dist:
            min_dist = dist
    points.append(min_dist)

print(max(points))