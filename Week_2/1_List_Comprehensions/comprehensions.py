# 1. Write a list comprehension that filters all the numbers which are less than 5 or larger than 15.


tpl = (1,15,2,8,31,5,9)
lst = [i for i in tpl if i < 5 or i > 15]
print(lst)

# 2. Write a list comprehension that filters all the numbers which are prime.
# You will need an is_prime function to use in the conditional part

tpl = (1,15,2,8,31,5,9)


def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, (n//2)+1):
        if (n % k) == 0:
            return False
    return True


lst_primes = [i for i in tpl if is_prime(i)]
print(lst_primes)

# 3. Write a list comprehension that filters all the strings which are longer than 5 symbols.
#
# ['cat', 'dog', 'elephant', 'cucumber'] -> ['elephant', 'cucumber']

lst1 = ['cat', 'dog', 'elephant', 'cucumber']
lst2 = [word for word in lst1 if len(word) > 5]
print(lst2)

# 4. Write a list comprehension that filters all the users that have strong passwords.
# A 'strong' password means one lowercase, one uppercase, one digit and at least 8 symbols long.

lst = [
    ('pesho', 'qwe345!'),
    ('gosho', 'passwOrd1'),
    ('penka', '1a2b3c4d'),
]

strong = [pair for pair in lst if len(pair[1]) >= 8 and
          any(i.isdigit() for i in pair[1]) and
          any(i.islower() for i in pair[1]) and 
          any(i.isupper() for i in pair[1])]
print(strong)
