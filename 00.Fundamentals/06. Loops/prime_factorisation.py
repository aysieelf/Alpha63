# number = int(input())


# while number != 1:
#     for prime in range(1, number+1):
#         for i in range(1, prime+1):
#             modulus = prime % i
#             if (modulus == 0) and (prime >= 2) and (prime == i or prime == 1):
#                 while number % prime == 0:
#                     print (prime)
#                     number = number / prime
#                     number = int(number)
#                 if number == 1:
#                      break
#             if number == 1:
#                  break
#     if number == 1:
#         break


# # Read input for n
# n = int(input())
 
# # Loop through the range from 2 to half of n including so that you include 2 which is prime but do not include 1 which is not prime
# for i in range(2, int(n / 2) + 1):
#     # Check if n is divisible by i
#     while n % i == 0:
#         # If it is, then print i and divide n by i to calculate the remainder
#         print(i)
#         n /= i


n = int(input())

for i in range(2, int(n/2) +1, 1):
    while n % i == 0:
        print (i)
        n = n / i