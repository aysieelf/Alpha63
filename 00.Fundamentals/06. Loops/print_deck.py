# Input
# 5
# Output
# 2 of spades, 2 of clubs, 2 of hearts, 2 of diamonds
# 3 of spades, 3 of clubs, 3 of hearts, 3 of diamonds
# 4 of spades, 4 of clubs, 4 of hearts, 4 of diamonds
# 5 of spades, 5 of clubs, 5 of hearts, 5 of diamonds


card = input()
count = 0

if card.isdigit():
    count = int(card) - 1
elif card in 'JQKA':
    if card == 'J':
        count = 11 - 1
    elif card == 'Q':
        count = 12 - 1
    elif card == 'K':
        count = 13 - 1
    elif card == 'A':
        count = 14 - 1

for i in range(count):
    if (i + 1) < 10:
        new_card = i + 2
        print(f'{new_card} of spades, {new_card} of clubs, {new_card} of hearts, {new_card} of diamonds')
    if (i + 1) > 9:
        if (i+1) == 10:
            new_card = 'J'
            print(f'{new_card} of spades, {new_card} of clubs, {new_card} of hearts, {new_card} of diamonds')
        if (i+1) == 11:
            new_card = 'Q'
            print(f'{new_card} of spades, {new_card} of clubs, {new_card} of hearts, {new_card} of diamonds')
        if (i+1) == 12:
            new_card = 'K'
            print(f'{new_card} of spades, {new_card} of clubs, {new_card} of hearts, {new_card} of diamonds')
        if (i+1) == 13:
            new_card = 'A'
            print(f'{new_card} of spades, {new_card} of clubs, {new_card} of hearts, {new_card} of diamonds')
    
    
