price = float(input())
payment = float(input())



change = payment - price

change_leva = change//1
if change_leva > 0:
    print (f'{int(change_leva)} x 1 lev')
    change = change - change_leva*1
    change = round(change, 2)

change_50st = change//0.5
if change_50st > 0:
    print (f'{int(change_50st)} x 50 stotinki')
    change = change - change_50st*0.5
    change = round(change, 2)

change_20st = change//0.2
if change_20st > 0:
    print (f'{int(change_20st)} x 20 stotinki')
    change = change - int(change_20st)*0.2
    change = round(change, 2)

change_10st = change//0.1
if change_10st > 0:
    print(f'{int(change_10st)} x 10 stotinki')
    change = change - change_10st*0.1
    change = round(change, 2)

change_5st = change//0.05
if change_5st > 0:
    print (f'{int(change_5st)} x 5 stotinki')
    change = change - change_5st*0.05
    change = round(change, 2)

change_2st = change//0.02
if change_2st > 0:
    print (f'{int(change_2st)} x 2 stotinki')
    change = change - change_2st*0.02
    change = round(change, 2)

change_1st = change//0.01
if change_1st > 0:
    print (f'{int(change_1st)} x 1 stotinka')
    change = round(change, 2)
