# 1. Write a list comprehension that filters all the numbers which are less than 5 or larger than 15.


lst1 = [1, 15, 2, 8, 31, 5, 9]
new_lst = [i for i in lst1 if 15 < i or i < 5]
print(new_lst)

# 2. Write a list comprehension that filters all the numbers which are prime.
# You will need an is_prime function to use in the conditional part


def is_prime(n):
    if n > 1:
        for k in range(2, (n//2)+1):
            if (n % k) == 0:
                return False
        return True


lst2 = [1, 15, 2, 8, 31, 5, 9]
prime_nums = [i for i in lst2 if is_prime(i)]
print(prime_nums)

# 3. Write a list comprehension that filters all the strings which are longer than 5 symbols.


lst3 = ['cat', 'dog', 'elephant', 'cucumber']
longer_than5 = [word for word in lst3 if len(word) > 5]
print(longer_than5)

# 4. Write a list comprehension that filters all the users that have strong passwords.
# A 'strong' password means one lowercase, one uppercase, one digit and at least 8 symbols long.


passwords = [
    ('pesho', 'qwe345!'),
    ('gosho', 'passwOrd1'),
    ('penka', '1a2b3c4d'),
]

# 4.1


strong_pass = [pair for pair in passwords if len(pair[1]) >= 8 and
               any(el.isdigit() for el in pair[1]) and
               any(el.islower() for el in pair[1]) and
               any(el.isupper() for el in pair[1])]

print(strong_pass)

# 4.2 (imported re on line 50 for readability, because it's used for this exercise)


import re

regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{7,}$"
result = [pair for pair in passwords if re.match(regex, pair[1])]
print(result)
