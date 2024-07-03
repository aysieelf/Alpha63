n = int(input())
best_ratio = 1
best_food = ''
best_vowels = 0

for i in range(n):
    food = input()
    vowels_sum = 0
    for ii in food:
        if ii in 'aouei':
            vowels_sum = vowels_sum + 1
    if vowels_sum/len(food) < best_ratio:
        best_ratio = vowels_sum/len(food)
        best_food = food
        best_vowels = vowels_sum
    elif vowels_sum/len(food) == best_ratio and vowels_sum > best_vowels:
        best_ratio = vowels_sum/len(food)
        best_food = food
        best_vowels = vowels_sum
    elif vowels_sum/len(food) == best_ratio and vowels_sum == best_vowels and len(food) > len(best_food):
        best_ratio = vowels_sum/len(food)
        best_food = food
        best_vowels = vowels_sum


print(f'{best_food} {best_vowels}/{len(best_food)}')