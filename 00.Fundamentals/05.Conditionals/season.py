month = input('Enter month: ')
date = int(input('Enter date: '))

if (month == 'March' and 20 <= date <= 31) or (month == 'April' and 1 <= date <= 30) or (month == 'May' and 1 <= date <= 31) or (month == 'June' and 1 <= date <= 20):
    season = 'Spring'
elif (month == 'June' and 21 <= date <= 30) or (month == 'July' and 1 <= date <= 31) or (month == 'August' and 1 <= date <= 31) or (month == 'September' and 1 <= date <= 21):
    season = 'Summer'
elif (month == 'September' and 22 <= date <= 30) or (month == 'October' and 1 <= date <= 31) or (month == 'November' and 1 <= date <= 30) or (month == 'December' and 1 <= date <= 20):
    season = 'Autumn'
else:
    season = 'Winter'

print (season)