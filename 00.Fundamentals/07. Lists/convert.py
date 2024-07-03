# Input
# 0 15 30
# Output
# 32
# 59
# 86

celsius_list = input().split(' ')

farenheit_list = []
for i in range(len(celsius_list)):
    temp_farenheit = (int(celsius_list[i]) * (9/5)) + 32
    farenheit_list.append(round(temp_farenheit))

for ii in range(len(farenheit_list)):
    print(farenheit_list[ii])



celsius_list = input().split(' ')

for i in range(len(celsius_list)):
    temp_celsius = int(celsius_list[i])
    temp_farenheit = (temp_celsius * (9/5)) + 32
    print(round(temp_farenheit))
