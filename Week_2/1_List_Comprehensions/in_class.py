# ex 1
def is_prime(n):
    if n == 1:
        return False
    for k in range(2, (n//2)+1):
        if (n % k) == 0:
            return False
    return True


lst1 = [1, 15, 2, 8, 31, 5, 9]
new_lst = [i for i in lst1 if is_prime(i)]
print(new_lst)


# ex 4
passwords = [
    ('pesho', 'qwe345!'),
    ('gosho', 'passwOrd1'),
    ('penka', '1a2b3c4d'),
]  # -> [('gosho', 'passwOrd1')]

strong_pass = [pair for pair in passwords if len(pair[1]) >= 8 and
               any(el.isdigit() for el in pair[1]) and
               any(el.islower() for el in pair[1]) and
               any(el.isupper() for el in pair[1])]

print(strong_pass)


import re


regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{7,}$"
result = [pair for pair in passwords if re.match(regex, pair[1]) ]
print(result)
