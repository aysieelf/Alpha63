print("Welcome to the “Find Your Inner Fun-Quotient” quiz!")
print("Each question has multiple answers, please write only the letter of your answer!")
print("Have fun! :)")
print()
points = 0

print()
# 1
print('''1. What’s your go-to comfort food?
a) Pizza
b) Ice Cream
c) Sushi
d) Salad''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 2
print('''2. Which superpower would you choose?

a) Flying
b) Invisibility
c) Time Travel
d) Super Strength''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 3
print('''3. If you were an animal, what would you be?

a) Cat
b) Dolphin
c) Eagle
d) Lion''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 4
print('''4. What’s your ideal weekend activity?

a) Hiking
b) Binge-watching series
c) Reading a book
d) Going to a concert''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 5
print('''5. Pick a color that speaks to your soul.

a) Blue
b) Red
c) Green
d) Purple''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 6
print('''6. How do you handle a bad day?

a) Call a friend
b) Eat chocolate
c) Exercise
d) Meditate''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 7
print('''7. What’s your dream travel destination?

a) Paris
b) Tokyo
c) New York
d) Bali''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 8
print('''8. If you could have dinner with anyone, who would it be?

a) A historical figure
b) A famous musician
c) A renowned author
d) A fictional character''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 9
print('''9. What’s your favorite season?

a) Spring
b) Summer
c) Autumn
d) Winter''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")
print()
# 10
print('''10. Choose your spirit snack.

a) Chips
b) Chocolate
c) Fruit
d) Popcorn''')

x = False
while not x:
    answer = input("Write your answer: ")
    if answer in "aA":
        points = points + 10
        x = True
    elif answer in "bB":
        points = points + 20
        x = True
    elif answer in "cC":
        points = points + 30
        x = True
    elif answer in "dD":
        points = points + 40
        x = True
    else:
        print("Please, write a valid letter! :)")

print()
if 100 <= points <= 160:
    print('''The Chill Cat
    
You’re laid-back, relaxed, and take life as it comes. 
You love cozy nights in, and your friends often come to you for your calming presence. 
Keep spreading those good vibes!''')

elif 170 <= points <= 240:
    print('''The Adventurous Dolphin
    
Energetic and always on the move, you love exploring new places and trying new things. 
Your curiosity knows no bounds, and you’re the life of the party. Keep making waves!''')

elif 250 <= points <= 320:
    print('''The Wise Eagle

You’re thoughtful, introspective, and always looking to the future. 
You value deep conversations and enjoy spending time in nature. 
Your wisdom is a beacon for those around you.''')

elif 330 <= points <= 400:
    print('''The Bold Lion

Confident, brave, and a natural leader, you tackle challenges head-on. 
You’re not afraid to take risks, and you inspire others with your courage. 
Keep roaring and leading the pride!''')

