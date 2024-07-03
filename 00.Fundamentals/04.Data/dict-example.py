names = {
'Fred': 'Hello Fred',
'Xander': 'Hello Xander',
'Joe': 'Hello Joe',
'Arnold': 'Hello Arnold'
}

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))


raining = False
print("Let's go to the", 'beach' if not raining else 'library')
raining = True
print("Let's go to the", 'beach' if not raining else 'library')

if 'bar' in {'foo', 'bar', 'baz'}:
    print(1)
    print(2)