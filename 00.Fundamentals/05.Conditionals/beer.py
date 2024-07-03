# # A beer time is after 1:00 PM (incl.) and before 3:00 AM (excl.)

# time = input()

# y = 'beer time'
# n = 'non-beer time'
# part_of_day = time[-2:]

# if time[0].isdigit() == False:
#     print('invalid time')
# else:
#     if time[2] == ':':
#             hours = int(time[0:2])
#             minutes = int(time[3:5])
#             if part_of_day == 'AM':
#                 if hours == 1 or hours == 12:
#                     print(y)
#                 elif hours == 2 and 0 <= minutes <= 59:
#                     print(y)
#                 elif 3 <= hours <= 11:
#                     print (n)
#                 else:
#                     print ('invalid time')
#             elif part_of_day == 'PM':
#                 if 1 <= hours <= 11:
#                     print(y)
#                 elif hours == 12:
#                     print (n)
#                 else:
#                     print ('invalid time')
#     elif time [1] == ':':
#             hours = int(time[0])
#             minutes = int(time[2:4])
#             if part_of_day == 'AM':
#                 if hours == 1 or hours == 12:
#                     print(y)
#                 elif hours == 2 and 0 <= minutes <= 59:
#                     print(y)
#                 elif 3 <= hours <= 11:
#                     print (n)
#                 else:
#                     print ('invalid time')
#             elif part_of_day == 'PM':
#                 if 1 <= hours <= 11:
#                     print(y)
#                 elif hours == 12:
#                     print (n)
#                 else:
#                     print ('invalid time')
#     else:
#         print ('invalid time')



time = input()

if ' ' and ':' in time:
    hours_minutes, slot = time.split(' ')
    hours, minutes = hours_minutes.split(':')
    if hours.isdigit() and minutes.isdigit() and 1 <= int(hours) <=12 and 0 <= int(minutes) <= 59 and slot in 'AMPM':
        hours = int(hours)
        minutes = int(minutes)
        if slot == 'PM':
            hours = hours + 12
        if (12 <= hours <= 23 ) or (hours < 3):
            print ('beer time')
        else:
            print ('non-beer time')
    else:
        print ('invalid time')
else:
    print ('invalid time')







