# Elections
# You are tasked to determine how many votes are needed for a political party
# to enter the parliament and how many mandates it will take.
#
# After some research, you find out the main components:
#
# - The sum of all valid votes
# - A barrier of 4% from all valid votes
# - The sum of all actual votes - these are part of the mandate distribution
# - The coefficient mandate quote = sum of all actual votes / 240 (the seats in the parliament)
# - Each party that gets seats = the party votes/mandate quote.
#           If the remainder is > 0.5, the party gets one more seat.
#


# Sample Tests
# Input
# 415053
# 8
# Notes 2312
# JK 945
# Rodeos 45234
# Oil 8495
# XOR 104325
# ClaSS 45094
# ZOR 54325
# LSM 154323

# Output
# Notes 0
# JK 0
# Rodeos 27
# Oil 0
# XOR 62
# ClaSS 27
# ZOR 32
# LSM 92
# Explanation
# All valid counts are 415053, and the 4% barrier of them is *16602.12*;
# That means that *Notes*(2312), *JK*(945), and *Oil*(8495) won't get any seats in the parliament.
# After subtracting their votes from the valid votes, we get the actual votes = *403301*
# The mandate quote is *1680.4208* = 403301 / 240
# Rodeos has 45234 (actual votes) / 1680.4208 (quote) = 26.92, which are *27* seats
# Input
# 2460179
# 8
# Robin 343512
# Xyro 506099
# Llo 186528
# Gyro 96071
# Tom 634627
# Mermaids 232958
# Folks 115872
# Yorick 344512
# Output
# Robin 35
# Xyro 51
# Llo 19
# Gyro 0
# Tom 64
# Mermaids 24
# Folks 12
# Yorick 35

sum_votes = int(input())
n = int(input())
four_percent = (4/100) * sum_votes

all_parties = []
all_votes = []
actual_votes = []
for i in range(n):
    party_vote = input().split()
    party = party_vote[0]
    vote = party_vote[1]
    all_parties.append(party)
    all_votes.append(vote)
    if int(vote) >= four_percent:
        actual_votes.append(vote)

all_votes = [int(vote) for vote in all_votes]
actual_votes = [int(vote) for vote in actual_votes]

sum_actual_votes = sum(actual_votes)

coefficient = sum_actual_votes / 240

for j in range(len(all_votes)):
    if all_votes[j] < four_percent:
        temp_seat = 0
    else:
        temp_seat = round(all_votes[j] / coefficient)
    print(all_parties[j], temp_seat)





# - Each party that gets seats = the party votes/mandate quote.
#           If the remainder is > 0.5, the party gets one more seat.
#

#
# ouput = name of party number of seats