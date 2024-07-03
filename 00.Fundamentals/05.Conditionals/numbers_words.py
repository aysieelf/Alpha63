number = int(input())

names = {
0 : 'zero',
1 : 'one',
2 : 'two',
3 : 'three',
4 : 'four',
5 : 'five',
6 : 'six',
7 : 'seven',
8 : 'eight',
9 : 'nine',
10 : 'ten',
11 : 'eleven',
12 : 'twelve',
13 : 'thirteen',
14 : 'fourteen',
15 : 'fifteen',
16 : 'sixteen',
17 : 'seventeen',
18 : 'eighteen',
19 : 'nineteen',
20 : 'twenty',
30 : 'thirty',
40 : 'fourty',
50 : 'fifty',
60 : 'sixty',
70 : 'seventy',
80 : 'eighty',
90 : 'ninety'
}


if 100 <= number <= 999:
    if int(str(number[1:])) > 21:
        stotici = int(str(number[1:]))
        desetici = int(str(number[1]))
        edinici = int(str(number[2]))
        print(f'{names.get(stotici)} hundred and {names.get(desetici*10)} {names.get(edinici)}')
    elif 1 <= int(str(number[1:])) <= 2:
        stotici = int(str(number[0]))
        edinici = int(str(number[1:]))
        print(f'{names.get(stotici)} hundred and {names.get(edinici)}')
    elif 0 < int(str(number[1:])) <= 9:
        stotici = int(str(number[0]))
        edinici = int(str(number[2]))
        print(f'{names.get(stotici)} hundred and {names.get(edinici)}')
    elif int(str(number[2])) == 0:
        stotici = int(str(number[0]))
        print(f'{names.get(stotici)} hundred')
elif 21 <= int(str(number)) <= 99:
    desetici = int(str(number[0]))
    edinici = int(str(number[1]))
    print (f'{names.get(desetici*10)} {names.get(edinici)}')
elif int(str(number)) <= 20:
    print (f'{names.get(int(str(number)))}')
    





