d = int(input())
h = int(input())
m = int(input())
s = int(input())

d_sec = d * 24 * 60 * 60
h_sec = h * 60 * 60
m_sec = m * 60

print(d_sec + h_sec + m_sec + s)

