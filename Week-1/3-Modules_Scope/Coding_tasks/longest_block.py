letters = input()

def longest_block(string: str) -> str:
    seq = 1
    max_seq = 0
    temp_letter = string[0]
    best_letter = ''
    for i in range(1, len(string)):
        if i == len(string) - 1:
            if string[i] == temp_letter:
                seq += 1
            if seq > max_seq:
                max_seq = seq
                best_letter = string[i]
        elif string[i] != temp_letter:
            if seq > max_seq:
                max_seq = seq
                best_letter = string[i-1]
            temp_letter = string[i]
            seq = 1
        elif string[i] == temp_letter:
            seq += 1

    return max_seq * best_letter


print(longest_block(letters))
