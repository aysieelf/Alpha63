text_messages = int(input())
minutes = int(input())

additional_messages = text_messages - 20
if additional_messages <= 0:
    additional_messages = 0
additional_minutes = minutes - 60
if additional_minutes <= 0:
    additional_minutes = 0

additional_amount_messages = additional_messages * 0.06
additional_amount_minutes = additional_minutes * 0.10

taxes = 0.2 * (additional_amount_messages + additional_amount_minutes)
total_bill = 12 + taxes + additional_amount_messages + additional_amount_minutes

print(f'{additional_messages} additional messages for {additional_amount_messages:.2f} levas')
print(f'{additional_minutes} additional minutes for {additional_amount_minutes:.2f} levas')
print(f'{taxes:.2f} additional taxes')
print(f'{total_bill:.2f} total bill')


messages = int(input())
minutes = int(input())

price = 12.00
add_messages = messages - 20
if add_messages <= 0:
    add_messages = 0
add_minutes = minutes - 60
if add_minutes <= 0:
    add_minutes = 0

add_messages_cost = add_messages * 0.06
add_minutes_cost = add_minutes * 0.10
tax = (add_messages_cost + add_minutes_cost) * 0.20
total_bill = price + add_messages_cost + add_minutes_cost + tax

print (f'{add_messages} additional messages for {add_messages_cost:.2f} levas')
print (f'{add_minutes} additional minutes for {add_minutes_cost:.2f} levas')
print (f'{tax:.2f} additional taxes')
print (f'{total_bill:.2f} total bill')